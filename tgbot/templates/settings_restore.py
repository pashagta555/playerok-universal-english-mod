import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_restore_text():
    config = sett.get("config")
    
    auto_restore_items_sold = '🟢 Included' if config["playerok"]["auto_restore_items"]["sold"] else '🔴 Off'
    auto_restore_items_expired = '🟢 Included' if config["playerok"]["auto_restore_items"]["expired"] else '🔴 Off'
    auto_restore_items_all = 'All items' if config["playerok"]["auto_restore_items"]["all"] else 'Specified items'
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    
    txt = textwrap.dedent(f"""<b>♻️ Auto-Restore</b>

        <b>♻️ Auto item restore:</b>
        <b>・ Sold:</b> {auto_restore_items_sold}
        <b>・ Expired:</b> {auto_restore_items_expired}
        <b>📦 Restore:</b> {auto_restore_items_all}
        <b>➕ Included:</b> {auto_restore_items_included}
        <b>➖ Excluded:</b> {auto_restore_items_excluded}

        <b>How does auto-restore work?</b>
        This feature automatically relists an item after it is sold or expired, so it appears on sale again with the same priority status.

        <b>Note:</b>
        If you select "All items", everything will be restored except items from the excluded list.
        If you select "Specified items", only items from the included list will be restored.""")
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
        [InlineKeyboardButton(text=f"🛒 Sold:{auto_restore_items_sold}", callback_data="switch_auto_restore_items_sold")],
        [InlineKeyboardButton(text=f"⏰ Expired:{auto_restore_items_expired}", callback_data="switch_auto_restore_items_expired")],
        [InlineKeyboardButton(text=f"📦 Restore:{auto_restore_items_all}", callback_data="switch_auto_restore_items_all")],
        [
        InlineKeyboardButton(text=f"➕ Included:{auto_restore_items_included}", callback_data=calls.IncludedRestoreItemsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded:{auto_restore_items_excluded}", callback_data=calls.ExcludedRestoreItemsPagination(page=0).pack())
        ],
        [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_restore_float_text(placeholder: str):
    txt = textwrap.dedent(f"""<b>♻️ Auto-Restore</b>
        \n{placeholder}
    """)
    return txt