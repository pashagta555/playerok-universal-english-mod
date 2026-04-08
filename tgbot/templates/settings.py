import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as set

from .. import callback_datas as calls


def settings_text():
    txt = textwrap.dedent(f"""
        <b>⚙️Settings</b>
                          
        Select subsection:
    """)
    return txt


def settings_kb():
    rows = [
        [
        InlineKeyboardButton(text='🔑 Authorization', callback_data=calls.SettingsNavigation(to="auth").pack()),
        InlineKeyboardButton(text='📶 Connection', callback_data=calls.SettingsNavigation(to="conn").pack())
        ],
        [
        InlineKeyboardButton(text='💬 Messages', callback_data=calls.MessagesPagination(page=0).pack()),
        InlineKeyboardButton(text='❗ Teams', callback_data=calls.CustomCommandsPagination(page=0).pack())
        ],
        [
        InlineKeyboardButton(text='🚀 Auto-issue', callback_data=calls.AutoDeliveriesPagination(page=0).pack()),
        InlineKeyboardButton(text='♻️ Auto-recovery', callback_data=calls.SettingsNavigation(to="restore").pack())
        ],
        [
        InlineKeyboardButton(text='☑️ Auto-confirmation', callback_data=calls.SettingsNavigation(to="complete").pack()),
        InlineKeyboardButton(text='💸 Auto-withdrawal', callback_data=calls.SettingsNavigation(to="withdrawal").pack())
        ],
        [
        InlineKeyboardButton(text='⬆️ Auto-raising', callback_data=calls.SettingsNavigation(to="bump").pack()),
        InlineKeyboardButton(text='👀 Logger', callback_data=calls.SettingsNavigation(to="logger").pack())
        ],
        [InlineKeyboardButton(text='🔧 Other', callback_data=calls.SettingsNavigation(to="other").pack())],
        [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb