import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_comm_page_text(command: str):
    custom_commands = sett.get("custom_commands")
    command_text = "\n".join(custom_commands[command]) or "❌ Not set"
    txt = textwrap.dedent(f"""
        ✏️ <b>Editing Custom Command</b>

        ⌨️ <b>Command:</b> {command}
        💬 <b>Response:</b> 
        <blockquote>{command_text}</blockquote>

        Select a parameter to change ↓
    """)
    return txt


def settings_comm_page_kb(command: str, page: int = 0):
    custom_commands = sett.get("custom_commands")
    command_text = "\n".join(custom_commands[command]) or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"✍️ Response: {command_text}", callback_data="enter_custom_command_answer")],
        [InlineKeyboardButton(text="🗑️ Delete Command", callback_data="confirm_deleting_custom_command")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.CustomCommandsPagination(page=page).pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.CustomCommandPage(command=command).pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_comm_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ✏️ <b>Editing Custom Command</b>
        \n{placeholder}
    """)
    return txt