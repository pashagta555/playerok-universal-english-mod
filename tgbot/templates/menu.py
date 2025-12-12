import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from __init__ import VERSION

from .. import callback_datas as calls


def menu_text():
    txt = textwrap.dedent(f"""
        🏠 <b>Main Menu</b>

        <b>Playerok UNIVERSAL</b> v{VERSION}
        Helper bot for Playerok

        <b>Links:</b>
        ┣ <b>@alleexxeeyy</b> — main and only developer
        ┣ <b>@alexeyproduction</b> — channel where news is published
        ┗ <b>@alexey_production_bot</b> — bot for purchasing official modules

        Navigate through the sections below ↓
    """)
    return txt


def menu_kb():
    rows = [
        [
        InlineKeyboardButton(text="⚙️", callback_data=calls.SettingsNavigation(to="default").pack()), 
        InlineKeyboardButton(text="👤", callback_data=calls.MenuNavigation(to="profile").pack()), 
        InlineKeyboardButton(text="🔌", callback_data=calls.ModulesPagination(page=0).pack()),
        InlineKeyboardButton(text="📊", callback_data=calls.MenuNavigation(to="stats").pack())
        ],
        [InlineKeyboardButton(text="📖 Instruction", callback_data=calls.InstructionNavigation(to="default").pack())], 
        [
        InlineKeyboardButton(text="👨‍💻 Developer", url="https://t.me/alleexxeeyy"), 
        InlineKeyboardButton(text="📢 Our Channel", url="https://t.me/alexeyproduction"), 
        InlineKeyboardButton(text="🤖 Our Bot", url="https://t.me/alexey_production_bot")
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb