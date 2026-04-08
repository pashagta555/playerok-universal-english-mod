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
                f"\n{Fore.WHITE}Enter the {Fore.LIGHTBLUE_EX}token {Fore.WHITE}for your Playerok account. "
                f"You can find it in Cookie data using the Cookie-Editor extension."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni..."
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token saved to config successfully.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}The token you entered does not look valid. "
                    f"Make sure it matches the expected format and try again."
                )

        while not config["playerok"]["api"]["user_agent"]:
            print(
                f"\n{Fore.WHITE}Enter your browser {Fore.LIGHTMAGENTA_EX}User Agent{Fore.WHITE}. "
                f"You can copy it from {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com. "
                f"Or press Enter to skip this step."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}You skipped User Agent. The bot may behave less stably without it.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent saved to config successfully.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}The User Agent does not look valid. "
                    f"Make sure it contains no Cyrillic characters and try again."
                )
        
        while not config["playerok"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter an {Fore.LIGHTBLUE_EX}IPv4 HTTP proxy {Fore.WHITE}for your Playerok account. "
                f"Format: user:password@ip:port or ip:port if no auth. "
                f"If you do not need a proxy, press Enter to skip."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You skipped proxy.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy saved to config successfully.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}The proxy does not look valid. "
                    f"Make sure it matches the expected format and try again."
                )

    while not config["telegram"]["api"]["token"]:
        while not config["telegram"]["api"]["token"]:
            print(
                f"\n{Fore.WHITE}Enter the {Fore.CYAN}token for your Telegram bot{Fore.WHITE}. Create the bot with @BotFather."
                f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_tg_token_valid(token):
                config["telegram"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Telegram bot token saved to config successfully.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}The token you entered does not look valid. "
                    f"Make sure it matches the expected format and try again."
                )

        while not config["telegram"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter an {Fore.LIGHTBLUE_EX}IPv4 HTTP proxy {Fore.WHITE}for the Telegram bot. "
                f"Format: user:password@ip:port or ip:port if no auth. "
                f"If you do not need a proxy, press Enter to skip."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You skipped proxy.")
                break
            if is_proxy_valid(proxy):
                config["telegram"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy saved to config successfully.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}The proxy does not look valid. "
                    f"Make sure it matches the expected format and try again."
                )

    while not config["telegram"]["bot"]["password"]:
        print(
            f"\n{Fore.WHITE}Choose and enter a {Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. "
            f"The bot will ask for this password whenever someone new tries to use your bot."
            f"\n  {Fore.WHITE}· Password must be strong, at least 6 and at most 64 characters."
        )
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Password saved to config successfully.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}That password is not accepted. Use a stronger password that meets the requirements and try again.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(
            f"\n{Fore.LIGHTRED_EX}The Playerok account proxy does not seem to work. "
            f"Please check it and enter it again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok proxy is working.")

    if not is_pl_account_working():
        print(
            f"\n{Fore.LIGHTRED_EX}Could not connect to your Playerok account. "
            f"Please make sure the token is correct and enter it again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok account authorized successfully.")

    if is_pl_account_banned():
        print(
            f"{Fore.LIGHTRED_EX}\nYour Playerok account is banned! "
            f"I cannot run the bot on a blocked account."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()

    if config["telegram"]["api"]["proxy"] and not is_proxy_working(
        config["telegram"]["api"]["proxy"], 
        "https://api.telegram.org/"
    ):
        print(
            f"{Fore.LIGHTRED_EX}\nThe Telegram bot proxy does not seem to work. "
            f"Please check it and enter it again."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["telegram"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram proxy is working.")

    if not is_tg_bot_exists():
        print(
            f"{Fore.LIGHTRED_EX}\nCould not reach your Telegram bot. "
            f"If you are in Russia, Telegram may be blocked; use a proxy for the bot or a VPN."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram bot is reachable.")


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
            f"\n{Fore.LIGHTRED_EX}The bot hit an unexpected error and stopped."
            f"\n\n{Fore.WHITE}Please check our article with common issues and fixes.",
            f"\nArticle: {Fore.LIGHTWHITE_EX}https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26 {Fore.WHITE}(CTRL + click)\n"
        )
    except KeyboardInterrupt:
        print(
            f"\n{Fore.YELLOW}Bot stopped "
            f"\n{Fore.WHITE}(Ctrl + C)\n"
        )