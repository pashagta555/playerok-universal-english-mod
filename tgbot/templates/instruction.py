import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .. import callback_datas as calls
                
        
def instruction_text():
    txt = textwrap.dedent(f"""
        <b>📖 Instructions</b>
    """)
    return txt


def instruction_kb():
    rows = [
        [InlineKeyboardButton(text="⌨️ Commands", callback_data=calls.InstructionNavigation(to="commands").pack())],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def instruction_comms_text():
    txt = textwrap.dedent(f"""
        <b>⌨️ Commands</b>
                          
        ・ <code>!commands</code> — shows the menu with commands available to the buyer
        ・ <code>!seller</code> — notifies and calls the seller into the dialog with the buyer (sends you a Telegram message asking for help)
    """)
    return txt


def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=calls.InstructionNavigation(to="default").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb