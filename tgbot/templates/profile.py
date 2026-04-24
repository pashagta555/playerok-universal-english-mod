import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from .. import callback_datas as calls

def profile_text():
    from plbot.playerokbot import get_playerok_bot
    plbot = get_playerok_bot()
    plbot.refresh_account()
    acc = plbot.account
    profile = acc.profile
    txt = textwrap.dedent(f"\n        <b>👤 Мой профиль</b>\n\n        <b>🆔 ID:</b> <code>{profile.id}</code>\n        <b>👤 Никнейм:</b> {profile.username}\n        <b>📪 Email:</b> {profile.email}\n        <b>💬 Отзывы:</b> {profile.reviews_count} (<b>Рейтинг:</b> {profile.rating} ⭐)\n        \n        <b>💰 Баланс:</b> {(profile.balance.value if profile.balance else 0)}₽\n        <b>・ 👜 Доступно:</b> {(profile.balance.available if profile.balance else 0)}₽\n        <b>・ ⌛ В процессе:</b> {(profile.balance.pending_income if profile.balance else 0)}₽\n        <b>・ ❄️ Заморожено:</b> {(profile.balance.frozen if profile.balance else 0)}₽\n        \n        <b>📦 Предметы:</b>\n        <b>・ ➕ Активные:</b> {profile.stats.items.total - profile.stats.items.finished}\n        <b>・ ➖ Завершённые:</b> {profile.stats.items.finished}\n        <b>・ ♾️ Всего:</b> {profile.stats.items.total}\n        \n        <b>🛍️ Покупки:</b>\n        <b>・ ➕ Активные:</b> {profile.stats.deals.incoming.total - profile.stats.deals.incoming.finished}\n        <b>・ ➖ Завершённые:</b> {profile.stats.deals.incoming.finished}\n        <b>・ ♾️ Всего:</b> {profile.stats.deals.incoming.total}\n\n        <b>🛒 Продажи:</b>\n        <b>・ ➕ Активные:</b> {profile.stats.deals.outgoing.total - profile.stats.deals.outgoing.finished}\n        <b>・ ➖ Завершено:</b> {profile.stats.deals.outgoing.finished}\n        <b>・ ♾️ Всего:</b> {profile.stats.deals.outgoing.total}\n        \n        <b>📅 Дата регистрации:</b> {datetime.fromisoformat(profile.created_at.replace('Z', '+00:00')).strftime('%d.%m.%Y %H:%M:%S')}\n    ")
    return txt

def profile_kb():
    rows = [[InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb