import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils import get_stats

from .. import callback_datas as calls


def stats_text():
    try:
        stats = get_stats()
        
        txt = textwrap.dedent(f"""
            <b>📊 Statistics</b>

            ━━━━━━━━━━━━━━
            
            <b>⏰ In the last 24 hours:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['day']['active']}
            <b>・</b> ➖ Completed: {stats['day']['completed']}
            <b>・</b> 🔙 Refunds: {stats['day']['refunded']}
            <b>・</b> ♾️ Total: {stats['day']['orders']}
            
            <b>💸 Earned:</b> {stats['day']['profit']} rub.
            <b>🔥 Best product:</b> {stats['day']['best']}

            ━━━━━━━━━━━━━━

            <b>📅 Over the last week:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['week']['active']}
            <b>・</b> ➖ Completed: {stats['week']['completed']}
            <b>・</b> 🔙 Refunds: {stats['week']['refunded']}
            <b>・</b> ♾️ Total: {stats['week']['orders']}
            
            <b>💸 Earned:</b> {stats['week']['profit']} rub.
            <b>🔥 Best product:</b> {stats['week']['best']}

            ━━━━━━━━━━━━━━

            <b>🗓 Over the last month:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['month']['active']}
            <b>・</b> ➖ Completed: {stats['month']['completed']}
            <b>・</b> 🔙 Refunds: {stats['month']['refunded']}
            <b>・</b> ♾️ Total: {stats['month']['orders']}
            
            <b>💸 Earned:</b> {stats['month']['profit']} rub.
            <b>🔥 Best product:</b> {stats['month']['best']}

            ━━━━━━━━━━━━━━
            
            <b>📈 All time:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['all']['active']}
            <b>・</b> ➖ Completed: {stats['all']['completed']}
            <b>・</b> 🔙 Refunds: {stats['all']['refunded']}
            <b>・</b> ♾️ Total: {stats['all']['orders']}
            
            <b>💸 Earned:</b> {stats['all']['profit']} rub.
            <b>🔥 Best product:</b> {stats['all']['best']}

            ━━━━━━━━━━━━━━
            
            <i>Counted only while using the bot</i>
        """)
        return txt
    except:
        import traceback
        traceback.print_exc()


def stats_kb():
    rows = [
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb