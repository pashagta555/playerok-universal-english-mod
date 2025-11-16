import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_conn_text():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not specified"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not specified"
    listener_requests_delay = config["playerok"]["api"]["listener_requests_delay"] or "❌ Not specified"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 📶 Connection</b>

        🌐 <b>Proxy:</b> {proxy}
        🛜 <b>Connection timeout to playerok.com:</b> {requests_timeout}
        ⏱️ <b>Requests frequirency to playerok.com:</b> {listener_requests_delay}

        Select parametre to be changed  ↓
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not specified"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not specified"
    listener_requests_delay = config["playerok"]["api"]["listener_requests_delay"] or "❌ Not specified"
    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy: {proxy}", callback_data="enter_proxy")],
        [InlineKeyboardButton(text=f"🛜 Connection timeout playerok.com: {requests_timeout}", callback_data="enter_requests_timeout")],
        [InlineKeyboardButton(text=f"⏱️ Reqests frequierency to playerok.com: {listener_requests_delay}", callback_data="enter_listener_requests_delay")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.SettingsNavigation(to="conn").pack())
        ]
    ]
    if config["playerok"]["api"]["proxy"]: rows[0].append(InlineKeyboardButton(text=f"❌🌐 Убрать прокси", callback_data="clean_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 📶 Connection</b>
        \n{placeholder}
    """)
    return txt
