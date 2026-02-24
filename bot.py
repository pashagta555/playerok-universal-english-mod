import asyncio
import traceback
import os
from colorama import Fore, init as init_colorama
from logging import getLogger

from __init__ import ACCENT_COLOR, VERSION
from settings import Settings as sett
from core.utils import (
    set_title, 
    setup_logger, 
    install_requirements, 
    patch_requests, 
    init_main_loop, 
    run_async_in_thread,
    is_token_valid,
    is_pl_account_working,
    is_pl_account_banned,
    is_user_agent_valid,
    is_proxy_valid,
    is_proxy_working,
    is_tg_token_valid,
    is_tg_bot_exists,
    is_password_valid
)
from core.modules import (
    load_modules, 
    set_modules, 
    connect_modules
)
from core.handlers import call_bot_event
from updater import check_for_updates


logger = getLogger("universal")

try:
    main_loop = asyncio.get_running_loop()
except RuntimeError:
    main_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(main_loop)

init_colorama()
init_main_loop(main_loop)


async def clear_logs_task():
    from settings import Settings as sett
    
    path = "logs/latest.log"
    while True:
        if os.path.exists(path):
            file_size_bytes = os.path.getsize(path)
            file_size_mb = file_size_bytes / (1024 * 1024)
            
            config = sett.get("config")
            if file_size_mb > config["logs"]["max_file_size"]:
                with open(path, 'w'):
                    pass
        await asyncio.sleep(30)


async def start_telegram_bot():
    from tgbot.telegrambot import TelegramBot
    run_async_in_thread(TelegramBot().run_bot)


async def start_playerok_bot():
    from plbot.playerokbot import PlayerokBot
    await PlayerokBot().run_bot()


def check_and_configure_config():
    config = sett.get("config")
    
    while not config["playerok"]["api"]["token"]:
        while not config["playerok"]["api"]["token"]:
            print(
                f"\n{Fore.WHITE}Enter your Playerok account {Fore.LIGHTBLUE_EX}token{Fore.WHITE}. You can get it from Cookie data using the Cookie-Editor extension."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni..."
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token saved to config successfully.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}The token you entered appears to be invalid. Check the format and try again.")

        while not config["playerok"]["api"]["user_agent"]:
            print(
                f"\n{Fore.WHITE}Enter your browser's {Fore.LIGHTMAGENTA_EX}User Agent{Fore.WHITE}. You can copy it from {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com{Fore.WHITE}. Or press Enter to skip."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}User Agent was skipped. Note that the bot may run unstably without it.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent saved to config successfully.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}The User Agent you entered appears to be invalid. Ensure it contains no Cyrillic characters and try again.")
        
        while not config["playerok"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 Proxy{Fore.WHITE} as user:password@ip:port or ip:port if unauthenticated. If you don't need a proxy, press Enter to skip."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}Proxy input skipped.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy saved to config successfully.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}The proxy you entered appears to be invalid. Check the format and try again.")

    while not config["telegram"]["api"]["token"]:
        print(
            f"\n{Fore.WHITE}Enter the {Fore.CYAN}token of your Telegram bot{Fore.WHITE}. Create a bot with @BotFather if needed."
            f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
        )
        token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_tg_token_valid(token):
            config["telegram"]["api"]["token"] = token
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Telegram bot token saved to config successfully.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}The token you entered appears to be invalid. Check the format and try again.")

    while not config["telegram"]["bot"]["password"]:
        print(
            f"\n{Fore.WHITE}Choose and enter a {Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. The bot will ask for this password when an unknown user tries to use it."
            f"\n  {Fore.WHITE}· Password must be strong, between 6 and 64 characters."
        )
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Password saved to config successfully.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}Your password does not meet the requirements. Use a stronger password and try again.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(f"\n{Fore.LIGHTRED_EX}The proxy you specified does not seem to work. Please check it and enter again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.WHITE}Proxy is working.")

    if not is_pl_account_working():
        print(f"\n{Fore.LIGHTRED_EX}Could not connect to your Playerok account. Please check your token and enter it again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Playerok account authorized successfully.")

    if is_pl_account_banned():
        print(f"{Fore.LIGHTRED_EX}\nYour Playerok account is banned! I cannot run the bot on a blocked account...")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()

    if not is_tg_bot_exists():
        print(f"\n{Fore.LIGHTRED_EX}Could not connect to your Telegram bot. Please check your token and enter it again.")
        config["telegram"]["api"]["token"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Telegram bot is running.")


if __name__ == "__main__":
    try:
        install_requirements("requirements.txt") # установка недостающих зависимостей, если таковые есть
        patch_requests()
        setup_logger()
        
        set_title(f"Playerok Universal v{VERSION} by @alleexxeeyy")
        print(
            f"\n\n"
            f"\n   {ACCENT_COLOR}Playerok Universal {Fore.WHITE}v{Fore.LIGHTWHITE_EX}{VERSION}"
            f"\n"
            f"\n   {Fore.YELLOW}Links:"
            f"\n   {Fore.WHITE}· TG bot: {Fore.LIGHTWHITE_EX}https://t.me/alexey_production_bot"
            f"\n   {Fore.WHITE}· TG channel: {Fore.LIGHTWHITE_EX}https://t.me/alexeyproduction"
            f"\n   {Fore.WHITE}· GitHub: {Fore.LIGHTWHITE_EX}https://github.com/alleexxeeyy/playerok-universal"
            f"\n\n\n"
        )
        
        check_for_updates()
        check_and_configure_config()

        modules = load_modules()
        set_modules(modules)
        asyncio.run(connect_modules(modules))

        main_loop.run_until_complete(start_telegram_bot())
        main_loop.run_until_complete(start_playerok_bot())
        main_loop.create_task(clear_logs_task())

        asyncio.run(call_bot_event("ON_INIT"))
        
        main_loop.run_forever()
    except Exception as e:
        traceback.print_exc()
        print(
            f"\n{Fore.LIGHTRED_EX}The bot encountered an unexpected error and was shut down."
            f"\n\n{Fore.WHITE}Please check our article for common issues and solutions.",
            f"\nArticle: {Fore.LIGHTWHITE_EX}https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26 {Fore.WHITE}(CTRL + Click)\n"
        )