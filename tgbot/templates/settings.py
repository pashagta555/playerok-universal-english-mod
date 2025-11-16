import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_text():
    config = sett.get("config")
    token = config["playerok"]["api"]["token"][:5] + ("*" * 10) or "❌ Не задано"
    user_agent = config["playerok"]["api"]["user_agent"] or "❌ Не задано"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings</b>

        <b>Main settings:</b>
        ┣ Token: <b>{token}</b>
        ┗ User-Agent: <b>{user_agent}</b>

        Navigate through the sections below to change the parameter values ↓
    """)
    return txt


def settings_kb():
    rows = [
        [
        InlineKeyboardButton(text="🔑 Autorisation", callback_data=calls.SettingsNavigation(to="auth").pack()),
        InlineKeyboardButton(text="📶 Connection", callback_data=calls.SettingsNavigation(to="conn").pack()),
        InlineKeyboardButton(text="♻️ Recovery", callback_data=calls.SettingsNavigation(to="restore").pack())
        ],
        [
        InlineKeyboardButton(text="✉️ Messages", callback_data=calls.MessagesPagination(page=0).pack()),
        InlineKeyboardButton(text="⌨️ Commands", callback_data=calls.CustomCommandsPagination(page=0).pack()),
        InlineKeyboardButton(text="🚀 Auto delivery", callback_data=calls.AutoDeliveriesPagination(page=0).pack())
        ],
        [
        InlineKeyboardButton(text="👀 Logs", callback_data=calls.SettingsNavigation(to="logger").pack()),
        InlineKeyboardButton(text="🔧 Other", callback_data=calls.SettingsNavigation(to="other").pack())
        ],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.SettingsNavigation(to="default").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb
