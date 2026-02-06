import math
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from plbot.playerokbot import get_playerok_bot

from .. import callback_datas as calls
from ...settings import Settings as sett
from ...meta import NAME, VERSION


def menu_text():
    txt = textwrap.dedent(f"""
        📝 <b>{NAME} menu</b>

        <b>{NAME}</b> v{VERSION}
        Module that allows you to fill out forms

        <b>Links:</b>
        ┣ <b>@alleexxeeyy</b> — main and only developer
        ┗ <b>@alexey_production_bot</b> — bot for purchasing official modules

        Navigate through the sections below ↓
    """)
    return txt

def menu_kb():
    rows = [
        [
            InlineKeyboardButton(text="⚙️", callback_data=calls.FORMS_MenuNavigation(to="settings").pack())
        ],
        [InlineKeyboardButton(text="📖 Instructions", callback_data=calls.FORMS_InstructionNavigation(to="default").pack())],
        [
            InlineKeyboardButton(text="👨‍💻 Developer", url="https://t.me/alleexxeeyy"),
            InlineKeyboardButton(text="🤖 Our bot", url="https://t.me/alexey_production_bot")
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def menu_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        📝 <b>{NAME} menu</b>
        \n{placeholder}
    """)
    return txt


def instruction_text():
    txt = textwrap.dedent(f"""
        📖 <b>{NAME} instructions</b>
        This section describes how to work with the module

        Navigate through the sections below ↓
    """)
    return txt

def instruction_kb():
    rows = [
        [InlineKeyboardButton(text="⌨️ Commands", callback_data=calls.FORMS_InstructionNavigation(to="commands").pack())],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def instruction_comms_text():
    txt = textwrap.dedent(f"""
        📖 <b>{NAME} instructions</b> → ⌨️ <b>Commands</b>

        <code>!myform</code> — shows the data of the filled-out form
        <code>!fill</code> — starts the form filling process

        Choose an action ↓
    """)
    return txt

def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_InstructionNavigation(to="default").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_text():
    txt = textwrap.dedent(f"""
        ⚙️ <b>{NAME} settings</b>

        Navigate through the sections below to change parameter values ↓
    """)
    return txt

def settings_kb():
    config = sett.get("config")
    log_states = "🟢 Enabled" if config["playerok"]["bot"]["log_states"] else "🔴 Disabled"
    rows = [
        [InlineKeyboardButton(text=f"👁️ Log states to console: {log_states}", callback_data="forms_switch_log_states")],
        [InlineKeyboardButton(text=f"💬 Messages", callback_data=calls.FORMS_MessagesPagination(page=0).pack())],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.FORMS_MenuNavigation(to="settings").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>{NAME} settings</b>
        \n{placeholder}
    """)
    return txt


def settings_mess_text():
    messages = sett.get("messages")
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings</b> → ✉️ <b>Messages</b>
        There are <b>{len(messages.keys())}</b> configurable messages in the config

        Navigate through the sections below. Click a message to edit it ↓
    """)
    return txt

def settings_mess_kb(page: int = 0):
    messages = sett.get("messages")
    rows = []
    items_per_page = 8
    total_pages = math.ceil(len(messages.keys()) / items_per_page)
    total_pages = total_pages if total_pages > 0 else 1

    if page < 0: page = 0
    elif page >= total_pages: page = total_pages - 1

    start_offset = page * items_per_page
    end_offset = start_offset + items_per_page

    for mess_id, info in list(messages.items())[start_offset:end_offset]:
        enabled = "🟢" if info["enabled"] else "🔴"
        text_joined = "\n".join(info["text"])
        rows.append([InlineKeyboardButton(text=f"{enabled} {mess_id} | {text_joined}", callback_data=calls.FORMS_MessagePage(message_id=mess_id).pack())])

    buttons_row = []
    btn_back = InlineKeyboardButton(text="←", callback_data=calls.FORMS_MessagesPagination(page=page-1).pack()) if page > 0 else InlineKeyboardButton(text="🛑", callback_data="noop")
    buttons_row.append(btn_back)
    buttons_row.append(InlineKeyboardButton(text=f"{page+1}/{total_pages}", callback_data="forms_enter_messages_page"))

    btn_next = InlineKeyboardButton(text="→", callback_data=calls.FORMS_MessagesPagination(page=page+1).pack()) if page < total_pages - 1 else InlineKeyboardButton(text="🛑", callback_data="noop")
    buttons_row.append(btn_next)
    rows.append(buttons_row)

    rows.append([InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="settings").pack()),
                 InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.FORMS_MessagesPagination(page=page).pack())])
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_mess_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings</b> → ✉️ <b>Messages</b>
        \n{placeholder}
    """)
    return txt


def settings_mess_page_text(message_id: int):
    messages = sett.get("messages")
    enabled = "🟢 Enabled" if messages[message_id]["enabled"] else "🔴 Disabled"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not set"
    txt = textwrap.dedent(f"""
        ✒️ <b>Editing message</b>

        🆔 <b>Message ID:</b> {message_id}
        💡 <b>Status:</b> {enabled}
        💬 <b>Message text:</b> <blockquote>{message_text}</blockquote>

        Choose a parameter to change ↓
    """)
    return txt

def settings_mess_page_kb(message_id: int, page: int = 0):
    messages = sett.get("messages")
    enabled = "🟢 Enabled" if messages[message_id]["enabled"] else "🔴 Disabled"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"💡 Status: {enabled}", callback_data="forms_switch_message_enabled")],
        [InlineKeyboardButton(text=f"💬 Message text: {message_text}", callback_data="forms_enter_message_text")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MessagesPagination(page=page).pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.FORMS_MessagePage(message_id=message_id).pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_mess_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ✒️ <b>Editing message</b>
        \n{placeholder}
    """)
    return txt