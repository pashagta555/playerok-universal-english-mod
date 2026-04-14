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
                          
        ・ <code>!teams</code> — displays menu With accessible For buyer teams
        ・ <code>!seller</code> — notifies And causes seller V dialogue With buyer (writes to you V Telegram message With request O help)
    """)
    return txt


def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=calls.InstructionNavigation(to="default").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb