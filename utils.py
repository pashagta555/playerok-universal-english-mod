import pytz
import re
from datetime import datetime, timedelta
from collections import Counter
import base64
import string
import requests
from logging import getLogger
from colorama import Fore

from playerokapi.account import Account

from settings import Settings as sett
from data import Data as data


logger = getLogger("universal")


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
        config = sett.get("config")
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
        config = sett.get("config")
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


def is_proxy_working(proxy: str, test_url="https://playerok.com", timeout=10) -> bool:
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}"
    }
    try:
        response = requests.get(test_url, proxies=proxies, timeout=timeout)
        return response.status_code < 404
    except Exception:
        return False


def is_tg_token_valid(token: str) -> bool:
    pattern = r'^\d{7,12}:[A-Za-z0-9_-]{35}$'
    return bool(re.match(pattern, token))


def is_tg_bot_exists() -> bool:
    try:
        config = sett.get("config")
        token = config["telegram"]["api"]["token"]
        proxy = config["telegram"]["api"]["proxy"]
        
        if proxy:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}",
            }
        else:
            proxies = None
        
        response = requests.get(
            f"https://api.telegram.org/bot{token}/getMe", 
            proxies=proxies,
            timeout=5
        )
        
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


def configure_config():
    config = sett.get("config")
    
    while not config["playerok"]["api"]["token"]:
        while not config["playerok"]["api"]["token"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}token {Fore.WHITE}your Playerok account. "
                f"His Can to know from Cookie-data, take advantage expansion Cookie-Editor."
                f"\n  {Fore.WHITE}· Example: eyJhbGciOiJIUzI1NiIsInR5cCI1IkpXVCJ9.eyJzdWIiOiIxZWUxMzg0Ni..."
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_token_valid(token):
                config["playerok"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token successfully saved V config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It seems, What You introduced incorrect token. "
                    f"Make sure, What He corresponds format And try it more once."
                )

        while not config["playerok"]["api"]["user_agent"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTMAGENTA_EX}User Agent {Fore.WHITE}your browser. "
                f"His Can copy on website {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com. "
                f"Or You you can skip this parameter, pressing Enter."
                f"\n  {Fore.WHITE}· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not user_agent:
                print(f"\n{Fore.YELLOW}You missed input User Agent. Please note, What V like this case bot Maybe work unstable.")
                break
            if is_user_agent_valid(user_agent):
                config["playerok"]["api"]["user_agent"] = user_agent
                sett.set("config", config)
                print(f"\n{Fore.GREEN}User Agent successfully saved V config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It seems, What You introduced incorrect User Agent. "
                    f"Make sure, What V him No Russians characters And try it more once."
                )
        
        while not config["playerok"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy {Fore.WHITE}For Playerok account. "
                f"Format: user:password@ip:port or ip:port, If He without authorization. "
                f"If You Not you know What This, or Not want install proxy - skip it this parameter, pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You missed input proxy.")
                break
            if is_proxy_valid(proxy):
                config["playerok"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy successfully saved V config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It seems, What You introduced incorrect Proxy. "
                    f"Make sure, What He corresponds format And try it more once."
                )

    while not config["telegram"]["api"]["token"]:
        while not config["telegram"]["api"]["token"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.CYAN}token your Telegram bot{Fore.WHITE}. Botha need to create at @BotFather."
                f"\n  {Fore.WHITE}· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
            )
            token = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if is_tg_token_valid(token):
                config["telegram"]["api"]["token"] = token
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Token Telegram bot successfully saved V config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It seems, What You introduced incorrect token. "
                    f"Make sure, What He corresponds format And try it more once."
                )

        while not config["telegram"]["api"]["proxy"]:
            print(
                f"\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy {Fore.WHITE}For Telegram bot. "
                f"Format: user:password@ip:port or ip:port, If He without authorization. "
                f"If You Not you know What This, or Not want install proxy - skip it this parameter, pressing Enter."
                f"\n  {Fore.WHITE}· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
            if not proxy:
                print(f"\n{Fore.WHITE}You missed input proxy.")
                break
            if is_proxy_valid(proxy):
                config["telegram"]["api"]["proxy"] = proxy
                sett.set("config", config)
                print(f"\n{Fore.GREEN}Proxy successfully saved V config.")
            else:
                print(
                    f"\n{Fore.LIGHTRED_EX}It seems, What You introduced incorrect proxy. "
                    f"Make sure, What He corresponds format And try it more once."
                )

    while not config["telegram"]["bot"]["password"]:
        print(
            f"\n{Fore.WHITE}Come up with And enter {Fore.YELLOW}password For your Telegram bot{Fore.WHITE}. "
            f"Bot will request this password at each new attempt interactions someone else's user With yours Telegram bot."
            f"\n  {Fore.WHITE}· Password must be complex, length Not less 6 And Not more 64 characters."
        )
        password = input(f"  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}").strip()
        if is_password_valid(password):
            config["telegram"]["bot"]["password"] = password
            sett.set("config", config)
            print(f"\n{Fore.GREEN}Password successfully saved V config.")
        else:
            print(f"\n{Fore.LIGHTRED_EX}Your password Not fits. Make sure, What He corresponds format And Not is light And try it more once.")

    if config["playerok"]["api"]["proxy"] and not is_proxy_working(config["playerok"]["api"]["proxy"]):
        print(
            f"\n{Fore.LIGHTRED_EX}It seems, What proxy For Playerok account Not works. "
            f"Please, check his And enter again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return configure_config()
    elif config["playerok"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok proxy successfully works.")

    if not is_pl_account_working():
        print(
            f"\n{Fore.LIGHTRED_EX}Not succeeded connect To yours Playerok account. "
            f"Please, make sure, What at you indicated loyal token And enter his again."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Playerok account successfully authorized.")

    if is_pl_account_banned():
        print(
            f"{Fore.LIGHTRED_EX}\nYour Playerok account banned! "
            f"Alas, I Not Can run bot on blocked account..."
        )
        config["playerok"]["api"]["token"] = ""
        config["playerok"]["api"]["user_agent"] = ""
        config["playerok"]["api"]["proxy"] = ""
        sett.set("config", config)
        return configure_config()

    if config["telegram"]["api"]["proxy"] and not is_proxy_working(
        config["telegram"]["api"]["proxy"], 
        "https://api.telegram.org/"
    ):
        print(
            f"{Fore.LIGHTRED_EX}\nIt seems, What proxy For Telegram bot Not works. "
            f"Please, check his And enter again."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return configure_config()
    elif config["telegram"]["api"]["proxy"]:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram proxy successfully works.")

    if not is_tg_bot_exists():
        print(
            f"{Fore.LIGHTRED_EX}\nNot succeeded connect To yours Telegram bot. "
            f"If You you are on territories Russia, to you need to connect proxy To Telegram bot or use VPN, V mind blocking with sides RKN."
        )
        config["telegram"]["api"]["token"] = ""
        config["telegram"]["api"]["proxy"] = ""
        sett.set("config", config)
        return configure_config()
    else:
        logger.info(f"{Fore.LIGHTYELLOW_EX}Telegram bot successfully works.")


def get_stats():
    cached_orders = data.get("cached_orders")

    now = datetime.now(pytz.timezone("Europe/Moscow"))
    day_ago = now - timedelta(days=1)
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)

    day_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o["date"]) >= day_ago]
    week_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o["date"]) >= week_ago]
    month_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o["date"]) >= month_ago]
    all_orders = list(cached_orders.values())

    day_active = [o for o in day_orders if not o["status"].startswith("CONFIRMED") and not o["status"].startswith("ROLLED_BACK")]
    week_active = [o for o in week_orders if not o["status"].startswith("CONFIRMED") and not o["status"].startswith("ROLLED_BACK")]
    month_active = [o for o in month_orders if not o["status"].startswith("CONFIRMED") and not o["status"].startswith("ROLLED_BACK")]
    all_active = [o for o in all_orders if not o["status"].startswith("CONFIRMED") and not o["status"].startswith("ROLLED_BACK")]

    day_completed = [o for o in day_orders if o["status"].startswith("CONFIRMED")]
    week_completed = [o for o in week_orders if o["status"].startswith("CONFIRMED")]
    month_completed = [o for o in month_orders if o["status"].startswith("CONFIRMED")]
    all_completed = [o for o in all_orders if o["status"].startswith("CONFIRMED")]

    day_refunded = [o for o in day_orders if o["status"].startswith("ROLLED_BACK")]
    week_refunded = [o for o in week_orders if o["status"].startswith("ROLLED_BACK")]
    month_refunded = [o for o in month_orders if o["status"].startswith("ROLLED_BACK")]
    all_refunded = [o for o in all_orders if o["status"].startswith("ROLLED_BACK")]

    day_profit = round(sum(o["price"] for o in day_orders if o["status"].startswith("CONFIRMED")), 2)
    week_profit = round(sum(o["price"] for o in week_orders if o["status"].startswith("CONFIRMED")), 2)
    month_profit = round(sum(o["price"] for o in month_orders if o["status"].startswith("CONFIRMED")), 2)
    all_profit = round(sum(o["price"] for o in all_orders if o["status"].startswith("CONFIRMED")), 2)

    day_best = Counter(o["item_name"] for o in day_orders).most_common(1)[0][0] if day_orders else "-"
    week_best = Counter(o["item_name"] for o in week_orders).most_common(1)[0][0] if day_orders else "-"
    month_best = Counter(o["item_name"] for o in month_orders).most_common(1)[0][0] if day_orders else "-"
    all_best = Counter(o["item_name"] for o in all_orders).most_common(1)[0][0] if day_orders else "-"

    return {
        "day": {
            "orders": len(day_orders),
            "active": len(day_active),
            "completed": len(day_completed),
            "refunded": len(day_refunded),
            "profit": day_profit,
            "best": day_best
        },
        "week": {
            "orders": len(week_orders),
            "active": len(week_active),
            "completed": len(week_completed),
            "refunded": len(week_refunded),
            "profit": week_profit,
            "best": week_best
        },
        "month": {
            "orders": len(month_orders),
            "active": len(month_active),
            "completed": len(month_completed),
            "refunded": len(month_refunded),
            "profit": month_profit,
            "best": month_best
        },
        "all": {
            "orders": len(all_orders),
            "active": len(all_active),
            "completed": len(all_completed),
            "refunded": len(all_refunded),
            "profit": all_profit,
            "best": all_best
        }
    }