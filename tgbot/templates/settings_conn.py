import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_conn_text():
    config = sett.get("config")
    
    pl_proxy = config["playerok"]["api"]["proxy"] or "❌ Not given"
    tg_proxy = config["telegram"]["api"]["proxy"] or "❌ Not given"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not given"
    
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>

        <b>🌐 Proxy for Playerok:</b> {pl_proxy}
        <b>🌐 Proxy for Telegram:</b> {tg_proxy}

        <b>🛜 Request timeout for playerok.com:</b> {requests_timeout}

        <b>What is request timeout for playerok.com?</b>
        This is the maximum wait time for a response from Playerok.
        If the timeout is reached, the request fails. Use a higher value on slow networks.
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    
    pl_proxy = config["playerok"]["api"]["proxy"] or "❌ Not given"
    tg_proxy = config["telegram"]["api"]["proxy"] or "❌ Not given"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not given"

    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy for Playerok: {pl_proxy}", callback_data="enter_pl_proxy")],
        [InlineKeyboardButton(text=f"🌐 Proxy for Telegram: {tg_proxy}", callback_data="enter_tg_proxy")],
        [InlineKeyboardButton(text=f"🛜 Request timeout for playerok.com: {requests_timeout}", callback_data="enter_playerokapi_requests_timeout")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    if config["playerok"]["api"]["proxy"]: 
        rows[0].append(InlineKeyboardButton(text="❌ Clear proxy", callback_data="clean_pl_proxy"))
    if config["telegram"]["api"]["proxy"]: 
        rows[1].append(InlineKeyboardButton(text="❌ Clear proxy", callback_data="clean_tg_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>
        \n{placeholder}
    """)
    return txt