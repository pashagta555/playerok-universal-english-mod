from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import textwrap
from datetime import datetime, timedelta

from data import Data as data
from settings import Settings as sett

from .. import callback_datas as calls


def events_text():
    config = sett.get("config")
    latest_events_times = data.get("latest_events_times")
    
    last_bump_items = (datetime.fromisoformat(latest_events_times["auto_bump_items"]).strftime("%d.%m.%Y %H:%M")) if latest_events_times.get("auto_bump_items") else "❌ Never"
    next_bump_items = ((datetime.fromisoformat(latest_events_times["auto_bump_items"]) if latest_events_times.get("auto_bump_items") else datetime.now()) + timedelta(seconds=config["playerok"]["auto_bump_items"]["interval"])).strftime("%d.%m.%Y %H:%M")
    last_withdrawal = (datetime.fromisoformat(latest_events_times["auto_withdrawal"]).strftime("%d.%m.%Y %H:%M")) if latest_events_times.get("auto_withdrawal") else "❌ Never"
    next_withdrawal = ((datetime.fromisoformat(latest_events_times["auto_withdrawal"]) if latest_events_times.get("auto_withdrawal") else datetime.now()) + timedelta(seconds=config["playerok"]["auto_withdrawal"]["interval"])).strftime("%d.%m.%Y %H:%M")
    
    txt = textwrap.dedent(f"""
        <b>🚩 Events</b>

        <b>📆⬆️ Item bumping:</b>
        ・ <b>Last:</b> {last_bump_items}
        ・ <b>Next:</b> {next_bump_items}

        <b>📆💸 Withdrawals:</b>
        ・ <b>Last:</b> {last_withdrawal}
        ・ <b>Next:</b> {next_withdrawal}
    """)
    return txt


def events_kb():
    rows = [
        [InlineKeyboardButton(text="⬆️ Bump items", callback_data="confirm_bump_items")],
        [InlineKeyboardButton(text="💸 Withdraw funds", callback_data="confirm_withdrawal")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def events_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>🚩 Events</b>
        \n{placeholder}
    """)
    return txt