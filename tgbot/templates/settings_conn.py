import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_conn_text():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    listener_requests_delay = config["playerok"]["api"]["listener_requests_delay"] or "❌ Not set"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 📶 Connection</b>

        🌐 <b>Proxy:</b> {proxy}
        🛜 <b>Connection timeout to playerok.com:</b> {requests_timeout}
        ⏱️ <b>Request frequency to playerok.com:</b> {listener_requests_delay}

        <b>What is connection timeout to playerok.com?</b>
        This is the maximum time for a response to come from the Playerok site. If the time expires and no response came — the bot will show an error. If you have slow internet, specify a larger value

        <b>What is request frequency to playerok.com?</b>
        How often requests will be sent to Playerok to get events. We don't recommend setting it below 4 seconds, as Playerok may simply ban your IP address, and you won't be able to send requests from it anymore

        Select parameter to change ↓
    """)
    return txt


def settings_conn_kb():
    config = sett.get("config")
    proxy = config["playerok"]["api"]["proxy"] or "❌ Not set"
    requests_timeout = config["playerok"]["api"]["requests_timeout"] or "❌ Not set"
    listener_requests_delay = config["playerok"]["api"]["listener_requests_delay"] or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"🌐 Proxy: {proxy}", callback_data="enter_proxy")],
        [InlineKeyboardButton(text=f"🛜 Connection timeout to playerok.com: {requests_timeout}", callback_data="enter_requests_timeout")],
        [InlineKeyboardButton(text=f"⏱️ Request frequency to playerok.com: {listener_requests_delay}", callback_data="enter_listener_requests_delay")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.SettingsNavigation(to="conn").pack())
        ]
    ]
    if config["playerok"]["api"]["proxy"]: rows[0].append(InlineKeyboardButton(text=f"❌🌐 Remove proxy", callback_data="clean_proxy"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 📶 Connection</b>
        \n{placeholder}
    """)
    return txt
