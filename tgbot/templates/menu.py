import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from __init__ import VERSION

from .. import callback_datas as calls


def menu_text():
    txt = textwrap.dedent(f"""
        <b>🏠 Main menu</b>

        <b>Playerok Universal</b> v{VERSION}
        Assistant bot for Playerok

        <b>🔗 Links:</b>
        ・ <b>@alleexxeeyy</b> — developer
        ・ <b>@alexeyproduction</b> — news channel
        ・ <b>@alexey_production_bot</b> — bot for purchasing plugins
    """)
    return txt


def menu_kb():
    rows = [
        [
        InlineKeyboardButton(text="⚙️", callback_data=calls.SettingsNavigation(to="default").pack()), 
        InlineKeyboardButton(text="👤", callback_data=calls.MenuNavigation(to="profile").pack()), 
        InlineKeyboardButton(text="🚩", callback_data=calls.MenuNavigation(to="events").pack()),
        InlineKeyboardButton(text="🗒️", callback_data=calls.MenuNavigation(to="logs").pack()),
        InlineKeyboardButton(text="📊", callback_data=calls.MenuNavigation(to="stats").pack()),
        InlineKeyboardButton(text="🔌", callback_data=calls.ModulesPagination(page=0).pack())
        ],
        [InlineKeyboardButton(text="📖 Instructions", callback_data=calls.InstructionNavigation(to="default").pack())], 
        [
        InlineKeyboardButton(text="👨‍💻 Developer", url="https://t.me/alleexxeeyy"), 
        InlineKeyboardButton(text="📢 Our channel", url="https://t.me/alexeyproduction"), 
        InlineKeyboardButton(text="🤖 Our bot", url="https://t.me/alexey_production_bot")
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb