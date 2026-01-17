import asyncio
import traceback
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


logger = getLogger(f"universal")

try:
    main_loop = asyncio.get_running_loop()
except RuntimeError:
    main_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(main_loop)

init_colorama()
init_main_loop(main_loop)


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
                f"\n{Fore.WHITE}Enter the {Fore.LIGHTBLUE_EX}token {Fore.WHITE}of your Playerok account. You can find it in Cookie data, use the Cookie-Editor extension."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni..."
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token successfully saved to config.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems you entered an incorrect token. Make sure it matches the format and try again.")

        while not config["playerok"]["api"]["user_agent"]:
            print(
                f"\n{Fore.WHITE}Enter the {Fore.LIGHTMAGENTA_EX}User Agent {Fore.WHITE}of your browser. You can copy it from the site {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com. Or you can skip this parameter by pressing Enter."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}You skipped entering User Agent. Note that in this case the bot may work unstably.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent successfully saved to config.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems you entered an incorrect User Agent. Make sure it doesn't contain Russian characters and try again.")
        
        while not config["playerok"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 Proxy {Fore.WHITE}in the format user:password@ip:port or ip:port if it doesn't require authentication. If you don't know what this is, or don't want to set up a proxy - skip this parameter by pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You skipped entering proxy.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy successfully saved to config.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems you entered an incorrect Proxy. Make sure it matches the format and try again.")

    while not config["telegram"]["api"]["token"]:
        print(
            f"\n{Fore.WHITE}Enter the {Fore.CYAN}token of your Telegram bot{Fore.WHITE}. You need to create the bot with @BotFather."
            f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
        )
        token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_tg_token_valid(token):
            config["telegram"]["api"]["token"] = token
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Telegram bot token successfully saved to config.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}It seems you entered an incorrect token. Make sure it matches the format and try again.")

    while not config["telegram"]["bot"]["password"]:
        print(
            f"\n{Fore.WHITE}Create and enter a {Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. The bot will request this password every time a new user tries to interact with your Telegram bot."
            f"\n  {Fore.WHITE}· Password must be complex, at least 6 and no more than 64 characters long."
        )
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Password successfully saved to config.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}Your password is not suitable. Make sure it matches the format and is not too simple and try again.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(f"\n{Fore.LIGHTRED_EX}It seems the proxy you specified is not working. Please check it and enter it again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.WHITE}Proxy is working successfully.")

    if not is_pl_account_working():
        print(f"\n{Fore.LIGHTRED_EX}Failed to connect to your Playerok account. Please make sure you have the correct token specified and enter it again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Playerok account successfully authorized.")

    if is_pl_account_banned():
        print(f"{Fore.LIGHTRED_EX}\nYour Playerok account is banned! Unfortunately, I cannot start the bot on a blocked account...")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()

    if not is_tg_bot_exists():
        print(f"\n{Fore.LIGHTRED_EX}Failed to connect to your Telegram bot. Please make sure you have the correct token specified and enter it again.")
        config["telegram"]["api"]["token"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Telegram bot is working successfully.")


if __name__ == "__main__":
    try:
        install_requirements("requirements.txt") # install missing dependencies if any
        patch_requests()
        setup_logger()
        
        set_title(f"Playerok Universal v{VERSION} by @alleexxeeyy")
        print(
            f"\n\n   {ACCENT_COLOR}Playerok Universal {Fore.WHITE}v{Fore.LIGHTWHITE_EX}{VERSION}"
            f"\n    · {Fore.LIGHTWHITE_EX}https://t.me/alleexxeeyy"
            f"\n    · {Fore.LIGHTWHITE_EX}https://t.me/alexeyproduction\n\n"
        )
        
        check_for_updates()
        check_and_configure_config()

        modules = load_modules()
        set_modules(modules)
        asyncio.run(connect_modules(modules))

        main_loop.run_until_complete(start_telegram_bot())
        main_loop.run_until_complete(start_playerok_bot())

        asyncio.run(call_bot_event("ON_INIT"))
        
        main_loop.run_forever()
    except Exception as e:
        traceback.print_exc()
        print(
            f"\n{Fore.LIGHTRED_EX}Your bot encountered an unexpected error and was shut down."
            f"\n\n{Fore.WHITE}Please try to find your problem in our article, which collects all the most common errors.",
            f"\nArticle: {Fore.LIGHTWHITE_EX}https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26 {Fore.WHITE}(CTRL + Left Click)\n"
        )