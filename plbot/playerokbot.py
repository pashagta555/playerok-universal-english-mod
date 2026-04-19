The provided text is a Python script that uses the `asyncio` library to create an asynchronous bot for interacting with the Playerok API. Here's the translation:

```
from __future__ import annotations
import asyncio

# Importing necessary libraries


class PlayerokBot:
    def __init__(self):
        # Initialization of the class

    async def run_bot(self):
        logger.info("")  # Log information message
        logger.info(f"{Fore.YELLOW}Playerok бот запущен и активен")  # Log bot start message
        logger.info("")  # Log new line

        # Print account information and other statistics

        profile = self.account.profile
        if profile.balance:
            logger.info(f" · Баланс: {Fore.LIGHTWHITE_EX}{profile.balance.value}₽")  # Log balance information
            logger.info(f"   · Доступно: {Fore.LIGHTWHITE_EX}{profile.balance.available}₽")
            logger.info(f"   · В ожидании: {Fore.LIGHTWHITE_EX}{profile.balance.pending_income}₽")
            logger.info(f"   · Заморожено: {Fore.LIGHTWHITE_EX}{profile.balance.frozen}₽")

        # Print number of active deals

        logger.info(f"{Fore.YELLOW}───────────────────────────────────────")  # Log separator
        logger.info("")

        proxy = self.config["playerok"]["api"]["proxy"]
        if proxy:
            user, password = None, None
            ip, port = proxy.split(":")
            
            ip = ".".join([("*" * len(nums)) if i >= 3 else nums for i, nums in enumerate(ip.split("."), start=1)])
            port = f"{port[:3]}**"
            user = f"{user[:3]}*****" if user else "-"
            password = f"{password[:3]}*****" if password else "-"

            logger.info(f"{Fore.YELLOW}───────────────────────────────────────")  # Log separator
            logger.info(f"{Fore.YELLOW}Информация о прокси:")
            logger.info(f" · IP: {Fore.LIGHTWHITE_EX}{ip}:{port}")
            logger.info(f" · Юзер: {Fore.LIGHTWHITE_EX}{user}")
            logger.info(f" · Пароль: {Fore.LIGHTWHITE_EX}{password}")
            logger.info(f"{Fore.YELLOW}───────────────────────────────────────")  # Log separator
            logger.info("")

        add_bot_event_handler("ON_PLAYEROK_BOT_INIT", PlayerokBot._on_playerok_bot_init, 0)
        add_playerok_event_handler(EventTypes.NEW_MESSAGE, PlayerokBot._on_new_message, 0)
        add_playerok_event_handler(EventTypes.NEW_REVIEW, PlayerokBot._on_new_review, 0)
        add_playerok_event_handler(EventTypes.DEAL_HAS_PROBLEM, PlayerokBot._on_new_problem, 0)
        add_playerok_event_handler(EventTypes.NEW_DEAL, PlayerokBot._on_new_deal, 0)
        add_playerok_event_handler(EventTypes.ITEM_PAID, PlayerokBot._on_item_paid, 0)
        add_playerok_event_handler(EventTypes.DEAL_STATUS_CHANGED, PlayerokBot._on_deal_status_changed, 0)

        async def listener_loop():
            listener = EventListener(self.account)
            for event in listener.listen():
                await call_playerok_event(event.type, [self, event])

        run_async_in_thread(listener_loop)
        await call_bot_event("ON_PLAYEROK_BOT_INIT", [self])
```

Please note that this translation assumes the original text is a Python script. If the text has other formats or purposes, please provide more context for accurate translation.

