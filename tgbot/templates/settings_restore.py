import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_restore_text():
    config = sett.get("config")
    auto_restore_items_sold = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["sold"] else "🔴 Disabled"
    auto_restore_items_expired = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["expired"] else "🔴 Disabled"
    auto_restore_items_all = "All items" if config["playerok"]["auto_restore_items"]["all"] else "Selected items"
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    txt = textwrap.dedent(f"""
        <b>♻️ Restore</b>

        <b>♻️ Auto-restore items:</b>
        <b>・ Sold:</b> {auto_restore_items_sold}
        <b>・ Expired:</b> {auto_restore_items_expired}

        <b>📦 Restore:</b> {auto_restore_items_all}

        <b>➕ Included:</b> {auto_restore_items_included}
        <b>➖ Excluded:</b> {auto_restore_items_excluded}

        <b>What is auto-restore?</b>
        Automatically re-list items that were sold or expired, with the same priority as before.

        <b>Note:</b>
        "All items" = restore everything except exclusions. "Selected items" = restore only those in the included list.
    """)
    return txt


def settings_restore_kb():
    config = sett.get("config")
    auto_restore_items_sold = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["sold"] else "🔴 Disabled"
    auto_restore_items_expired = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["expired"] else "🔴 Disabled"
    auto_restore_items_all = "All items" if config["playerok"]["auto_restore_items"]["all"] else "Selected items"
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    rows = [
        [InlineKeyboardButton(text=f"🛒 Sold: {auto_restore_items_sold}", callback_data="switch_auto_restore_items_sold")],
        [InlineKeyboardButton(text=f"⏰ Expired: {auto_restore_items_expired}", callback_data="switch_auto_restore_items_expired")],
        [InlineKeyboardButton(text=f"📦 Restore: {auto_restore_items_all}", callback_data="switch_auto_restore_items_all")],
        [
        InlineKeyboardButton(text=f"➕ Included: {auto_restore_items_included}", callback_data=calls.IncludedRestoreItemsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded: {auto_restore_items_excluded}", callback_data=calls.ExcludedRestoreItemsPagination(page=0).pack())
        ],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_restore_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>♻️ Restore</b>
        \n{placeholder}
    """)
    return txt