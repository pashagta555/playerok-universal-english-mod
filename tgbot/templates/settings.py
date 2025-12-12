import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_text():
    config = sett.get("config")
    token = config["playerok"]["api"]["token"][:5] + ("*" * 10) or "❌ Not set"
    user_agent = config["playerok"]["api"]["user_agent"] or "❌ Not set"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings</b>

        <b>Main settings:</b>
        ┣ Token: <b>{token}</b>
        ┗ User-Agent: <b>{user_agent}</b>

        Navigate through the sections below to change parameter values ↓
    """)
    return txt


def settings_kb():
    rows = [
        [
        InlineKeyboardButton(text="🔑 Authorization", callback_data=calls.SettingsNavigation(to="auth").pack()),
        InlineKeyboardButton(text="📶 Connection", callback_data=calls.SettingsNavigation(to="conn").pack()),
        InlineKeyboardButton(text="♻️ Restore", callback_data=calls.SettingsNavigation(to="restore").pack())
        ],
        [
        InlineKeyboardButton(text="✉️ Messages", callback_data=calls.MessagesPagination(page=0).pack()),
        InlineKeyboardButton(text="⌨️ Commands", callback_data=calls.CustomCommandsPagination(page=0).pack()),
        InlineKeyboardButton(text="🚀 Auto-Delivery", callback_data=calls.AutoDeliveriesPagination(page=0).pack())
        ],
        [
        InlineKeyboardButton(text="👀 Logger", callback_data=calls.SettingsNavigation(to="logger").pack()),
        InlineKeyboardButton(text="🔧 Other", callback_data=calls.SettingsNavigation(to="other").pack())
        ],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.SettingsNavigation(to="default").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb