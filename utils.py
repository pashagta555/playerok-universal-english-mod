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
from playerokapi.exceptions import BotCheckDetectedException
from settings import Settings as sett
from data import Data as data
logger = getLogger('universal')

def is_cookies_valid(cookie_str: str) -> bool:
    if not cookie_str or '=' not in cookie_str:
        return False
    parts = cookie_str.split(';')
    for part in parts:
        part = part.strip()
        if '=' not in part:
            return False
        key, value = part.split('=', 1)
        if not key or not value:
            return False
    return True

def is_token_valid(token: str) -> bool:
    if not re.match('^[A-Za-z0-9_-]+\\.[A-Za-z0-9_-]+\\.[A-Za-z0-9_-]+$', token):
        return False
    try:
        header, payload, signature = token.split('.')
        for part in (header, payload, signature):
            padding = '=' * (-len(part) % 4)
            base64.urlsafe_b64decode(part + padding)
        return True
    except Exception:
        return False

def is_pl_account_working() -> tuple[bool, str]:
    try:
        config = sett.get('config')
        Account(cookies=config['playerok']['api']['cookies'], user_agent=config['playerok']['api']['user_agent'], requests_timeout=config['playerok']['api']['requests_timeout'], proxy=config['playerok']['api']['proxy'] or None).get()
        return (True, '')
    except BotCheckDetectedException:
        return (False, 'Bot-проверка заметила подозрительную активность при подключении к аккаунту Playerok. Чтобы продолжить работу, вам нужно указать актуальные Cookies вашего авторизованного Playerok аккаунта.')
    except:
        return (False, '')

def is_pl_account_banned() -> bool:
    try:
        config = sett.get('config')
        acc = Account(cookies=config['playerok']['api']['cookies'], user_agent=config['playerok']['api']['user_agent'], requests_timeout=config['playerok']['api']['requests_timeout'], proxy=config['playerok']['api']['proxy'] or None).get()
        return acc.profile.is_blocked
    except:
        return False

def is_user_agent_valid(ua: str) -> bool:
    if not ua or not 10 <= len(ua) <= 512:
        return False
    allowed_chars = string.ascii_letters + string.digits + string.punctuation + ' '
    return all((c in allowed_chars for c in ua))

def is_proxy_valid(proxy: str) -> bool:
    ip_pattern = '(?:25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)'
    pattern_ip_port = re.compile(f'^{ip_pattern}\\.{ip_pattern}\\.{ip_pattern}\\.{ip_pattern}:(\\d+)$')
    pattern_auth_ip_port = re.compile(f'^[^:@]+:[^:@]+@{ip_pattern}\\.{ip_pattern}\\.{ip_pattern}\\.{ip_pattern}:(\\d+)$')
    match = pattern_ip_port.match(proxy)
    if match:
        port = int(match.group(1))
        return 1 <= port <= 65535
    match = pattern_auth_ip_port.match(proxy)
    if match:
        port = int(match.group(1))
        return 1 <= port <= 65535
    return False

def is_proxy_working(proxy: str, test_url='https://playerok.com', timeout=10) -> bool:
    proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    try:
        response = requests.get(test_url, proxies=proxies, timeout=timeout)
        return response.status_code < 404
    except Exception:
        return False

def is_tg_token_valid(token: str) -> bool:
    pattern = '^\\d{7,12}:[A-Za-z0-9_-]{35}$'
    return bool(re.match(pattern, token))

def is_tg_bot_exists() -> bool:
    try:
        config = sett.get('config')
        token = config['telegram']['api']['token']
        proxy = config['telegram']['api']['proxy']
        if proxy:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
        else:
            proxies = None
        response = requests.get(f'https://api.telegram.org/bot{token}/getMe', proxies=proxies, timeout=5)
        data = response.json()
        return data.get('ok', False) is True and data.get('result', {}).get('is_bot', False) is True
    except Exception:
        return False

def is_password_valid(password: str) -> bool:
    if len(password) < 6 or len(password) > 64:
        return False
    common_passwords = {'123456', '1234567', '12345678', '123456789', 'password', 'qwerty', 'admin', '123123', '111111', 'abc123', 'letmein', 'welcome', 'monkey', 'login', 'root', 'pass', 'test', '000000', 'user', 'qwerty123', 'iloveyou'}
    if password.lower() in common_passwords:
        return False
    return True

def configure_config():
    config = sett.get('config')
    while not config['playerok']['api']['cookies']:
        while not config['playerok']['api']['cookies']:
            print(f'\n{Fore.WHITE}Enter {Fore.YELLOW}Cookie-Данные {Fore.WHITE}your {Fore.LIGHTWHITE_EX}authorized {Fore.WHITE}Playerok аккаунта в формате Header String. \nАвторизуйтесь в свой аккаунт на сайте, а после скопируйте куки с помощью расширения Cookie-Editor (ЛКМ на расширение -> Export -> Header String).\n  {Fore.WHITE}· Пример: __ddg3=4L7yBmrBwMwKm15X;token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...')
            str_cookies = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
            cookies = {c.split('=')[0].strip(): c.split('=')[1].strip() for c in str_cookies.split(';') if c.strip() and '=' in c}
            if is_cookies_valid(str_cookies) and is_token_valid(cookies['token']):
                config['playerok']['api']['cookies'] = str_cookies
                sett.set('config', config)
                print(f'\n{Fore.GREEN}Cookies успешно сохранены в конфиг.')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Похоже, что вы ввели некорректные Cookies. Убедитесь, что они соответствует формату и попробуйте ещё раз.')
        while not config['playerok']['api']['user_agent']:
            print(f'\n{Fore.WHITE}Enter {Fore.LIGHTMAGENTA_EX}User Agent {Fore.WHITE}вашего браузера. Его можно скопировать on сайте {Fore.LIGHTWHITE_EX}https://whatmyuseragent.com.\n  {Fore.WHITE}· Пример: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36')
            user_agent = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
            if is_user_agent_valid(user_agent):
                config['playerok']['api']['user_agent'] = user_agent
                sett.set('config', config)
                print(f'\n{Fore.GREEN}User Agent successfully saved to config.')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Похоже, что вы ввели некорректный User Agent. Убедитесь, что в нём нет русских символов и попробуйте ещё раз.')
        while not config['playerok']['api']['proxy']:
            print(f'\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy {Fore.WHITE}для Playerok аккаунта. Формат: user:password@ip:port или ip:port, если он без авторизации. Если вы не знаете что это, или не хотите устанавливать прокси - пропустите этот параметр, нажав Enter.\n  {Fore.WHITE}· Пример: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000')
            proxy = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
            if not proxy:
                print(f'\n{Fore.WHITE}You missed entering a proxy.')
                break
            if is_proxy_valid(proxy):
                config['playerok']['api']['proxy'] = proxy
                sett.set('config', config)
                print(f'\n{Fore.GREEN}Proxy successfully saved to config.')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Похоже, что вы ввели некорректный Proxy. Убедитесь, что он соответствует формату и попробуйте ещё раз.')
    while not config['telegram']['api']['token']:
        while not config['telegram']['api']['token']:
            print(f'\n{Fore.WHITE}Enter {Fore.CYAN}token of your Telegram bot{Fore.WHITE}. Бота нужно создать у @BotFather.\n  {Fore.WHITE}· Пример: 7257913369:AAG2KjLL3-zvvfSQFSVhaTb4w7tR2iXsJXM')
            token = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
            if is_tg_token_valid(token):
                config['telegram']['api']['token'] = token
                sett.set('config', config)
                print(f'\n{Fore.GREEN}Telegram bot token successfully saved to config.')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Похоже, что вы ввели некорректный токен. Убедитесь, что он соответствует формату и попробуйте ещё раз.')
        while not config['telegram']['api']['proxy']:
            print(f'\n{Fore.WHITE}Enter {Fore.LIGHTBLUE_EX}IPv4 HTTP Proxy {Fore.WHITE}для Telegram бота. Формат: user:password@ip:port или ip:port, если он без авторизации. Если вы не знаете что это, или не хотите устанавливать прокси - пропустите этот параметр, нажав Enter.\n  {Fore.WHITE}· Пример: DRjcQTm3Yc:m8GnUN8Q9L@46.161.30.187:8000')
            proxy = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
            if not proxy:
                print(f'\n{Fore.WHITE}You missed entering a proxy.')
                break
            if is_proxy_valid(proxy):
                config['telegram']['api']['proxy'] = proxy
                sett.set('config', config)
                print(f'\n{Fore.GREEN}Proxy successfully saved to config.')
            else:
                print(f'\n{Fore.LIGHTRED_EX}Похоже, что вы ввели некорректный прокси. Убедитесь, что он соответствует формату и попробуйте ещё раз.')
    while not config['telegram']['bot']['password']:
        print(f'\n{Fore.WHITE}Think and enter {Fore.YELLOW}password for your Telegram bot{Fore.WHITE}. The bot will request this password every time another user tries to interact with your Telegram bot.\n  {Fore.WHITE}· Password должен быть сложным, длиной не менее 6 и не более 64 символов.')
        password = input(f'  {Fore.WHITE}↳ {Fore.LIGHTWHITE_EX}').strip()
        if is_password_valid(password):
            config['telegram']['bot']['password'] = password
            sett.set('config', config)
            print(f'\n{Fore.GREEN}The password was successfully saved to the config.')
        else:
            print(f'\n{Fore.LIGHTRED_EX}Ваш пароль не подходит. Убедитесь, что он соответствует формату и не является лёгким и попробуйте ещё раз.')
    if config['playerok']['api']['proxy'] and (not is_proxy_working(config['playerok']['api']['proxy'])):
        print(f'\n{Fore.LIGHTRED_EX}Похоже, что прокси для Playerok аккаунта не работает. Пожалуйста, проверьте его и введите снова.')
        config['playerok']['api']['cookies'] = ''
        config['playerok']['api']['user_agent'] = ''
        config['playerok']['api']['proxy'] = ''
        sett.set('config', config)
        return configure_config()
    elif config['playerok']['api']['proxy']:
        logger.info(f'{Fore.LIGHTYELLOW_EX}Playerok proxy works successfully.')
    is_pl_acc_working, reason = is_pl_account_working()
    if not is_pl_acc_working:
        reason = reason if reason else 'Не удалось подключиться к вашему Playerok аккаунту. Пожалуйста, убедитесь, что у вас указан верный токен и введите его снова.'
        print(f'\n{Fore.LIGHTRED_EX}{reason}')
        config['playerok']['api']['cookies'] = ''
        config['playerok']['api']['user_agent'] = ''
        config['playerok']['api']['proxy'] = ''
        sett.set('config', config)
        return configure_config()
    else:
        logger.info(f'{Fore.LIGHTYELLOW_EX}Playerok account has been successfully authorized.')
    if is_pl_account_banned():
        print(f'{Fore.LIGHTRED_EX}\nВаш Playerok аккаунт забанен! Увы, я не могу запустить бота on заблокированном аккаунте...')
        config['playerok']['api']['cookies'] = ''
        config['playerok']['api']['user_agent'] = ''
        config['playerok']['api']['proxy'] = ''
        sett.set('config', config)
        return configure_config()
    if config['telegram']['api']['proxy'] and (not is_proxy_working(config['telegram']['api']['proxy'], 'https://api.telegram.org/')):
        print(f'{Fore.LIGHTRED_EX}\nПохоже, что прокси для Telegram бота не работает. Пожалуйста, проверьте его и введите снова.')
        config['telegram']['api']['token'] = ''
        config['telegram']['api']['proxy'] = ''
        sett.set('config', config)
        return configure_config()
    elif config['telegram']['api']['proxy']:
        logger.info(f'{Fore.LIGHTYELLOW_EX}Telegram proxy works successfully.')
    if not is_tg_bot_exists():
        print(f'{Fore.LIGHTRED_EX}\nНе удалось подключиться к вашему Telegram боту. Если вы находитесь on территории России, вам нужно подключить прокси к Telegram боту или использовать VPN, в виду блокировок со стороны РКН.')
        config['telegram']['api']['token'] = ''
        config['telegram']['api']['proxy'] = ''
        sett.set('config', config)
        return configure_config()
    else:
        logger.info(f'{Fore.LIGHTYELLOW_EX}Telegram bot is working successfully.')

def get_stats():
    cached_orders = data.get('cached_orders')
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    day_ago = now - timedelta(days=1)
    week_ago = now - timedelta(days=7)
    month_ago = now - timedelta(days=30)
    day_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o['date']) >= day_ago]
    week_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o['date']) >= week_ago]
    month_orders = [o for o in cached_orders.values() if datetime.fromisoformat(o['date']) >= month_ago]
    all_orders = list(cached_orders.values())
    day_active = [o for o in day_orders if not o['status'].startswith('CONFIRMED') and (not o['status'].startswith('ROLLED_BACK'))]
    week_active = [o for o in week_orders if not o['status'].startswith('CONFIRMED') and (not o['status'].startswith('ROLLED_BACK'))]
    month_active = [o for o in month_orders if not o['status'].startswith('CONFIRMED') and (not o['status'].startswith('ROLLED_BACK'))]
    all_active = [o for o in all_orders if not o['status'].startswith('CONFIRMED') and (not o['status'].startswith('ROLLED_BACK'))]
    day_completed = [o for o in day_orders if o['status'].startswith('CONFIRMED')]
    week_completed = [o for o in week_orders if o['status'].startswith('CONFIRMED')]
    month_completed = [o for o in month_orders if o['status'].startswith('CONFIRMED')]
    all_completed = [o for o in all_orders if o['status'].startswith('CONFIRMED')]
    day_refunded = [o for o in day_orders if o['status'].startswith('ROLLED_BACK')]
    week_refunded = [o for o in week_orders if o['status'].startswith('ROLLED_BACK')]
    month_refunded = [o for o in month_orders if o['status'].startswith('ROLLED_BACK')]
    all_refunded = [o for o in all_orders if o['status'].startswith('ROLLED_BACK')]
    day_profit = round(sum((o['price'] for o in day_orders if o['status'].startswith('CONFIRMED'))), 2)
    week_profit = round(sum((o['price'] for o in week_orders if o['status'].startswith('CONFIRMED'))), 2)
    month_profit = round(sum((o['price'] for o in month_orders if o['status'].startswith('CONFIRMED'))), 2)
    all_profit = round(sum((o['price'] for o in all_orders if o['status'].startswith('CONFIRMED'))), 2)
    day_best = Counter((o['item_name'] for o in day_orders)).most_common(1)[0][0] if day_orders else '-'
    week_best = Counter((o['item_name'] for o in week_orders)).most_common(1)[0][0] if day_orders else '-'
    month_best = Counter((o['item_name'] for o in month_orders)).most_common(1)[0][0] if day_orders else '-'
    all_best = Counter((o['item_name'] for o in all_orders)).most_common(1)[0][0] if day_orders else '-'
    return {'day': {'orders': len(day_orders), 'active': len(day_active), 'completed': len(day_completed), 'refunded': len(day_refunded), 'profit': day_profit, 'best': day_best}, 'week': {'orders': len(week_orders), 'active': len(week_active), 'completed': len(week_completed), 'refunded': len(week_refunded), 'profit': week_profit, 'best': week_best}, 'month': {'orders': len(month_orders), 'active': len(month_active), 'completed': len(month_completed), 'refunded': len(month_refunded), 'profit': month_profit, 'best': month_best}, 'all': {'orders': len(all_orders), 'active': len(all_active), 'completed': len(all_completed), 'refunded': len(all_refunded), 'profit': all_profit, 'best': all_best}}