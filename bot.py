import asyncio
import re
import string
import requests
import traceback
import base64
from colorama import Fore, init as init_colorama
from logging import getLogger

from playerokapi.account import Account

from __init__ import ACCENT_COLOR, VERSION
from settings import Settings as sett
from core.utils import (
    set_title, 
    setup_logger, 
    install_requirements, 
    patch_requests, 
    init_main_loop, 
    run_async_in_thread
)
from core.modules import (
    load_modules, 
    set_modules, 
    connect_modules
)
from core.handlers import call_bot_event
from updater import check_for_updates


logger = getLogger(f"universal")

main_loop = asyncio.get_event_loop()
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

    def is_token_valid(token: str) -> bool:
        if not re.match(r"^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$", token):
            return False
        try:
            header, payload, signature = token.split('.')
            for part in (header, payload, signature):
                padding = '=' * (-len(part) % 4)
                base64.urlsafe_b64decode(part + padding)
            return True
        except Exception:
            return False
    
    def is_pl_account_working() -> bool:
        try:
            Account(
                token=config["playerok"]["api"]["token"],
                user_agent=config["playerok"]["api"]["user_agent"],
                requests_timeout=config["playerok"]["api"]["requests_timeout"],
                proxy=config["playerok"]["api"]["proxy"] or None
            ).get()
            return True
        except:
            return False
    
    def is_pl_account_banned() -> bool:
        try:
            acc = Account(
                token=config["playerok"]["api"]["token"],
                user_agent=config["playerok"]["api"]["user_agent"],
                requests_timeout=config["playerok"]["api"]["requests_timeout"],
                proxy=config["playerok"]["api"]["proxy"] or None
            ).get()
            return acc.profile.is_blocked
        except:
            return False

    def is_user_agent_valid(ua: str) -> bool:
        if not ua or not (10 <= len(ua) <= 512):
            return False
        allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' '
        return all(c in allowed_chars for c in ua)

    def is_proxy_valid(proxy: str) -> bool:
        ip_pattern = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'
        pattern_ip_port = re.compile(
            rf'^{ip_pattern}\.{ip_pattern}\.{ip_pattern}\.{ip_pattern}:(\d+)$'
        )
        pattern_auth_ip_port = re.compile(
            rf'^[^:@]+:[^:@]+@{ip_pattern}\.{ip_pattern}\.{ip_pattern}\.{ip_pattern}:(\d+)$'
        )
        match = pattern_ip_port.match(proxy)
        if match:
            port = int(match.group(1))
            return 1 <= port <= 65535
        match = pattern_auth_ip_port.match(proxy)
        if match:
            port = int(match.group(1))
            return 1 <= port <= 65535
        return False
    
    def is_proxy_working(proxy: str, timeout: int = 10) -> bool:
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        test_url = "https://playerok.com"
        try:
            response = requests.get(test_url, proxies=proxies, timeout=timeout)
            return response.status_code in [200, 403]
        except Exception:
            return False
    
    def is_tg_token_valid(token: str) -> bool:
        pattern = r'^\d{7,12}:[A-Za-z0-9_-]{35}$'
        return bool(re.match(pattern, token))
    
    def is_tg_bot_exists() -> bool:
        try:
            response = requests.get(f"https://api.telegram.org/bot{config['telegram']['api']['token']}/getMe", timeout=5)
            data = response.json()
            return data.get("ok", False) is True and data.get("result", {}).get("is_bot", False) is True
        except Exception:
            return False
        
    def is_password_valid(password: str) -> bool:
        if len(password) < 6 or len(password) > 64:
            return False
        common_passwords = {
            "123456", "1234567", "12345678", "123456789", "password", "qwerty",
            "admin", "123123", "111111", "abc123", "letmein", "welcome",
            "monkey", "login", "root", "pass", "test", "000000", "user",
            "qwerty123", "iloveyou"
        }
        if password.lower() in common_passwords:
            return False
        return True
    
    while not config["playerok"]["api"]["token"]:
        while not config["playerok"]["api"]["token"]:
            print(f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}token{Fore.WHITE}Of your Playerok account. You can find it from Cookie data, use the Cookie-Editor extension."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni...")
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token was succesfully saved to the config.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems that you entered an incorrect token. Make sure it matches the format and try again.")

        while not config["playerok"]["api"]["user_agent"]:
            print(f"\n{Fore.WHITE}Enter {Fore.LIGHTMAGENTA_EX}User Agent {Fore.WHITE}of your browser. It can be copied on the website {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com. Or you can skip this option by pressing Enter."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}You missed entering the User Agent. Please note that in this case the bot may work unstable.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent has been successfully saved to the config.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems that you entered an incorrect User Agent. Make sure there are no non-english characters in it and try again.")
        
        while not config["playerok"]["api"]["proxy"]:
            print(f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 proxy {Fore.WHITE}in format user:password@ip:port or ip:port, in case it is without authorization. If you don't know what it is or don't want to install a proxy, skip this option by pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000")
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You missed the proxy input.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}The proxy has been successfully saved in the configuration.")
            else:
                print(f"\n{Fore.LIGHTRED_EX}It seems that you entered the wrong Proxy. Make sure it matches the format and try again.")

    while not config["telegram"]["api"]["token"]:
        print(f"\n{Fore.WHITE}Enter {Fore.CYAN}token of your Telegram bot{Fore.WHITE}. You need to create a bot from @BotFather."
              f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM")
        token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_tg_token_valid(token):
            config["telegram"]["api"]["token"] = token
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Telegram bot token successfully saved to the config.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}It seems that you entered an incorrect token. Make sure it matches the format and try again.")

    while not config["telegram"]["bot"]["password"]:
        print(f"\n{Fore.WHITE}Come up with and enter {Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. The bot will request this password every time someone else's attempt to interact with your Telegram bot."
              f"\n  {Fore.WHITE}· The password must be complex, at least 6 and no more than 64 characters long.")
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}The password has been successfully saved in the configuration.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}Your password does not match. Make sure it matches the format and is not easy and try again.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(f"\n{Fore.LIGHTRED_EX}It seems that the proxy you specified does not work. Please check it and enter it again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.WHITE}The proxy works successfully.")

    if not is_pl_account_working():
        print(f"\n{Fore.LIGHTRED_EX}Failed to connect to your Playerok account. Please make sure that you have the correct token and enter it again.")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Playerok account has been successfully authorized.")

    if is_pl_account_banned():
        print(f"{Fore.LIGHTRED_EX}\nВаш Playerok аккаунт забанен! Увы, я не могу запустить бота на заблокированном аккаунте...")
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return check_and_configure_config()

    if not is_tg_bot_exists():
        print(f"\n{Fore.LIGHTRED_EX}Failed to connect to your Telegram bot. Please make sure that you have the correct token and enter it again.")
        config["telegram"]["api"]["token"] = ""
        sett.set("config", config)
        return check_and_configure_config()
    else:
        logger.info(f"{Fore.WHITE}Telegram бот успешно работает.")


if __name__ == "__main__":
    try:
        install_requirements("requirements.txt") # установка недостающих зависимостей, если таковые есть
        patch_requests()
        setup_logger()
        
        set_title(f"Playerok Universal v{VERSION} translated by @pashagta555")
        print(
            f"\n\n   {ACCENT_COLOR}Playerok Universal {Fore.WHITE}v{Fore.LIGHTWHITE_EX}{VERSION}"
            f"\n    · {Fore.LIGHTWHITE_EX}-"
            f"\n    · {Fore.LIGHTWHITE_EX}-"
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
            f"\n{Fore.LIGHTRED_EX}Ваш бот словил непредвиденную ошибку и был выключен."
            f"\n\n{Fore.WHITE}Пожалуйста, попробуйте найти свою проблему в нашей статье, в которой собраны все самые частые ошибки.",
            f"\nСтатья: {Fore.LIGHTWHITE_EX}https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26 {Fore.WHITE}(CTRL + Клик ЛКМ)\n"
        )
    raise SystemExit(1)
