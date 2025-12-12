from __future__ import annotations
import asyncio
import time
from datetime import datetime
import time
from threading import Thread
import textwrap
import shutil
from colorama import Fore

from playerokapi.account import Account
from playerokapi import exceptions as plapi_exceptions
from playerokapi.enums import *
from playerokapi.listener.events import *
from playerokapi.listener.listener import EventListener
from playerokapi.types import Chat, Item

from __init__ import ACCENT_COLOR, VERSION
from core.utils import set_title, shutdown, run_async_in_thread
from core.handlers import add_bot_event_handler, add_playerok_event_handler, call_bot_event, call_playerok_event
from settings import DATA, Settings as sett
from logging import getLogger
from data import Data as data
from tgbot.telegrambot import get_telegram_bot, get_telegram_bot_loop
from tgbot.templates import log_text, log_new_mess_kb, log_new_deal_kb

from .stats import get_stats, set_stats


def get_playerok_bot() -> PlayerokBot | None:
    if hasattr(PlayerokBot, "instance"):
        return getattr(PlayerokBot, "instance")


class PlayerokBot:
    def __new__(cls, *args, **kwargs) -> PlayerokBot:
        if not hasattr(cls, "instance"):
            cls.instance = super(PlayerokBot, cls).__new__(cls)
        return getattr(cls, "instance")

    def __init__(self):
        self.logger = getLogger("universal.playerok")

        self.config = sett.get("config")
        self.messages = sett.get("messages")
        self.custom_commands = sett.get("custom_commands")
        self.auto_deliveries = sett.get("auto_deliveries")
        self.auto_restore_items = sett.get("auto_restore_items")

        self.initialized_users = data.get("initialized_users")
        self.stats = get_stats()

        self.account = self.playerok_account = Account(
            token=self.config["playerok"]["api"]["token"],
            user_agent=self.config["playerok"]["api"]["user_agent"],
            requests_timeout=self.config["playerok"]["api"]["requests_timeout"],
            proxy=self.config["playerok"]["api"]["proxy"] or None
        ).get()

        self.__saved_chats: dict[str, Chat] = {}
        """Dictionary of last remembered chats.\nFormat: {`chat_id` _or_ `username`: `chat_obj`, ...}"""

    def get_chat_by_id(self, chat_id: str) -> Chat:
        """ 
        Gets a chat with a user from remembered chats by its ID.
        Remembers and gets the chat if it's not remembered.
        
        :param chat_id: Chat ID.
        :type chat_id: `str`
        
        :return: Chat object.
        :rtype: `playerokapi.types.Chat`
        """
        if chat_id in self.__saved_chats:
            return self.__saved_chats[chat_id]
        self.__saved_chats[chat_id] = self.account.get_chat(chat_id)
        return self.get_chat_by_id(chat_id)

    def get_chat_by_username(self, username: str) -> Chat:
        """ 
        Gets a chat with a user from remembered chats by the interlocutor's nickname.
        Remembers and gets the chat if it's not remembered.
        
        :param username: Chat interlocutor's username.
        :type username: `str`
        
        :return: Chat object.
        :rtype: `playerokapi.types.Chat`
        """
        if username in self.__saved_chats:
            return self.__saved_chats[username]
        self.__saved_chats[username] = self.account.get_chat_by_username(username)
        return self.get_chat_by_username(username)
    
    def msg(self, message_name: str, messages_config_name: str = "messages", 
            messages_data: dict = DATA, **kwargs) -> str | None:
        """ 
        Gets a formatted message from the messages dictionary.

        :param message_name: Message name in the messages dictionary (ID).
        :type message_name: `str`

        :param messages_config_name: Messages configuration file name.
        :type messages_config_name: `str`

        :param messages_data: Configuration files data dictionary.
        :type messages_data: `dict` or `None`

        :return: Formatted message or None if message is disabled.
        :rtype: `str` or `None`
        """
        class SafeDict(dict):
            def __missing__(self, key):
                return "{" + key + "}"

        messages = sett.get(messages_config_name, messages_data) or {}
        mess = messages.get(message_name, {})
        if not mess.get("enabled"):
            return None
        message_lines: list[str] = mess.get("text", [])
        if not message_lines:
            return f"Message {message_name} is empty"
        try:
            msg = "\n".join([line.format_map(SafeDict(**kwargs)) for line in message_lines])
            return msg
        except:
            pass
        return f"Failed to get message {message_name}"
    

    def refresh_account(self):
        """Updates Playerok account data."""
        self.account = self.playerok_account = self.account.get()

    def check_banned(self):
        """
        Checks if the Playerok account is banned.
        If the account is banned, shuts down the bot.
        """
        user = self.account.get_user(self.account.id)
        if user.is_blocked:
            self.logger.critical(f"")
            self.logger.critical(f"{Fore.LIGHTRED_EX}Your Playerok account has been blocked! Unfortunately, I cannot continue working on a blocked account...")
            self.logger.critical(f"Contact Playerok support to find out the reason for the ban and resolve this issue as soon as possible.")
            self.logger.critical(f"")
            shutdown()

    def send_message(self, chat_id: str, text: str | None = None, photo_file_path: str | None = None,
                     mark_chat_as_read: bool = None, exclude_watermark: bool = False, max_attempts: int = 3) -> types.ChatMessage:
        """
        Custom method for sending a message to Playerok chat.
        Tries to send in 3 attempts, if failed - outputs an error to console.\n
        Can send a text message `text` or a photo `photo_file_path`.

        :param chat_id: Chat ID to send the message to.
        :type chat_id: `str`

        :param text: Message text, _optional_.
        :type text: `str` or `None`

        :param photo_file_path: Path to photo file, _optional_.
        :type photo_file_path: `str` or `None`

        :param mark_chat_as_read: Mark chat as read before sending, _optional_.
        :type mark_chat_as_read: `bool`

        :param exclude_watermark: Skip and don't use watermark under message?
        :type exclude_watermark: `bool`

        :return: Sent message object.
        :rtype: `PlayerokAPI.types.ChatMessage`
        """
        if not text and not photo_file_path:
            return None
        for _ in range(max_attempts):
            try:
                if (
                    text
                    and self.config["playerok"]["watermark"]["enabled"]
                    and self.config["playerok"]["watermark"]["value"]
                    and not exclude_watermark
                ):
                    text += f"\n{self.config['playerok']['watermark']['value']}"
                mark_chat_as_read = (self.config["playerok"]["read_chat"]["enabled"] or False) if mark_chat_as_read is None else mark_chat_as_read
                mess = self.account.send_message(chat_id, text, photo_file_path, mark_chat_as_read)
                return mess
            except plapi_exceptions.RequestFailedError:
                continue
            except Exception as e:
                text = text.replace('\n', ' ').strip()
                self.logger.error(f"{Fore.LIGHTRED_EX}Error sending message {Fore.LIGHTWHITE_EX}«{text}» {Fore.LIGHTRED_EX}to chat {Fore.LIGHTWHITE_EX}{chat_id} {Fore.LIGHTRED_EX}: {Fore.WHITE}{e}")
                return
        text = text.replace('\n', ' ').strip()
        self.logger.error(f"{Fore.LIGHTRED_EX}Failed to send message {Fore.LIGHTWHITE_EX}«{text}» {Fore.LIGHTRED_EX}to chat {Fore.LIGHTWHITE_EX}{chat_id}")

    def restore_last_sold_item(self, item: Item):
        """ 
        Restores the last sold item. 
        
        :param item: Item object to restore.
        :type item: `playerokapi.types.Item`
        """
        try:
            profile = self.account.get_user(id=self.account.id)
            items = profile.get_items(count=24, statuses=[ItemStatuses.SOLD]).items
            _item = [profile_item for profile_item in items if profile_item.name == item.name]
            if len(_item) <= 0: return
            try: item: types.MyItem = self.account.get_item(_item[0].id)
            except: item = _item[0]

            priority_statuses = self.account.get_item_priority_statuses(item.id, item.price)
            try: priority_status = [status for status in priority_statuses if status.type is PriorityTypes.DEFAULT or status.price == 0][0]
            except IndexError: priority_status = [status for status in priority_statuses][0]

            new_item = self.account.publish_item(item.id, priority_status.id)
            if new_item.status is ItemStatuses.PENDING_APPROVAL or new_item.status is ItemStatuses.APPROVED:
                self.logger.info(f"{Fore.LIGHTWHITE_EX}«{item.name}» {Fore.WHITE}— {Fore.YELLOW}item restored")
            else:
                self.logger.error(f"{Fore.LIGHTRED_EX}Failed to restore item «{new_item.name}». Its status: {Fore.WHITE}{new_item.status.name}")
        except Exception as e:
            self.logger.error(f"{Fore.LIGHTRED_EX}Error occurred while restoring item «{item.name}»: {Fore.WHITE}{e}")

    def get_my_items(self, statuses: list[ItemStatuses] | None = None) -> list[types.ItemProfile]:
        """
        Gets all account items.

        :param statuses: Statuses to get items with, _optional_.
        :type statuses: `list[playerokapi.enums.ItemStatuses]` or `None`

        :return: Array of profile items.
        :rtype: `list` of `playerokapi.types.ItemProfile`
        """
        user = self.account.get_user(self.account.id)
        my_items: list[types.ItemProfile] = []
        next_cursor = None
        while True:
            _items = user.get_items(statuses=statuses, after_cursor=next_cursor)
            for _item in _items.items:
                if _item.id not in [item.id for item in my_items]:
                    my_items.append(_item)
            if not _items.page_info.has_next_page:
                break
            next_cursor = _items.page_info.end_cursor
            time.sleep(0.3)
        return my_items


    def log_new_message(self, message: types.ChatMessage, chat: types.Chat):
        plbot = get_playerok_bot()
        try: chat_user = [user.username for user in chat.users if user.id != plbot.account.id][0]
        except: chat_user = message.user.username
        ch_header = f"New message in chat with {chat_user}:"
        self.logger.info(f"{ACCENT_COLOR}{ch_header.replace(chat_user, f'{Fore.LIGHTCYAN_EX}{chat_user}')}")
        self.logger.info(f"{ACCENT_COLOR}│ {Fore.LIGHTWHITE_EX}{message.user.username}:")
        max_width = shutil.get_terminal_size((80, 20)).columns - 40
        longest_line_len = 0
        text = ""
        if message.text is not None: text = message.text
        elif message.file is not None: text = f"{Fore.LIGHTMAGENTA_EX}Image {Fore.WHITE}({message.file.url})"
        for raw_line in text.split("\n"):
            if not raw_line.strip():
                self.logger.info(f"{ACCENT_COLOR}│")
                continue
            wrapped_lines = textwrap.wrap(raw_line, width=max_width)
            for wrapped in wrapped_lines:
                self.logger.info(f"{ACCENT_COLOR}│ {Fore.WHITE}{wrapped}")
                longest_line_len = max(longest_line_len, len(wrapped.strip()))
        underline_len = max(len(ch_header)-1, longest_line_len+2)
        self.logger.info(f"{ACCENT_COLOR}└{'─'*underline_len}")

    def log_new_deal(self, deal: types.ItemDeal):
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")
        self.logger.info(f"{Fore.YELLOW}New deal {deal.id}:")
        self.logger.info(f" · Buyer: {Fore.LIGHTWHITE_EX}{deal.user.username}")
        self.logger.info(f" · Item: {Fore.LIGHTWHITE_EX}{deal.item.name}")
        self.logger.info(f" · Amount: {Fore.LIGHTWHITE_EX}{deal.item.price}₽")
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")

    def log_new_review(self, deal: types.ItemDeal):
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")
        self.logger.info(f"{Fore.YELLOW}New review for deal {deal.id}:")
        self.logger.info(f" · Rating: {Fore.LIGHTYELLOW_EX}{'★' * deal.review.rating or 5} ({deal.review.rating or 5})")
        self.logger.info(f" · Text: {Fore.LIGHTWHITE_EX}{deal.review.text}")
        self.logger.info(f" · Left by: {Fore.LIGHTWHITE_EX}{deal.review.user.username}")
        self.logger.info(f" · Date: {Fore.LIGHTWHITE_EX}{datetime.fromisoformat(deal.review.created_at).strftime('%d.%m.%Y %H:%M:%S')}")
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")

    def log_deal_status_changed(self, deal: types.ItemDeal, status_frmtd: str = "Unknown"):
        self.logger.info(f"{Fore.WHITE}───────────────────────────────────────")
        self.logger.info(f"{Fore.WHITE}Deal {Fore.LIGHTWHITE_EX}{deal.id} {Fore.WHITE}status changed:")
        self.logger.info(f" · Status: {Fore.LIGHTWHITE_EX}{status_frmtd}")
        self.logger.info(f" · Buyer: {Fore.LIGHTWHITE_EX}{deal.user.username}")
        self.logger.info(f" · Item: {Fore.LIGHTWHITE_EX}{deal.item.name}")
        self.logger.info(f" · Amount: {Fore.LIGHTWHITE_EX}{deal.item.price}₽")
        self.logger.info(f"{Fore.WHITE}───────────────────────────────────────")

    def log_new_problem(self, deal: types.ItemDeal):
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")
        self.logger.info(f"{Fore.YELLOW}New complaint in deal {deal.id}:")
        self.logger.info(f" · Left by: {Fore.LIGHTWHITE_EX}{deal.user.username}")
        self.logger.info(f" · Item: {Fore.LIGHTWHITE_EX}{deal.item.name}")
        self.logger.info(f" · Amount: {Fore.LIGHTWHITE_EX}{deal.item.price}₽")
        self.logger.info(f"{Fore.YELLOW}───────────────────────────────────────")


    async def _on_playerok_bot_init(self):
        self.stats.bot_launch_time = datetime.now()

        def endless_loop():
            while True:
                balance = self.account.profile.balance.value if self.account.profile.balance is not None else "?"
                set_title(f"Playerok Universal v{VERSION} | {self.account.username}: {balance}₽")
                if self.stats != get_stats(): set_stats(self.stats)
                if data.get("initialized_users") != self.initialized_users: data.set("initialized_users", self.initialized_users)
                if sett.get("config") != self.config: self.config = sett.get("config")
                if sett.get("messages") != self.messages: self.messages = sett.get("messages")
                if sett.get("custom_commands") != self.custom_commands: self.custom_commands = sett.get("custom_commands")
                if sett.get("auto_deliveries") != self.auto_deliveries: self.auto_deliveries = sett.get("auto_deliveries")
                if sett.get("auto_restore_items") != self.auto_restore_items: self.auto_restore_items = sett.get("auto_restore_items")
                time.sleep(3)

        def refresh_account_loop():
            while True:
                time.sleep(1)
                self.refresh_account()

        def check_banned_loop():
            while True:
                self.check_banned()
                time.sleep(900)

        Thread(target=endless_loop, daemon=True).start()
        Thread(target=refresh_account_loop, daemon=True).start()
        Thread(target=check_banned_loop, daemon=True).start()

    async def _on_new_message(self, event: NewMessageEvent):
        if event.message.user is None:
            return
        self.log_new_message(event.message, event.chat)
        if event.message.user.id == self.account.id:
            return

        if (
            self.config["playerok"]["tg_logging"]["enabled"]
            and (self.config["playerok"]["tg_logging"]["events"]["new_user_message"] 
            or self.config["playerok"]["tg_logging"]["events"]["new_system_message"])
        ):
            do = False
            if self.config["playerok"]["tg_logging"]["events"]["new_user_message"] and event.message.user.username not in ["Playerok.com", "Support"]: do = True 
            if self.config["playerok"]["tg_logging"]["events"]["new_system_message"] and event.message.user.username in ["Playerok.com", "Support"]: do = True 
            if do:
                text = f"<b>{event.message.user.username}:</b> "
                text += event.message.text or ""
                text += f'<b><a href="{event.message.file.url}">{event.message.file.filename}</a></b>' if event.message.file else ""
                asyncio.run_coroutine_threadsafe(
                    get_telegram_bot().log_event(
                        text=log_text(
                            title=f'💬 New message in <a href="https://playerok.com/chats/{event.chat.id}">chat</a>', 
                            text=text.strip()
                        ),
                        kb=log_new_mess_kb(event.message.user.username)
                    ), 
                    get_telegram_bot_loop()
                )

        if event.chat.id not in [self.account.system_chat_id, self.account.support_chat_id]:
            if event.message.user.id not in self.initialized_users:
                self.send_message(event.chat.id, self.msg("first_message", username=event.message.user.username))
                self.initialized_users.append(event.message.user.id)
            
            if str(event.message.text).lower() in ["!commands"]:
                self.send_message(event.chat.id, self.msg("cmd_commands"))
            elif str(event.message.text).lower() in ["!seller"]:
                asyncio.run_coroutine_threadsafe(
                    get_telegram_bot().call_seller(event.message.user.username, event.chat.id), 
                    get_telegram_bot_loop()
                )
                self.send_message(event.chat.id, self.msg("cmd_seller"))
            elif self.config["playerok"]["custom_commands"]["enabled"]:
                if event.message.text.lower() in [key.lower() for key in self.custom_commands.keys()]:
                    msg = "\n".join(self.custom_commands[event.message.text])
                    self.send_message(event.chat.id, msg)

    async def _on_new_review(self, event: NewReviewEvent):
        if event.deal.user.id == self.account.id:
            return
        
        self.log_new_review(event.deal)
        if (
            self.config["playerok"]["tg_logging"]["enabled"] 
            and self.config["playerok"]["tg_logging"]["events"]["new_review"]
        ):
            asyncio.run_coroutine_threadsafe(
                get_telegram_bot().log_event(
                    text=log_text(
                        title=f'💬✨ New review for <a href="https://playerok.com/deal/{event.deal.id}">deal</a>', 
                        text=f"<b>Rating:</b> {'⭐' * event.deal.review.rating}\n<b>Left by:</b> {event.deal.review.creator.username}\n<b>Text:</b> {event.deal.review.text}\n<b>Date:</b> {datetime.fromisoformat(event.deal.review.created_at).strftime('%d.%m.%Y %H:%M:%S')}"
                    ),
                    kb=log_new_mess_kb(event.deal.user.username)
                ), 
                get_telegram_bot_loop()
            )

    async def _on_new_problem(self, event: ItemPaidEvent):
        if event.deal.user.id == self.account.id:
            return

        self.log_new_problem(event.deal)
        if (
            self.config["playerok"]["tg_logging"]["enabled"] 
            and self.config["playerok"]["tg_logging"]["events"]["new_problem"]
        ):
            asyncio.run_coroutine_threadsafe(
                get_telegram_bot().log_event(
                    text=log_text(
                        title=f'🤬 New complaint in <a href="https://playerok.com/deal/{event.deal.id}">deal</a>', 
                        text=f"<b>Buyer:</b> {event.deal.user.username}\n<b>Item:</b> {event.deal.item.name}"
                    ),
                    kb=log_new_mess_kb(event.deal.user.username)
                ), 
                get_telegram_bot_loop()
            )

    async def _on_new_deal(self, event: NewDealEvent):
        if event.deal.user.id == self.account.id:
            return
        
        self.log_new_deal(event.deal)
        if (
            self.config["playerok"]["tg_logging"]["enabled"] 
            and self.config["playerok"]["tg_logging"]["events"]["new_deal"]
        ):
            asyncio.run_coroutine_threadsafe(
                get_telegram_bot().log_event(
                    text=log_text(
                        title=f'📋 New <a href="https://playerok.com/deal/{event.deal.id}">deal</a>', 
                        text=f"<b>Buyer:</b> {event.deal.user.username}\n<b>Item:</b> {event.deal.item.name}\n<b>Amount:</b> {event.deal.item.price or '?'}₽"
                    ),
                    kb=log_new_deal_kb(event.deal.user.username, event.deal.id)
                ), 
                get_telegram_bot_loop()
            )

        self.send_message(event.chat.id, self.msg("new_deal", deal_item_name=event.deal.item.name, deal_item_price=event.deal.item.price))
        
        if self.config["playerok"]["auto_deliveries"]["enabled"]:
            for auto_delivery in self.auto_deliveries:
                for phrase in auto_delivery["keyphrases"]:
                    if phrase.lower() in event.deal.item.name.lower() or event.deal.item.name.lower() == phrase.lower():
                        self.send_message(event.chat.id, "\n".join(auto_delivery["message"]))
                        break
        if self.config["playerok"]["auto_complete_deals"]["enabled"]:
            self.account.update_deal(event.deal.id, ItemDealStatuses.SENT)

    async def _on_item_paid(self, event: ItemPaidEvent):
        if event.deal.user.id == self.account.id:
            return
        elif not self.config["playerok"]["auto_restore_items"]["enabled"]:
            return
        
        included = any(
            any(
                phrase.lower() in event.deal.item.name.lower()
                or event.deal.item.name.lower() == phrase.lower()
                for phrase in included_item
            )
            for included_item in self.auto_restore_items["included"]
        )
        excluded = any(
            any(
                phrase.lower() in event.deal.item.name.lower()
                or event.deal.item.name.lower() == phrase.lower()
                for phrase in excluded_item
            )
            for excluded_item in self.auto_restore_items["excluded"]
        )

        if (
            self.config["playerok"]["auto_restore_items"]["all"]
            and not excluded
        ) or (
            not self.config["playerok"]["auto_restore_items"]["all"]
            and included
        ):
            self.restore_last_sold_item(event.deal.item)
        

    async def _on_deal_status_changed(self, event: DealStatusChangedEvent):
        if event.deal.user.id == self.account.id:
            return
        
        status_frmtd = "Unknown"
        if event.deal.status is ItemDealStatuses.PAID: status_frmtd = "Paid"
        elif event.deal.status is ItemDealStatuses.PENDING: status_frmtd = "Pending shipment"
        elif event.deal.status is ItemDealStatuses.SENT: status_frmtd = "Seller confirmed completion"
        elif event.deal.status is ItemDealStatuses.CONFIRMED: status_frmtd = "Buyer confirmed deal"
        elif event.deal.status is ItemDealStatuses.ROLLED_BACK: status_frmtd = "Refund"

        self.log_deal_status_changed(event.deal, status_frmtd)
        if (
            self.config["playerok"]["tg_logging"]["enabled"] 
            and self.config["playerok"]["tg_logging"]["events"]["deal_status_changed"]
        ):
            asyncio.run_coroutine_threadsafe(
                get_telegram_bot().log_event(
                    log_text(
                        title=f'🔄️📋 <a href="https://playerok.com/deal/{event.deal.id}/">Deal</a> status changed', 
                        text=f"<b>New status:</b> {status_frmtd}"
                    )
                ), 
                get_telegram_bot_loop()
            )

        if event.deal.status is ItemDealStatuses.PENDING:
            self.send_message(event.chat.id, self.msg("deal_pending", deal_id=event.deal.id, deal_item_name=event.deal.item.name, deal_item_price=event.deal.item.price))
        if event.deal.status is ItemDealStatuses.SENT:
            self.send_message(event.chat.id, self.msg("deal_sent", deal_id=event.deal.id, deal_item_name=event.deal.item.name, deal_item_price=event.deal.item.price))
        if event.deal.status is ItemDealStatuses.CONFIRMED:
            self.send_message(event.chat.id, self.msg("deal_confirmed", deal_id=event.deal.id, deal_item_name=event.deal.item.name, deal_item_price=event.deal.item.price))
            self.stats.deals_completed += 1
            if not event.deal.transaction:
                event.deal = self.account.get_deal(event.deal.id)
            self.stats.earned_money += round(getattr(event.deal.transaction, "value") or 0, 2)
        elif event.deal.status is ItemDealStatuses.ROLLED_BACK:
            self.send_message(event.chat.id, self.msg("deal_refunded", deal_id=event.deal.id, deal_item_name=event.deal.item.name, deal_item_price=event.deal.item.price))
            self.stats.deals_refunded += 1


    async def run_bot(self):
        self.logger.info(f"{Fore.GREEN}Playerok bot is running and active")
        self.logger.info("")
        self.logger.info(f"{ACCENT_COLOR}───────────────────────────────────────")
        self.logger.info(f"{ACCENT_COLOR}Account information:")
        self.logger.info(f" · ID: {Fore.LIGHTWHITE_EX}{self.account.id}")
        self.logger.info(f" · Username: {Fore.LIGHTWHITE_EX}{self.account.username}")
        if self.playerok_account.profile.balance:
            self.logger.info(f" · Balance: {Fore.LIGHTWHITE_EX}{self.account.profile.balance.value}₽")
            self.logger.info(f"   · Available: {Fore.LIGHTWHITE_EX}{self.account.profile.balance.available}₽")
            self.logger.info(f"   · Pending: {Fore.LIGHTWHITE_EX}{self.account.profile.balance.pending_income}₽")
            self.logger.info(f"   · Frozen: {Fore.LIGHTWHITE_EX}{self.account.profile.balance.frozen}₽")
        self.logger.info(f" · Active sales: {Fore.LIGHTWHITE_EX}{self.account.profile.stats.deals.outgoing.total - self.account.profile.stats.deals.outgoing.finished}")
        self.logger.info(f" · Active purchases: {Fore.LIGHTWHITE_EX}{self.account.profile.stats.deals.incoming.total - self.account.profile.stats.deals.incoming.finished}")
        self.logger.info(f"{ACCENT_COLOR}───────────────────────────────────────")
        self.logger.info("")
        if self.config["playerok"]["api"]["proxy"]:
            user, password = self.config["playerok"]["api"]["proxy"].split("@")[0].split(":") if "@" in self.config["playerok"]["api"]["proxy"] else self.config["playerok"]["api"]["proxy"]
            ip, port = self.config["playerok"]["api"]["proxy"].split("@")[1].split(":") if "@" in self.config["playerok"]["api"]["proxy"] else self.config["playerok"]["api"]["proxy"]
            ip = ".".join([("*" * len(nums)) if i >= 3 else nums for i, nums in enumerate(ip.split("."), start=1)])
            port = f"{port[:3]}**"
            user = f"{user[:3]}*****" if user else "No authentication"
            password = f"{password[:3]}*****" if password else "No authentication"
            self.logger.info(f"{ACCENT_COLOR}───────────────────────────────────────")
            self.logger.info(f"{ACCENT_COLOR}Proxy information:")
            self.logger.info(f" · IP: {Fore.LIGHTWHITE_EX}{ip}:{port}")
            self.logger.info(f" · User: {Fore.LIGHTWHITE_EX}{user}")
            self.logger.info(f" · Password: {Fore.LIGHTWHITE_EX}{password}")
            self.logger.info(f"{ACCENT_COLOR}───────────────────────────────────────")
            self.logger.info("")

        add_bot_event_handler("ON_PLAYEROK_BOT_INIT", PlayerokBot._on_playerok_bot_init, 0)
        add_playerok_event_handler(EventTypes.NEW_MESSAGE, PlayerokBot._on_new_message, 0)
        add_playerok_event_handler(EventTypes.NEW_REVIEW, PlayerokBot._on_new_review, 0)
        add_playerok_event_handler(EventTypes.DEAL_HAS_PROBLEM, PlayerokBot._on_new_problem, 0)
        add_playerok_event_handler(EventTypes.NEW_DEAL, PlayerokBot._on_new_deal, 0)
        add_playerok_event_handler(EventTypes.ITEM_PAID, PlayerokBot._on_item_paid, 0)
        add_playerok_event_handler(EventTypes.DEAL_STATUS_CHANGED, PlayerokBot._on_deal_status_changed, 0)

        async def listener_loop():
            listener = EventListener(self.account)
            for event in listener.listen(requests_delay=self.config["playerok"]["api"]["listener_requests_delay"]):
                await call_playerok_event(event.type, [self, event])

        run_async_in_thread(listener_loop)
        self.logger.info(f"Event listener started")

        await call_bot_event("ON_PLAYEROK_BOT_INIT", [self])