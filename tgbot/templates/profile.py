I can translate the text for you. However, I will keep the code unchanged.

The translated text is:

<b>👤 My Profile</b>

<b>🆔 ID:</b> <code>{profile.id}</code>
<b>👤 Nickname:</b> {profile.username}
<b>📪 Email:</b> {profile.email}
<b>💬 Reviews:</b> {profile.reviews_count} (<b>Ratings:</b> {profile.rating} ⭐)

<b>💰 Balance:</b> {profile.balance.value if profile.balance else 0}₽
<b>・ 👜 Available:</b> {profile.balance.available if profile.balance else 0}₽
<b>・ ⌛ Pending Income:</b> {profile.balance.pending_income if profile.balance else 0}₽
<b>・ ❄️ Frozen:</b> {profile.balance.frozen if profile.balance else 0}₽

<b>📦 Items:</b>
<b>・ ➕ Active:</b> {profile.stats.items.total - profile.stats.items.finished}
<b>・ ➖ Finished:</b> {profile.stats.items.finished}
<b>・ ♾️ Total:</b> {profile.stats.items.total}

<b>🛍️ Purchases:</b>
<b>・ ➕ Active:</b> {profile.stats.deals.incoming.total - profile.stats.deals.incoming.finished}
<b>・ ➖ Finished:</b> {profile.stats.deals.incoming.finished}
<b>・ ♾️ Total:</b> {profile.stats.deals.incoming.total}

<b>🛒 Sales:</b>
<b>・ ➕ Active:</b> {profile.stats.deals.outgoing.total - profile.stats.deals.outgoing.finished}
<b>・ ➖ Finished:</b> {profile.stats.deals.outgoing.finished}
<b>・ ♾️ Total:</b> {profile.stats.deals.outgoing.total}

<b>📅 Registration Date:</b> {datetime.fromisoformat(profile.created_at.replace('Z', '+00:00')).strftime('%d.%m.%Y %H:%M:%S')}

