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

        <b>🌐 Proxy For Playerok:</b> {pl_proxy}
        <b>🌐 Proxy For Telegram:</b> {tg_proxy}

        <b>🛜 Time-out connections To playerok.com:</b> {requests_timeout}

        <b>What for time-out connections To playerok.com?</b>
        This maximum time, for which must come answer on request With site Playerok. If time expired, A answer Not came — bot will give out error. If at you weak Internet, indicate meaning more
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    
    pl_proxy = config["playerok"]["api"]["proxy"] or "❌ Not given"
    tg_proxy = config["telegram"]["api"]["proxy"] or "❌ Not given"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not given"

    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy For Playerok: {pl_proxy}", callback_data="enter_pl_proxy")],
        [InlineKeyboardButton(text=f"🌐 Proxy For Telegram: {tg_proxy}", callback_data="enter_tg_proxy")],
        [InlineKeyboardButton(text=f"🛜 Time-out connections To playerok.com: {requests_timeout}", callback_data="enter_playerokapi_requests_timeout")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    if config["playerok"]["api"]["proxy"]: 
        rows[0].append(InlineKeyboardButton(text=f"❌ Put away proxy", callback_data="clean_pl_proxy"))
    if config["telegram"]["api"]["proxy"]: 
        rows[1].append(InlineKeyboardButton(text=f"❌ Put away proxy", callback_data="clean_tg_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>
        \n{placeholder}
    """)
    return txt