from __future__ import annotations
import asyncio
import textwrap
import logging
from colorama import Fore
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, InlineKeyboardMarkup
from aiogram.client.session.aiohttp import AiohttpSession
from settings import Settings as sett
from core.modules import get_modules
from core.handlers import call_bot_event
from . import router as main_router
from . import templates as templ
logger = logging.getLogger('universal.telegram')

def get_telegram_bot() -> TelegramBot | None:
    if hasattr(TelegramBot, 'instance'):
        return getattr(TelegramBot, 'instance')

def get_telegram_bot_loop() -> asyncio.AbstractEventLoop | None:
    if hasattr(get_telegram_bot(), 'loop'):
        return getattr(get_telegram_bot(), 'loop')

class TelegramBot:

    def __new__(cls, *args, **kwargs) -> TelegramBot:
        if not hasattr(cls, 'instance'):
            cls.instance = super(TelegramBot, cls).__new__(cls)
        return getattr(cls, 'instance')

    def __init__(self):
        logging.getLogger('aiogram').setLevel(logging.CRITICAL)
        logging.getLogger('aiogram.event').setLevel(logging.CRITICAL)
        logging.getLogger('aiogram.dispatcher').setLevel(logging.CRITICAL)
        config = sett.get('config')
        self.token = config['telegram']['api']['token']
        self.proxy = config['telegram']['api']['proxy']
        if self.proxy:
            session = AiohttpSession(proxy=f'http://{self.proxy}')
        else:
            session = None
        self.bot = Bot(token=self.token, session=session)
        self.dp = Dispatcher()
        for module in get_modules():
            for router in module.telegram_bot_routers:
                main_router.include_router(router)
        self.dp.include_router(main_router)

    async def _set_main_menu(self):
        try:
            main_menu_commands = [BotCommand(command='/start', description='🏠 Main menu'), BotCommand(command='/restart', description='🔄️ Reboot')]
            await self.bot.set_my_commands(main_menu_commands)
        except:
            pass

    async def _set_short_description(self):
        try:
            short_description = textwrap.dedent(f'\n                Playerok Universal — бесплатный бот-помощник для playerok.com\n                \n                📢 @alexeyproduction\n                🤖 @alexey_production_bot\n                🧑\u200d💻 @alleexxeeyy\n            ')
            await self.bot.set_my_short_description(short_description=short_description)
        except:
            pass

    async def _set_description(self):
        try:
            description = textwrap.dedent(f'\n                🟢 Вечный онлайн\n                ♻️ Авто-восстановление товаров\n                ⬆️ Авто-поднятие товаров\n                💸 Авто-вывод средств\n                🚀 Авто-выдача товаров\n                ❗ Кастомные команды\n                💬 Вызов продавца\n                👋 Приветственное сообщение\n                📊 Подробная статистика\n                📲 Уведомления в Telegram\n                🖌️ Кастомизация\n                🔌 Плагины\n                                        \n                ⬇️ Скачать бота: https://github.com/alleexxeeyy/playerok-universal\n                \n                📢 Канал: @alexeyproduction\n                🤖 Бот: @alexey_production_bot\n                🧑\u200d💻 Автор: @alleexxeeyy\n            ')
            await self.bot.set_my_description(description=description)
        except:
            pass

    async def run_bot(self, from_tg=False):
        self.loop = asyncio.get_running_loop()
        await self._set_main_menu()
        await self._set_short_description()
        await self._set_description()
        await call_bot_event('ON_TELEGRAM_BOT_INIT', [self])
        me = await self.bot.get_me()
        logger.info('')
        logger.info(f'{Fore.LIGHTBLUE_EX}Telegram bot {Fore.LIGHTWHITE_EX}@{me.username} {Fore.LIGHTBLUE_EX}launched and active')
        if self.proxy:
            if '@' in self.proxy:
                user, password = self.proxy.split('@')[0].split(':')
                ip, port = self.proxy.split('@')[1].split(':')
            else:
                user, password = (None, None)
                ip, port = self.proxy.split(':')
            ip = '.'.join(['*' * len(nums) if i >= 3 else nums for i, nums in enumerate(ip.split('.'), start=1)])
            port = f'{port[:3]}**'
            user = f'{user[:3]}*****' if user else '-'
            password = f'{password[:3]}*****' if password else '-'
            logger.info('')
            logger.info(f'{Fore.LIGHTBLUE_EX}───────────────────────────────────────')
            logger.info(f'{Fore.LIGHTBLUE_EX}Proxy information:')
            logger.info(f' · IP: {Fore.LIGHTWHITE_EX}{ip}:{port}')
            logger.info(f' · User: {Fore.LIGHTWHITE_EX}{user}')
            logger.info(f' · Password: {Fore.LIGHTWHITE_EX}{password}')
            logger.info(f'{Fore.LIGHTBLUE_EX}───────────────────────────────────────')
        if from_tg:
            await self.notify_bot_restarted()
        while True:
            try:
                await self.dp.start_polling(self.bot, skip_updates=True, handle_signals=False)
            except:
                pass

    async def notify_bot_restarted(self):
        config = sett.get('config')
        for user_id in config['telegram']['bot']['signed_users']:
            await self.bot.send_message(chat_id=user_id, text='✅ Бот был <b>успешно перезагружен</b>', reply_markup=templ.destroy_kb(), parse_mode='HTML')

    async def call_seller(self, calling_name: str, chat_id: int | str):
        config = sett.get('config')
        for user_id in config['telegram']['bot']['signed_users']:
            await self.bot.send_message(chat_id=user_id, text=templ.call_seller_text(calling_name, f'https://playerok.com/chats/{chat_id}'), reply_markup=templ.destroy_kb(), parse_mode='HTML')

    async def log_event(self, text: str, kb: InlineKeyboardMarkup | None=None):
        config = sett.get('config')
        chat_id = config['playerok']['tg_logging']['chat_id']
        if not chat_id:
            for user_id in config['telegram']['bot']['signed_users']:
                await self.bot.send_message(chat_id=user_id, text=text, reply_markup=kb, parse_mode='HTML')
        else:
            await self.bot.send_message(chat_id=chat_id, text=f'{text}\n<span class="tg-spoiler">Переключите чат логов на чат с ботом, чтобы отображалось меню с действиями</span>', reply_markup=None, parse_mode='HTML')