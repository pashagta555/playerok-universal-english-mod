import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import get_stats
from .. import callback_datas as calls

def stats_text():
    try:
        stats = get_stats()
        txt = textwrap.dedent(f"\n            <b>📊 Статистика</b>\n\n            ━━━━━━━━━━━━━━\n            \n            <b>⏰ За последние 24 часа:</b>\n            \n            <b>📋 Заказы:</b>\n            <b>・</b> ➕ Активных: {stats['day']['active']}\n            <b>・</b> ➖ Завершённых: {stats['day']['completed']}\n            <b>・</b> 🔙 Возвратов: {stats['day']['refunded']}\n            <b>・</b> ♾️ Всего: {stats['day']['orders']}\n            \n            <b>💸 Заработано:</b> {stats['day']['profit']} руб.\n            <b>🔥 Лучший товар:</b> {stats['day']['best']}\n\n            ━━━━━━━━━━━━━━\n\n            <b>📅 За последнюю неделю:</b>\n            \n            <b>📋 Заказы:</b>\n            <b>・</b> ➕ Активных: {stats['week']['active']}\n            <b>・</b> ➖ Завершённых: {stats['week']['completed']}\n            <b>・</b> 🔙 Возвратов: {stats['week']['refunded']}\n            <b>・</b> ♾️ Всего: {stats['week']['orders']}\n            \n            <b>💸 Заработано:</b> {stats['week']['profit']} руб.\n            <b>🔥 Лучший товар:</b> {stats['week']['best']}\n\n            ━━━━━━━━━━━━━━\n\n            <b>🗓 За последний месяц:</b>\n            \n            <b>📋 Заказы:</b>\n            <b>・</b> ➕ Активных: {stats['month']['active']}\n            <b>・</b> ➖ Завершённых: {stats['month']['completed']}\n            <b>・</b> 🔙 Возвратов: {stats['month']['refunded']}\n            <b>・</b> ♾️ Всего: {stats['month']['orders']}\n            \n            <b>💸 Заработано:</b> {stats['month']['profit']} руб.\n            <b>🔥 Лучший товар:</b> {stats['month']['best']}\n\n            ━━━━━━━━━━━━━━\n            \n            <b>📈 За все время:</b>\n            \n            <b>📋 Заказы:</b>\n            <b>・</b> ➕ Активных: {stats['all']['active']}\n            <b>・</b> ➖ Завершённых: {stats['all']['completed']}\n            <b>・</b> 🔙 Возвратов: {stats['all']['refunded']}\n            <b>・</b> ♾️ Всего: {stats['all']['orders']}\n            \n            <b>💸 Заработано:</b> {stats['all']['profit']} руб.\n            <b>🔥 Лучший товар:</b> {stats['all']['best']}\n\n            ━━━━━━━━━━━━━━\n            \n            <i>Подсчитывается только во время использования бота</i>\n        ")
        return txt
    except:
        import traceback
        traceback.print_exc()

def stats_kb():
    rows = [[InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb