import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_restore_text():
    config = sett.get("config")
    auto_restore_items_enabled = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["enabled"] else "🔴 Disabled"
    auto_restore_items_all = "All items" if config["playerok"]["auto_restore_items"]["all"] else "Specified items"
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → ♻️ Restore</b>

        ♻️ <b>Auto-restore items:</b> {auto_restore_items_enabled}
        📦 <b>Restore:</b> {auto_restore_items_all}

        ➕ <b>Included:</b> {auto_restore_items_included}
        ➖ <b>Excluded:</b> {auto_restore_items_excluded}

        <b>What is automatic item restoration?</b>
        On Playerok, as soon as your item is purchased - it disappears from sale. This feature will automatically restore (re-list) the item that was just purchased so it's on sale again. The item will be listed with the same priority status as before.

        <b>Note:</b>
        If you choose "All items", all items will be restored except those specified in exclusions. If you choose "Specified items", only those items you add to included will be restored.
        
        Select parameter to change ↓
    """)
    return txt


def settings_restore_kb():
    config = sett.get("config")
    auto_restore_items_enabled = "🟢 Enabled" if config["playerok"]["auto_restore_items"]["enabled"] else "🔴 Disabled"
    auto_restore_items_all = "All items" if config["playerok"]["auto_restore_items"]["all"] else "Specified items"
    auto_restore_items = sett.get("auto_restore_items")
    auto_restore_items_included = len(auto_restore_items["included"])
    auto_restore_items_excluded = len(auto_restore_items["excluded"])
    rows = [
        [InlineKeyboardButton(text=f"♻️ Auto-restore items: {auto_restore_items_enabled}", callback_data="switch_auto_restore_items_enabled")],
        [InlineKeyboardButton(text=f"📦 Restore: {auto_restore_items_all}", callback_data="switch_auto_restore_items_all")],
        [
        InlineKeyboardButton(text=f"➕ Included: {auto_restore_items_included}", callback_data=calls.IncludedRestoreItemsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded: {auto_restore_items_excluded}", callback_data=calls.ExcludedRestoreItemsPagination(page=0).pack())
        ],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.SettingsNavigation(to="items").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_restore_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → ♻️ Restore</b>
        \n{placeholder}
    """)
    return txt
