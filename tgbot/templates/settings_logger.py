import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_logger_text():
    config = sett.get("config")
    tg_logging_enabled = "🟢 Turned on" if config["playerok"]["tg_logging"]["enabled"] else "🔴 Turned off"
    tg_logging_chat_id = config["playerok"]["tg_logging"]["chat_id"] or "✔️ Ваш чат с ботом"
    tg_logging_events = config["playerok"]["tg_logging"]["events"] or {}
    event_new_user_message = "🟢" if tg_logging_events["new_user_message"] else "🔴"
    event_new_system_message = "🟢" if tg_logging_events["new_system_message"] else "🔴"
    event_new_deal = "🟢" if tg_logging_events["new_deal"] else "🔴"
    event_new_review = "🟢" if tg_logging_events["new_review"] else "🔴"
    event_new_problem = "🟢" if tg_logging_events["new_problem"] else "🔴"
    event_deal_status_changed = "🟢" if tg_logging_events["deal_status_changed"] else "🔴"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 👀 Logs</b>

        👀 <b>Ivent loggin of the Playerok to Telegram:</b> {tg_logging_enabled}
        💬 <b>Chat's id for the logs:</b> <b>{tg_logging_chat_id}</b>
        📢 <b>Log ivents:</b>
        ┣ {event_new_user_message} <b>💬👤 New message from the user</b>
        ┣ {event_new_system_message} <b>💬⚙️ New system message</b>
        ┣ {event_new_deal} <b>📋 New deal</b>
        ┣ {event_new_review} <b>💬✨ New feedback</b>
        ┣ {event_new_problem} <b>🤬 New problem in the deal</b>
        ┗ {event_deal_status_changed} <b>🔄️📋 Status of the deal was changed</b>
        
        Select parametre to be changed ↓
    """)
    return txt


def settings_logger_kb():
    config = sett.get("config")
    tg_logging_enabled = "🟢 Turned on" if config["playerok"]["tg_logging"]["enabled"] else "🔴 Tirned off"
    tg_logging_chat_id = config["playerok"]["tg_logging"]["chat_id"] or "✔️ Ваш чат с ботом"
    tg_logging_events = config["playerok"]["tg_logging"]["events"] or {}
    event_new_user_message = "🟢" if tg_logging_events["new_user_message"] else "🔴"
    event_new_system_message = "🟢" if tg_logging_events["new_system_message"] else "🔴"
    event_new_deal = "🟢" if tg_logging_events["new_deal"] else "🔴"
    event_new_review = "🟢" if tg_logging_events["new_review"] else "🔴"
    event_new_problem = "🟢" if tg_logging_events["new_problem"] else "🔴"
    event_deal_status_changed = "🟢" if tg_logging_events["deal_status_changed"] else "🔴"
    rows = [
        [InlineKeyboardButton(text=f"👀 Ivent logging Playerok в Telegram: {tg_logging_enabled}", callback_data="switch_tg_logging_enabled")],
        [InlineKeyboardButton(text=f"💬 Chat's id for the logs: {tg_logging_chat_id}", callback_data="enter_tg_logging_chat_id")],
        [
        InlineKeyboardButton(text=f"{event_new_user_message} 💬👤 New message user", callback_data="switch_tg_logging_event_new_user_message"),
        InlineKeyboardButton(text=f"{event_new_system_message} 💬⚙️New system message", callback_data="switch_tg_logging_event_new_system_message"),
        InlineKeyboardButton(text=f"{event_new_deal} 📋 New deal", callback_data="switch_tg_logging_event_new_deal")
        ],
        [
        InlineKeyboardButton(text=f"{event_new_review} 💬✨ New feadback", callback_data="switch_tg_logging_event_new_review"),
        InlineKeyboardButton(text=f"{event_new_problem} 🤬 New problem in the deal", callback_data="switch_tg_logging_event_new_problem"),
        InlineKeyboardButton(text=f"{event_deal_status_changed} 🔄️📋 Status of the deal was changed", callback_data="switch_tg_logging_event_deal_status_changed")
        ],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.SettingsNavigation(to="logger").pack())
        ]
    ]
    if config["playerok"]["tg_logging"]["chat_id"]:
        rows[1].append(InlineKeyboardButton(text=f"❌💬 Очистить", callback_data="clean_tg_logging_chat_id"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_logger_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → 👀 Logs</b>
        \n{placeholder}
    """)
    return txt
