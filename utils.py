import pytz 
import re 
from datetime import datetime ,timedelta 
from collections import Counter 
import base64 
import string 
import requests 
from logging import getLogger 
from colorama import Fore 

from playerokapi .account import Account 
from playerokapi .exceptions import BotCheckDetectedException 

from settings import Settings as sett 
from data import Data as data 


logger =getLogger ("universal")


def is_cookies_valid (cookie_str :str )->bool :
    if not cookie_str or "="not in cookie_str :
        return False 

    parts =cookie_str .split (";")

    for part in parts :
        part =part .strip ()
        if "="not in part :
            return False 

        key ,value =part .split ("=",1 )

        if not key or not value :
            return False 

    return True 


def is_token_valid (token :str )->bool :
    if not re .match (r"^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$",token ):
        return False 
    try :
        header ,payload ,signature =token .split ('.')
        for part in (header ,payload ,signature ):
            padding ='='*(-len (part )%4 )
            base64 .urlsafe_b64decode (part +padding )
        return True 
    except Exception :
        return False 


def is_pl_account_working ()->tuple [bool ,str ]:
    try :
        config =sett .get ("config")
        Account (
        cookies =config ["playerok"]["api"]["cookies"],
        user_agent =config ["playerok"]["api"]["user_agent"],
        requests_timeout =config ["playerok"]["api"]["requests_timeout"],
        proxy =config ["playerok"]["api"]["proxy"]or None 
        ).get ()
        return True ,""
    except BotCheckDetectedException :
        return False ,"The verification bot noticed suspicious activity when connecting to your Playerok account. To continue working, you need to provide the current Cookie data of your authorized Playerok account."
    except :
        return False ,""


def is_pl_account_banned ()->bool :
    try :
        config =sett .get ("config")
        acc =Account (
        cookies =config ["playerok"]["api"]["cookies"],
        user_agent =config ["playerok"]["api"]["user_agent"],
        requests_timeout =config ["playerok"]["api"]["requests_timeout"],
        proxy =config ["playerok"]["api"]["proxy"]or None 
        ).get ()
        return acc .profile .is_blocked 
    except :
        return False 


def is_user_agent_valid (ua :str )->bool :
    if not ua or not (10 <=len (ua )<=512 ):
        return False 
    allowed_chars =string .ascii_letters +string .digits +string .punctuation +' '
    return all (c in allowed_chars for c in ua )


def is_proxy_valid (proxy :str )->bool :
    ip_pattern =r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'
    pattern_ip_port =re .compile (
    rf'^{ip_pattern }\.{ip_pattern }\.{ip_pattern }\.{ip_pattern }:(\d+)$'
    )
    pattern_auth_ip_port =re .compile (
    rf'^[^:@]+:[^:@]+@{ip_pattern }\.{ip_pattern }\.{ip_pattern }\.{ip_pattern }:(\d+)$'
    )
    match =pattern_ip_port .match (proxy )
    if match :
        port =int (match .group (1 ))
        return 1 <=port <=65535 
    match =pattern_auth_ip_port .match (proxy )
    if match :
        port =int (match .group (1 ))
        return 1 <=port <=65535 
    return False 


def is_proxy_working (proxy :str ,test_url ="https://playerok.com",timeout =10 )->bool :
    proxies ={
    "http":f"http://{proxy }",
    "https":f"http://{proxy }"
    }
    try :
        response =requests .get (test_url ,proxies =proxies ,timeout =timeout )
        return response .status_code <404 
    except Exception :
        return False 


def is_tg_token_valid (token :str )->bool :
    pattern =r'^\d{7,12}:[A-Za-z0-9_-]{35}$'
    return bool (re .match (pattern ,token ))


def is_tg_bot_exists ()->bool :
    try :
        config =sett .get ("config")
        token =config ["telegram"]["api"]["token"]
        proxy =config ["telegram"]["api"]["proxy"]

        if proxy :
            proxies ={
            "http":f"http://{proxy }",
            "https":f"http://{proxy }",
            }
        else :
            proxies =None 

        response =requests .get (
        f"https://api.telegram.org/bot{token }/getMe",
        proxies =proxies ,
        timeout =5 
        )

        data =response .json ()
        return data .get ("ok",False )is True and data .get ("result",{}).get ("is_bot",False )is True 
    except Exception :
        return False 


def is_password_valid (password :str )->bool :
    if len (password )<6 or len (password )>64 :
        return False 
    common_passwords ={
    "123456","1234567","12345678","123456789","password","qwerty",
    "admin","123123","111111","abc123","letmein","welcome",
    "monkey","login","root","pass","test","000000","user",
    "qwerty123","iloveyou"
    }
    if password .lower ()in common_passwords :
        return False 
    return True 


def configure_config ():
    config =sett .get ("config")

    while not config ["playerok"]["api"]["cookies"]:
        while not config ["playerok"]["api"]["cookies"]:
            print (
            f"\n{Fore .WHITE }Enter{Fore .YELLOW }Cookie Data{Fore .WHITE }your"
            f"{Fore .LIGHTWHITE_EX }authorized{Fore .WHITE }Playerok account in Header String format."
            f"\nLogin into your account on the site, and then copy the cookies using the Cookie-Editor extension (LMB on the extension -> Export -> Header String)."
            f"\n  {Fore .WHITE }· Example: __ddg3=4L7yBmrBwMwKm15X;token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
            )
            str_cookies =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()
            cookies ={
            c .split ("=")[0 ].strip ():c .split ("=")[1 ].strip ()for c 
            in str_cookies .split (";")if c .strip ()and "="in c 
            }

            if is_cookies_valid (str_cookies )and is_token_valid (cookies ["token"]):
                config ["playerok"]["api"]["cookies"]=str_cookies 
                sett .set ("config",config )
                print (f"\n{Fore .GREEN }Cookie data was successfully saved to the config.")
            else :
                print (
                f"\n{Fore .LIGHTRED_EX }It looks like you entered incorrect Cookie data."
                f"Make sure they match the format and try again."
                )

        while not config ["playerok"]["api"]["user_agent"]:
            print (
            f"\n{Fore .WHITE }Enter{Fore .LIGHTMAGENTA_EX }User Agent {Fore .WHITE }your browser."
            f"It can be copied on the website{Fore .LIGHTWHITE_EX }https://whatmyuseragent.com."
            f"\n  {Fore .WHITE }· Example: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
            )
            user_agent =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()

            if is_user_agent_valid (user_agent ):
                config ["playerok"]["api"]["user_agent"]=user_agent 
                sett .set ("config",config )
                print (f"\n{Fore .GREEN }User Agent was successfully saved to the config.")
            else :
                print (
                f"\n{Fore .LIGHTRED_EX }It looks like you entered an incorrect User Agent."
                f"Make sure there are no Russian characters in it and try again."
                )

        while not config ["playerok"]["api"]["proxy"]:
            print (
            f"\n{Fore .WHITE }Enter{Fore .LIGHTBLUE_EX }IPv4 HTTP Proxy{Fore .WHITE }for Playerok account."
            f"Format: user:password@ip:port or ip:port if it is without authorization."
            f"If you don't know what this is, or don't want to install a proxy, skip this option by pressing Enter."
            f"\n  {Fore .WHITE }· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()

            if not proxy :
                print (f"\n{Fore .WHITE }You missed entering a proxy.")
                break 
            if is_proxy_valid (proxy ):
                config ["playerok"]["api"]["proxy"]=proxy 
                sett .set ("config",config )
                print (f"\n{Fore .GREEN }The proxy was successfully saved in the config.")
            else :
                print (
                f"\n{Fore .LIGHTRED_EX }It looks like you entered an incorrect Proxy."
                f"Make sure it matches the format and try again."
                )

    while not config ["telegram"]["api"]["token"]:
        while not config ["telegram"]["api"]["token"]:
            print (
            f"\n{Fore .WHITE }Enter{Fore .CYAN }token of your Telegram bot{Fore .WHITE }. The bot needs to be created by @BotFather."
            f"\n  {Fore .WHITE }· Example: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM"
            )
            token =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()

            if is_tg_token_valid (token ):
                config ["telegram"]["api"]["token"]=token 
                sett .set ("config",config )
                print (f"\n{Fore .GREEN }The Telegram bot token has been successfully saved to the config.")
            else :
                print (
                f"\n{Fore .LIGHTRED_EX }It looks like you entered an incorrect token."
                f"Make sure it matches the format and try again."
                )

        while not config ["telegram"]["api"]["proxy"]:
            print (
            f"\n{Fore .WHITE }Enter{Fore .LIGHTBLUE_EX }IPv4 HTTP Proxy{Fore .WHITE }for Telegram bot."
            f"Format: user:password@ip:port or ip:port if it is without authorization."
            f"If you don't know what this is, or don't want to install a proxy, skip this option by pressing Enter."
            f"\n  {Fore .WHITE }· Example: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000"
            )
            proxy =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()

            if not proxy :
                print (f"\n{Fore .WHITE }You missed entering a proxy.")
                break 
            if is_proxy_valid (proxy ):
                config ["telegram"]["api"]["proxy"]=proxy 
                sett .set ("config",config )
                print (f"\n{Fore .GREEN }The proxy was successfully saved in the config.")
            else :
                print (
                f"\n{Fore .LIGHTRED_EX }It looks like you entered an incorrect proxy."
                f"Make sure it matches the format and try again."
                )

    while not config ["telegram"]["bot"]["password"]:
        print (
        f"\n{Fore .WHITE }Think and enter{Fore .YELLOW }password for your Telegram bot{Fore .WHITE }. "
        f"The bot will request this password every time another user tries to interact with your Telegram bot."
        f"\n  {Fore .WHITE }· The password must be complex, at least 6 and no more than 64 characters long."
        )
        password =input (f"  {Fore .WHITE }↳ {Fore .LIGHTWHITE_EX }").strip ()

        if is_password_valid (password ):
            config ["telegram"]["bot"]["password"]=password 
            sett .set ("config",config )
            print (f"\n{Fore .GREEN }The password was successfully saved in the config.")
        else :
            print (f"\n{Fore .LIGHTRED_EX }Your password is not correct. Make sure it fits the format and is not lightweight and try again.")

    if config ["playerok"]["api"]["proxy"]and not is_proxy_working (config ["playerok"]["api"]["proxy"]):
        print (
        f"\n{Fore .LIGHTRED_EX }It seems that the proxy for Playerok account is not working."
        f"Please check it and enter again."
        )

        config ["playerok"]["api"]["cookies"]=""
        config ["playerok"]["api"]["user_agent"]=""
        config ["playerok"]["api"]["proxy"]=""
        sett .set ("config",config )

        return configure_config ()
    elif config ["playerok"]["api"]["proxy"]:
        logger .info (f"{Fore .LIGHTYELLOW_EX }Playerok proxy is working successfully.")

    is_pl_acc_working ,reason =is_pl_account_working ()
    if not is_pl_acc_working :
        reason =reason if reason else "Failed to connect to your Playerok account. Please make sure you have the correct token and enter it again."
        print (f"\n{Fore .LIGHTRED_EX }{reason }")

        config ["playerok"]["api"]["cookies"]=""
        config ["playerok"]["api"]["user_agent"]=""
        config ["playerok"]["api"]["proxy"]=""
        sett .set ("config",config )

        return configure_config ()
    else :
        logger .info (f"{Fore .LIGHTYELLOW_EX }Playerok account has been successfully authorized.")

    if is_pl_account_banned ():
        print (
        f"{Fore .LIGHTRED_EX }\nYour Playerok account has been banned!"
        f"Unfortunately, I can't run the bot on a blocked account..."
        )

        config ["playerok"]["api"]["cookies"]=""
        config ["playerok"]["api"]["user_agent"]=""
        config ["playerok"]["api"]["proxy"]=""
        sett .set ("config",config )

        return configure_config ()

    if config ["telegram"]["api"]["proxy"]and not is_proxy_working (
    config ["telegram"]["api"]["proxy"],
    "https://api.telegram.org/"
    ):
        print (
        f"{Fore .LIGHTRED_EX }\nIt seems that the proxy for the Telegram bot is not working."
        f"Please check it and enter again."
        )

        config ["telegram"]["api"]["token"]=""
        config ["telegram"]["api"]["proxy"]=""
        sett .set ("config",config )

        return configure_config ()
    elif config ["telegram"]["api"]["proxy"]:
        logger .info (f"{Fore .LIGHTYELLOW_EX }Telegram proxy is working successfully.")

    if not is_tg_bot_exists ():
        print (
        f"{Fore .LIGHTRED_EX }\nFailed to connect to your Telegram bot."
        f"If you are in Russia, you need to connect a proxy to the Telegram bot or use a VPN, due to blocking by the RKN."
        )
        config ["telegram"]["api"]["token"]=""
        config ["telegram"]["api"]["proxy"]=""
        sett .set ("config",config )

        return configure_config ()
    else :
        logger .info (f"{Fore .LIGHTYELLOW_EX }Telegram bot is working successfully.")


def get_stats ():
    cached_orders =data .get ("cached_orders")

    now =datetime .now (pytz .timezone ("Europe/Moscow"))
    day_ago =now -timedelta (days =1 )
    week_ago =now -timedelta (days =7 )
    month_ago =now -timedelta (days =30 )

    day_orders =[o for o in cached_orders .values ()if datetime .fromisoformat (o ["date"])>=day_ago ]
    week_orders =[o for o in cached_orders .values ()if datetime .fromisoformat (o ["date"])>=week_ago ]
    month_orders =[o for o in cached_orders .values ()if datetime .fromisoformat (o ["date"])>=month_ago ]
    all_orders =list (cached_orders .values ())

    day_active =[o for o in day_orders if not o ["status"].startswith ("CONFIRMED")and not o ["status"].startswith ("ROLLED_BACK")]
    week_active =[o for o in week_orders if not o ["status"].startswith ("CONFIRMED")and not o ["status"].startswith ("ROLLED_BACK")]
    month_active =[o for o in month_orders if not o ["status"].startswith ("CONFIRMED")and not o ["status"].startswith ("ROLLED_BACK")]
    all_active =[o for o in all_orders if not o ["status"].startswith ("CONFIRMED")and not o ["status"].startswith ("ROLLED_BACK")]

    day_completed =[o for o in day_orders if o ["status"].startswith ("CONFIRMED")]
    week_completed =[o for o in week_orders if o ["status"].startswith ("CONFIRMED")]
    month_completed =[o for o in month_orders if o ["status"].startswith ("CONFIRMED")]
    all_completed =[o for o in all_orders if o ["status"].startswith ("CONFIRMED")]

    day_refunded =[o for o in day_orders if o ["status"].startswith ("ROLLED_BACK")]
    week_refunded =[o for o in week_orders if o ["status"].startswith ("ROLLED_BACK")]
    month_refunded =[o for o in month_orders if o ["status"].startswith ("ROLLED_BACK")]
    all_refunded =[o for o in all_orders if o ["status"].startswith ("ROLLED_BACK")]

    day_profit =round (sum (o ["price"]for o in day_orders if o ["status"].startswith ("CONFIRMED")),2 )
    week_profit =round (sum (o ["price"]for o in week_orders if o ["status"].startswith ("CONFIRMED")),2 )
    month_profit =round (sum (o ["price"]for o in month_orders if o ["status"].startswith ("CONFIRMED")),2 )
    all_profit =round (sum (o ["price"]for o in all_orders if o ["status"].startswith ("CONFIRMED")),2 )

    day_best =Counter (o ["item_name"]for o in day_orders ).most_common (1 )[0 ][0 ]if day_orders else "-"
    week_best =Counter (o ["item_name"]for o in week_orders ).most_common (1 )[0 ][0 ]if day_orders else "-"
    month_best =Counter (o ["item_name"]for o in month_orders ).most_common (1 )[0 ][0 ]if day_orders else "-"
    all_best =Counter (o ["item_name"]for o in all_orders ).most_common (1 )[0 ][0 ]if day_orders else "-"

    return {
    "day":{
    "orders":len (day_orders ),
    "active":len (day_active ),
    "completed":len (day_completed ),
    "refunded":len (day_refunded ),
    "profit":day_profit ,
    "best":day_best 
    },
    "week":{
    "orders":len (week_orders ),
    "active":len (week_active ),
    "completed":len (week_completed ),
    "refunded":len (week_refunded ),
    "profit":week_profit ,
    "best":week_best 
    },
    "month":{
    "orders":len (month_orders ),
    "active":len (month_active ),
    "completed":len (month_completed ),
    "refunded":len (month_refunded ),
    "profit":month_profit ,
    "best":month_best 
    },
    "all":{
    "orders":len (all_orders ),
    "active":len (all_active ),
    "completed":len (all_completed ),
    "refunded":len (all_refunded ),
    "profit":all_profit ,
    "best":all_best 
    }
    }