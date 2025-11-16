import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_mess_page_text(message_id: int):
    messages = sett.get("messages")
    enabled = "🟢 Turned on" if messages[message_id]["enabled"] else "🔴 Turned off"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not specified"
    txt = textwrap.dedent(f"""
        ✒️ <b>Edit message</b>

        🆔 <b>ID of the message:</b> {message_id}
        💡 <b>Status:</b> {enabled}
        💬 <b>Message text:</b> <blockquote>{message_text}</blockquote>

        Select parametre to be changed ↓
    """)
    return txt


def settings_mess_page_kb(message_id: int, page: int = 0):
    messages = sett.get("messages")
    enabled = "🟢 Turned on" if messages[message_id]["enabled"] else "🔴 Turned off"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not specified"
    rows = [
        [InlineKeyboardButton(text=f"💡 Status: {enabled}", callback_data="switch_message_enabled")],
        [InlineKeyboardButton(text=f"💬 Message text: {message_text}", callback_data="enter_message_text")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MessagesPagination(page=page).pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.MessagePage(message_id=message_id).pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_mess_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ✒️ <b>Edit message</b>
        \n{placeholder}
    """)
    return txt
