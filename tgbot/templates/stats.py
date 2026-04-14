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
            
            <b>⏰ For latest 24 hours:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['day']['active']}
            <b>・</b> ➖ Completed: {stats['day']['completed']}
            <b>・</b> 🔙 Returns: {stats['day']['refunded']}
            <b>・</b> ♾️ Total: {stats['day']['orders']}
            
            <b>💸 Earned:</b> {stats['day']['profit']} rub.
            <b>🔥 Best product:</b> {stats['day']['best']}

            ━━━━━━━━━━━━━━

            <b>📅 For last a week:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['week']['active']}
            <b>・</b> ➖ Completed: {stats['week']['completed']}
            <b>・</b> 🔙 Returns: {stats['week']['refunded']}
            <b>・</b> ♾️ Total: {stats['week']['orders']}
            
            <b>💸 Earned:</b> {stats['week']['profit']} rub.
            <b>🔥 Best product:</b> {stats['week']['best']}

            ━━━━━━━━━━━━━━

            <b>🗓 For last month:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['month']['active']}
            <b>・</b> ➖ Completed: {stats['month']['completed']}
            <b>・</b> 🔙 Returns: {stats['month']['refunded']}
            <b>・</b> ♾️ Total: {stats['month']['orders']}
            
            <b>💸 Earned:</b> {stats['month']['profit']} rub.
            <b>🔥 Best product:</b> {stats['month']['best']}

            ━━━━━━━━━━━━━━
            
            <b>📈 For All time:</b>
            
            <b>📋 Orders:</b>
            <b>・</b> ➕ Active: {stats['all']['active']}
            <b>・</b> ➖ Completed: {stats['all']['completed']}
            <b>・</b> 🔙 Returns: {stats['all']['refunded']}
            <b>・</b> ♾️ Total: {stats['all']['orders']}
            
            <b>💸 Earned:</b> {stats['all']['profit']} rub.
            <b>🔥 Best product:</b> {stats['all']['best']}

            ━━━━━━━━━━━━━━
            
            <i>Counting only in time use bot</i>
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