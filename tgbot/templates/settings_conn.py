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
        <b>🛜 Connection timeout to playerok.com:</b> {requests_timeout}

        <b>What is the connection timeout to playerok.com?</b>
        This is the maximum time in which a response from Playerok must arrive. If the time is up and there is no response, the bot will raise an error. If your internet connection is weak, set a larger value.
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy: {proxy}", callback_data="enter_proxy")],
        [InlineKeyboardButton(text=f"🛜 Connection timeout to playerok.com: {requests_timeout}", callback_data="enter_requests_timeout")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    if config["playerok"]["api"]["proxy"]:
        rows[0].append(InlineKeyboardButton(text=f"❌🌐 Remove proxy", callback_data="clean_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>📶 Connection</b>
        \n{placeholder}
    """)
    return txt