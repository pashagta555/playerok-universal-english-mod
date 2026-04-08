import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as set

from .. import callback_datas as calls


def settings_restore_text():
    config = sett.get("config")
    
    auto_restore_items_sold = '🟢 Included' if config["playerok"]["auto_restore_items"]["sold"] else '🔴 Off'
    auto_restore_items_expired = '🟢 Included' if config["playerok"]["auto_restore_items"]["expired"] else '🔴 Off'
    auto_restore_items_all = 'All items' if config["playerok"]["auto_restore_items"]["all"] else 'Specified items'
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    
    txt = textwrap.dedent(f"""
        <b>♻️ Auto-recovery</b>

        <b>♻️ Auto-recovery of items:</b>
        <b>・ Sold:</b> {auto_restore_items_sold}
        <b>・ Expired:</b> {auto_restore_items_expired}

        <b>📦 Restore:</b> {auto_restore_items_all}

        <b>➕ Included:</b> {auto_restore_items_included}
        <b>➖ Excluded:</b> {auto_restore_items_excluded}

        <b>What is this auto-recovery of items?</b>
        This feature will allow you to automatically restore (relist) an item that has just been purchased or has expired so that it is back on sale. The item will be listed with the same priority status as before.

        <b>Note:</b>
        If you select "All items", all items will be restored except those specified in the exceptions. If you select "Specified Items", only those items that you add to the included ones will be restored.
    """)
    return txt


def settings_restore_kb():
    config = sett.get("config")
    
    auto_restore_items_sold = '🟢 Included' if config["playerok"]["auto_restore_items"]["sold"] else '🔴 Off'
    auto_restore_items_expired = '🟢 Included' if config["playerok"]["auto_restore_items"]["expired"] else '🔴 Off'
    auto_restore_items_all = 'All items' if config["playerok"]["auto_restore_items"]["all"] else 'Specified items'
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
        [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_restore_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>♻️ Author-restoration</b>
        \n{placeholder}
    """)
    return txt