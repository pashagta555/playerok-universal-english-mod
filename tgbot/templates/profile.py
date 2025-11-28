import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from .. import callback_datas as calls


def profile_text():
    from plbot.playerokbot import get_playerok_bot
    acc = get_playerok_bot().playerok_account.get()
    profile = acc.profile
    txt = textwrap.dedent(f"""
        👤 <b>My profile</b>

        <b>🆔 ID:</b> <code>{profile.id}</code>
        <b>👤 Username:</b> {profile.username}
        <b>📪 Email:</b> {profile.email}
        <b>💬 Reviews:</b> {profile.reviews_count} (<b>Rating:</b> {profile.rating} ⭐)
        
        <b>💰 Balance:</b> {profile.balance.value}₽
          ┣ <b>👜 Available:</b> {profile.balance.available}₽
          ┣ <b>⌛ Pending:</b> {profile.balance.pending_income}₽
          ┗ <b>❄️ Frozen:</b> {profile.balance.frozen}₽
        
        <b>📦 Items:</b>
          ┣ <b>➖ Expired:</b> {profile.stats.items.finished}
          ┗ <b>♾️ Total:</b> {profile.stats.items.total}
        
        <b>🛍️ Purchases:</b>
          ┣ <b>➕ Active:</b> {profile.stats.deals.incoming.total - profile.stats.deals.incoming.finished}
          ┣ <b>➖ Completed:</b> {profile.stats.deals.incoming.finished}
          ┗ <b>♾️ Total:</b> {profile.stats.deals.incoming.total}

        <b>🛒 Sales:</b>
          ┣ <b>➕ Active:</b> {profile.stats.deals.outgoing.total - profile.stats.deals.outgoing.finished}
          ┣ <b>➖ Completed:</b> {profile.stats.deals.outgoing.finished}
          ┗ <b>♾️ Total:</b> {profile.stats.deals.outgoing.total}
        
        <b>📅 Registration date:</b> {datetime.fromisoformat(profile.created_at.replace('Z', '+00:00')).strftime('%d.%m.%Y %H:%M:%S')}

        Select an action ↓
    """)
    return txt


def profile_kb():
    rows = [
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.MenuNavigation(to="profile").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb