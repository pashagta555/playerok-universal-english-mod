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
        📝 <b>Menu{NAME}</b>

        <b>{NAME}</b> v{VERSION}
        A module that allows you to fill out questionnaires

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
        📝 <b>Menu{NAME}</b>
        \n{placeholder}
    """)
    return txt


def instruction_text():
    txt = textwrap.dedent(f"""
        📖 <b>Instructions{NAME}</b>
        This section describes instructions for working with the module

        Navigate through the sections below ↓
    """)
    return txt

def instruction_kb():
    rows = [
        [InlineKeyboardButton(text="⌨️ Teams", callback_data=calls.FORMS_InstructionNavigation(to="commands").pack())],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def instruction_comms_text():
    txt = textwrap.dedent(f"""
        📖 <b>Instructions{NAME}</b> → ⌨️ <b>Teams</b>

        <code>!myquestionnaire</code> - displays the data of the completed questionnaire
        <code>!fill</code>—starts the process of filling out the form

        Select action ↓
    """)
    return txt

def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_InstructionNavigation(to="default").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_text():
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings{NAME}</b>

        Navigate through the sections below to change parameter values ​​↓
    """)
    return txt

def settings_kb():
    config = sett.get("config")
    log_states = "🟢 Enabled" if config["playerok"]["bot"]["log_states"] else "🔴 Off"
    rows = [
        [InlineKeyboardButton(text=f"👁️ Log states to the console:{log_states}", callback_data="forms_switch_log_states")],
        [InlineKeyboardButton(text=f"💬 Messages", callback_data=calls.FORMS_MessagesPagination(page=0).pack())],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.FORMS_MenuNavigation(to="settings").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings{NAME}</b>
        \n{placeholder}
    """)
    return txt


def settings_mess_text():
    messages = sett.get("messages")
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings</b> → ✉️ <b>Messages</b>
        Total<b>{len(messages.keys())}</b> custom messages in the config

        Navigate through the sections below. Click on a message to go to edit it ↓
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
    btn_back = InlineKeyboardButton(text="←", callback_data=calls.FORMS_MessagesPagination(page=page-1).pack()) if page > 0 else InlineKeyboardButton(text="🛑", callback_data="123")
    buttons_row.append(btn_back)
    buttons_row.append(InlineKeyboardButton(text=f"{page+1}/{total_pages}", callback_data="forms_enter_messages_page"))

    btn_next = InlineKeyboardButton(text="→", callback_data=calls.FORMS_MessagesPagination(page=page+1).pack()) if page < total_pages - 1 else InlineKeyboardButton(text="🛑", callback_data="123")
    buttons_row.append(btn_next)
    rows.append(buttons_row)

    rows.append([InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MenuNavigation(to="settings").pack()),
                 InlineKeyboardButton(text="🔄️ Update", callback_data=calls.FORMS_MessagesPagination(page=page).pack())])
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
    enabled = "🟢 Enabled" if messages[message_id]["enabled"] else "🔴Off"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not specified"
    txt = textwrap.dedent(f"""
        ✒️ <b>Editing a message</b>

        🆔 <b>ID messages:</b>{message_id}
        💡 <b>Condition:</b>{enabled}
        💬 <b>Message text:</b> <blockquote>{message_text}</blockquote>

        Select an option to change ↓
    """)
    return txt

def settings_mess_page_kb(message_id: int, page: int = 0):
    messages = sett.get("messages")
    enabled = "🟢 Enabled" if messages[message_id]["enabled"] else "🔴Off"
    message_text = "\n".join(messages[message_id]["text"]) or "❌ Not specified"
    rows = [
        [InlineKeyboardButton(text=f"💡 State:{enabled}", callback_data="forms_switch_message_enabled")],
        [InlineKeyboardButton(text=f"💬 Message text:{message_text}", callback_data="forms_enter_message_text")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.FORMS_MessagesPagination(page=page).pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.FORMS_MessagePage(message_id=message_id).pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_mess_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ✒️ <b>Editing a message</b>
        \n{placeholder}
    """)
    return txt