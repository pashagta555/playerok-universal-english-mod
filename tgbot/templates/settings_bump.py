import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_bump_text():
    config = sett.get("config")
    
    auto_bump_items_enabled = "🟢 Included" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Off"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_interval = config["playerok"]["auto_bump_items"]["interval"] or "❌ Not indicated"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    
    txt = textwrap.dedent(f"""
        <b>⬆️ Auto-Bump</b>

        <b>⬆️ Auto-bump items:</b> {auto_bump_items_enabled}
        <b>📦 Bump:</b> {auto_bump_items_all}
        <b>⏲️ Bump interval:</b> {auto_bump_items_interval} sec.

        <b>➕ Included:</b> {auto_bump_items_included}
        <b>➖ Excluded:</b> {auto_bump_items_excluded}

        <b>What is auto-bump?</b>
        The bot automatically bumps your items to keep them higher in listings. This helps keep your offers visible and improve conversion.

        <b>Note:</b>
        If you choose "All items", all items will be bumped except those in the excluded list.
        If you choose "Specified items", only items in the included list will be bumped.
    """)
    return txt


def settings_bump_kb():
    config = sett.get("config")
    
    auto_bump_items_enabled = "🟢 Included" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Off"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_interval = config["playerok"]["auto_bump_items"]["interval"] or "❌ Not indicated"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    
    rows = [
        [InlineKeyboardButton(text=f"⬆️ Auto-bump items: {auto_bump_items_enabled}", callback_data="switch_auto_bump_items_enabled")],
        [InlineKeyboardButton(text=f"📦 Bump: {auto_bump_items_all}", callback_data="switch_auto_bump_items_all")],
        [InlineKeyboardButton(text=f"⏲️ Bump interval: {auto_bump_items_interval} sec.", callback_data="enter_auto_bump_items_interval")],
        [
        InlineKeyboardButton(text=f"➕ Included: {auto_bump_items_included}", callback_data=calls.IncludedBumpItemsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded: {auto_bump_items_excluded}", callback_data=calls.ExcludedBumpItemsPagination(page=0).pack())
        ],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_bump_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>⬆️ Auto-Bump</b>
        \n{placeholder}
    """)
    return txt