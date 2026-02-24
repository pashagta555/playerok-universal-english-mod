import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_auth_text():
    config = sett.get("config")
    token = config["playerok"]["api"]["token"][:5] + ("*" * 10) or "❌ Not set"
    user_agent = config["playerok"]["api"]["user_agent"] or "❌ Not set"
    txt = textwrap.dedent(f"""
        <b>🔑 Authorization</b>

        <b>🔐 Token:</b> {token}
        <b>🎩 User Agent:</b> {user_agent}
    """)
    return txt


def settings_auth_kb():
    config = sett.get("config")
    token = config["playerok"]["api"]["token"][:5] + ("*" * 10) or "❌ Not set"
    user_agent = config["playerok"]["api"]["user_agent"] or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"🔐 Token: {token}", callback_data="enter_token")],
        [InlineKeyboardButton(text=f"🎩 User Agent: {user_agent}", callback_data="enter_user_agent")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_auth_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>🔑 Authorization</b>
        \n{placeholder}
    """)
    return txt