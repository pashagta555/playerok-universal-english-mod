import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from plbot.stats import get_stats

from .. import callback_datas as calls


def stats_text():
    stats = get_stats()
    txt = textwrap.dedent(f"""
        <b>📊 Statistics</b>

        Bot launch date: <b>{stats.bot_launch_time.strftime("%d.%m.%Y %H:%M:%S") or 'Not started'}</b>

        <b>Statistics since launch:</b>
        ・ Completed: <b>{stats.deals_completed}</b>
        ・ Refunds: <b>{stats.deals_refunded}</b>
        ・ Earned: <b>{stats.earned_money}</b>₽
    """)
    return txt


def stats_kb():
    rows = [
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb