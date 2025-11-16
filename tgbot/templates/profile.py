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
        <b>👤 Nickname:</b> {profile.username}
        <b>📪 Email:</b> {profile.email}
        <b>💬 Feedback:</b> {profile.reviews_count} (<b>Rating:</b> {profile.rating} ⭐)
        
        <b>💰 Balance:</b> {profile.balance.value}₽
          ┣ <b>👜 Available:</b> {profile.balance.available}₽
          ┣ <b>⌛ In process:</b> {profile.balance.pending_income}₽
          ┗ <b>❄️ Frozen:</b> {profile.balance.frozen}₽
        
        <b>📦 Items:</b>
          ┣ <b>➖ Finished:</b> {profile.stats.items.finished}
          ┗ <b>♾️ Summary:</b> {profile.stats.items.total}
        
        <b>🛍️ Boughts:</b>
          ┣ <b>➕ Active:</b> {profile.stats.deals.incoming.total - profile.stats.deals.incoming.finished}
          ┣ <b>➖ Finished:</b> {profile.stats.deals.incoming.finished}
          ┗ <b>♾️ Summary:</b> {profile.stats.deals.incoming.total}

        <b>🛒 Sales:</b>
          ┣ <b>➕ Active:</b> {profile.stats.deals.outgoing.total - profile.stats.deals.outgoing.finished}
          ┣ <b>➖ Finished:</b> {profile.stats.deals.outgoing.finished}
          ┗ <b>♾️ Summary:</b> {profile.stats.deals.outgoing.total}
        
        <b>📅 Date of registration:</b> {datetime.fromisoformat(profile.created_at.replace('Z', '+00:00')).strftime('%d.%m.%Y %H:%M:%S')}

        Select action↓
    """)
    return txt


def profile_kb():
    rows = [
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.MenuNavigation(to="profile").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb
