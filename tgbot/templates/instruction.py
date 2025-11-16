import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .. import callback_datas as calls
                
        
def instruction_text():
    txt = textwrap.dedent(f"""
        📖 <b>Instruction</b>
        This section describes instructions for working with the bot

        Navigate through the sections below ↓
    """)
    return txt


def instruction_kb():
    rows = [
        [InlineKeyboardButton(text="⌨️ Команды", callback_data=calls.InstructionNavigation(to="commands").pack())],
        [InlineKeyboardButton(text="⬅️ Назад", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def instruction_comms_text():
    txt = textwrap.dedent(f"""
        📖 <b>Instruction → ⌨️ Commands</b>
                          
       Buyer commands:
        ┣ <code>!commands</code> — Displays a menu with commands available to the buyer
        ┗ <code>!seller</code> — Notifies and calls the seller into a dialogue with the buyer (writes you a message in Telegram with a request for help)

        Выберите действие ↓
    """)
    return txt


def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=calls.InstructionNavigation(to="default").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb
