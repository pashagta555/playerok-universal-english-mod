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
                f"\n{Fore.WHITE}Enter{Fore.LIGHTBLUE_EX}token{Fore.WHITE}your Playerok account."
                f"You can find it out from Cookie data, use the Cookie-Editor extension."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni..."
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}The token was successfully saved to the config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It looks like you entered an incorrect token."
                    f"Make sure it matches the format and try again."
                )

        while not config["playerok"]["api"]["user_agent"]:
            print(
                f"\n{Fore.WHITE}Enter{Fore.LIGHTMAGENTA_EX}User Agent {Fore.WHITE}your browser."
                f"It can be copied on the website{Fore.LIGHTWHITE_EX}https://whatmyuseragent.com. "
                f"Or you can skip this option by pressing Enter."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}You missed entering User Agent. Please note that in this case the bot may become unstable.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent successfully saved to config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It looks like you entered an incorrect User Agent."
                    f"Make sure there are no Russian characters in it and try again."
                )
        
        while not config["playerok"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter{Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy{Fore.WHITE}for Playerok account."
                f"Format: user:password@ip:port or ip:port if it is without authorization."
                f"If you don't know what this is, or don't want to install a proxy, skip this option by pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You missed entering a proxy.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}The proxy was successfully saved in the config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It looks like you entered an incorrect Proxy."
                    f"Make sure it matches the format and try again."
                )

    while not config["telegram"]["api"]["token"]:
        while not config["telegram"]["api"]["token"]:
            print(
                f"\n{Fore.WHITE}Enter{Fore.CYAN}token of your Telegram bot{Fore.WHITE}. The bot needs to be created by @BotFather."
                f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_tg_token_valid(token):
                config["telegram"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}The Telegram bot token has been successfully saved to the config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It looks like you entered an incorrect token."
                    f"Make sure it matches the format and try again."
                )

        while not config["telegram"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter{Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy{Fore.WHITE}for Telegram bot."
                f"Format: user:password@ip:port or ip:port if it is without authorization."
                f"If you don't know what this is, or don't want to install a proxy, skip this option by pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You missed entering a proxy.")
                break
            if is_proxy_valid(proxy):
                config["telegram"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}The proxy was successfully saved in the config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It looks like you entered an incorrect proxy."
                    f"Make sure it matches the format and try again."
                )

    while not config["telegram"]["bot"]["password"]:
        print(
            f"\n{Fore.WHITE}Think and enter{Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. "
            f"The bot will request this password every time another user tries to interact with your Telegram bot."
            f"\n  {Fore.WHITE}· The password must be complex, at least 6 and no more than 64 characters long."
        )
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}The password was successfully saved in the config.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}Your password is not correct. Make sure it fits the format and is not lightweight and try again.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(
            f"\n{Fore.LIGHTRED_EX}It seems that the proxy for Playerok account is not working."
            f"Please check it and enter again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok the proxy is working successfully.")

    if not is_pl_account_working():
        print(
            f"\n{Fore.LIGHTRED_EX}Failed to connect to your Playerok account."
            f"Please make sure you have the correct token and enter it again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok The account has been successfully authorized.")

    if is_pl_account_banned():
        print(
            f"{Fore.LIGHTRED_EX}\nYour Playerok account has been banned!"
            f"Unfortunately, I can't run the bot on a blocked account..."
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
            f"{Fore.LIGHTRED_EX}\nIt looks like the Telegram bot proxy is not working."
            f"Please check it and enter again."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["telegram"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram the proxy is working successfully.")

    if not is_tg_bot_exists():
        print(
            f"{Fore.LIGHTRED_EX}\nFailed to connect to your Telegram bot."
            f"If you are in Russia, you need to connect a proxy to the Telegram bot or use a VPN, due to blocking by the RKN."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram The bot is working successfully.")


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
            f"\n   {Fore.YELLOW}Our links:"
            f"\n   {Fore.WHITE}· TG bot:{Fore.LIGHTWHITE_EX}https://t.me/alexey_production_bot"
            f"\n   {Fore.WHITE}· TG channel:{Fore.LIGHTWHITE_EX}https://t.me/alexeyproduction"
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
            f"\n{Fore.LIGHTRED_EX}Your bot encountered an unexpected error and was turned off."
            f"\n\n{Fore.WHITE}Please try to find your problem in our article, which contains all the most common errors.",
            f"\nArticle:{Fore.LIGHTWHITE_EX}https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26 {Fore.WHITE}(CTRL + Click LMB)\n"
        )
    except KeyboardInterrupt:
        print(
            f"\n{Fore.YELLOW}The bot has stopped working"
            f"\n{Fore.WHITE}(you pressed Ctrl + C)\n"
        )