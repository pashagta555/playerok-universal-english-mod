Here is the translation of the text to English, keeping the code unchanged:

```
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from __init__ import VERSION

from .. import callback_datas as calls


def menu_text():
    txt = textwrap.dedent(f"""
        <b>🏠 Main Menu</b>

        <b>Playerok Universal</b> v{VERSION}
        A bot assistant for Playerok

        <b>🔗 Links:</b>
        ・ <b>@alleexxeeyy</b> — developer
        ・ <b>@alexeyproduction</b> — channel with news
        ・ <b>@alexey_production_bot</b> — bot for purchasing plugins
    """)
    return txt


def menu_kb():
    rows = [
        [
        InlineKeyboardButton(text="⚙️ Settings", callback_data=calls.SettingsNavigation(to="default").pack()), 
        InlineKeyboardButton(text="👤 Profile", callback_data=calls.MenuNavigation(to="profile").pack())
        ],
        [
        InlineKeyboardButton(text="🚩 Events", callback_data=calls.MenuNavigation(to="events").pack()),
        InlineKeyboardButton(text="🗒️ Logs", callback_data=calls.MenuNavigation(to="logs").pack())
        ],
        [
        InlineKeyboardButton(text="📊 Statistics", callback_data=calls.MenuNavigation(to="stats").pack()),
        InlineKeyboardButton(text="🔌 Modules", callback_data=calls.ModulesPagination(page=0).pack())
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
```

Note that I translated the text, but left the code unchanged. If you need any modifications to the code itself, please let me know!

