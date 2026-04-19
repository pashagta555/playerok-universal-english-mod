I can translate the code for you, but I'll keep the original code format unchanged. Here is the translation:

**settings_logger_text()**

```
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_logger_text():
    config = sett.get("config")
    
    tg_logging_enabled = "Enabled" if config["playerok"]["tg_logging"]["enabled"] else "Disabled"
    tg_logging_chat_id = f"{config['playerok']['tg_logging']['chat_id']}" or "Your chat with the bot"
    tg_logging_events = config["playerok"]["tg_logging"]["events"] or {}
    event_new_user_message = "Enabled" if tg_logging_events["new_user_message"] else "Disabled"
    event_new_system_message = "Enabled" if tg_logging_events["new_system_message"] else "Disabled"
    event_new_deal = "Enabled" if tg_logging_events["new_deal"] else "Disabled"
    event_new_review = "Enabled" if tg_logging_events["new_review"] else "Disabled"
    event_new_problem = "Enabled" if tg_logging_events["new_problem"] else "Disabled"
    event_deal_status_changed = "Enabled" if tg_logging_events["deal_status_changed"] else "Disabled"
    
    txt = textwrap.dedent(f"""
        <b>Logger</b>

        <b>Events:</b> {tg_logging_enabled}
        <b>ID chat for logs:</b> {tg_logging_chat_id}
        
        <b>Events:</b>
        ・ {event_new_user_message}  New message from user
        ・ {event_new_system_message}  New system message
        ・ {event_new_deal}  New deal
        ・ {event_new_review}  New review
        ・ {event_new_problem}  New problem in a deal
        ・ {event_deal_status_changed}  Deal status changed
    """)
    return txt


**settings_logger_kb()**

```
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_logger_kb():
    config = sett.get("config")
    
    tg_logging_enabled = "Enabled" if config["playerok"]["tg_logging"]["enabled"] else "Disabled"
    tg_logging_chat_id = f"{config['playerok']['tg_logging']['chat_id']}" or "Your chat with the bot"
    tg_logging_events = config["playerok"]["tg_logging"]["events"] or {}
    event_new_user_message = "Enabled" if tg_logging_events["new_user_message"] else "Disabled"
    event_new_system_message = "Enabled" if tg_logging_events["new_system_message"] else "Disabled"
    event_new_deal = "Enabled" if tg_logging_events["new_deal"] else "Disabled"
    event_new_review = "Enabled" if tg_logging_events["new_review"] else "Disabled"
    event_new_problem = "Enabled" if tg_logging_events["new_problem"] else "Disabled"
    event_deal_status_changed = "Enabled" if tg_logging_events["deal_status_changed"] else "Disabled"
    
    rows = [
        [InlineKeyboardButton(text=f"Logger: {tg_logging_enabled}", callback_data="switch_tg_logging_enabled")],
        [InlineKeyboardButton(text=f"ID chat for logs: {tg_logging_chat_id}", callback_data="enter_tg_logging_chat_id")],
        [
            InlineKeyboardButton(text=f"{event_new_user_message}  New message from user", callback_data="switch_tg_logging_event_new_user_message"),
            InlineKeyboardButton(text=f"{event_new_system_message}  New system message", callback_data="switch_tg_logging_event_new_system_message"),
        ],
        [
            InlineKeyboardButton(text=f"{event_new_deal}  New deal", callback_data="switch_tg_logging_event_new_deal"),
            InlineKeyboardButton(text=f"{event_new_review}  New review", callback_data="switch_tg_logging_event_new_review"),
        ],
        [
            InlineKeyboardButton(text=f"{event_new_problem}  New problem in a deal", callback_data="switch_tg_logging_event_new_problem"),
            InlineKeyboardButton(text=f"{event_deal_status_changed}  Deal status changed", callback_data="switch_tg_logging_event_deal_status_changed")
        ],
        [InlineKeyboardButton(text="Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    if config["playerok"]["tg_logging"]["chat_id"]:
        rows[1].append(InlineKeyboardButton(text=f"Clear", callback_data="clean_tg_logging_chat_id"))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


**settings_logger_float_text()**

```
def settings_logger_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>Logger</b>
        \n{placeholder}
    """)
    return txt
```

