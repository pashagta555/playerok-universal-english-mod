import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_conn_text():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>

        <b>🌐 Proxy:</b> {proxy}
        <b>🛜 playerok.com request timeout:</b> {requests_timeout}

        <b>What is request timeout?</b>
        Maximum time to wait for a response from Playerok. If it expires, the bot will report an error. Use a higher value on slow connections.
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy: {proxy}", callback_data="enter_proxy")],
        [InlineKeyboardButton(text=f"🛜 playerok.com timeout: {requests_timeout}", callback_data="enter_requests_timeout")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    if config["playerok"]["api"]["proxy"]: rows[0].append(InlineKeyboardButton(text=f"❌🌐 Remove proxy", callback_data="clean_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>
        \n{placeholder}
    """)
    return txt