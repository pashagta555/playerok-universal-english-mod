import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_bump_text():
    config = sett.get("config")
    auto_bump_items_enabled = "🟢 Enabled" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Disabled"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_interval = config["playerok"]["auto_bump_items"]["interval"] or "❌ Not specified"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    txt = textwrap.dedent(f"""
        <b>⬆️ Bumping</b>

        <b>⬆️ Auto-bumping of items:</b> {auto_bump_items_enabled}
        <b>📦 Bump:</b> {auto_bump_items_all}
        <b>⏲️ Bump interval:</b> {auto_bump_items_interval}

        <b>➕ Included:</b> {auto_bump_items_included}
        <b>➖ Excluded:</b> {auto_bump_items_excluded}

        <b>What is auto-bumping of items?</b>
        The bot will automatically bump items that have gone beyond the specified position in the general items table. That is, it will refresh their PREMIUM status so that they are back at the top. This helps to outrun competitors and get more customers.

        <b>Note:</b>
        If you select "All items", all items will be bumped except those specified in the exclusions. If you select "Specified items", only the items you add to the included list will be bumped.
    """)
    return txt


def settings_bump_kb():
    config = sett.get("config")
    auto_bump_items_enabled = "🟢 Enabled" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Disabled"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_interval = config["playerok"]["auto_bump_items"]["interval"] or "❌ Not specified"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    rows = [
        [InlineKeyboardButton(text=f"⬆️ Auto-bumping of items: {auto_bump_items_enabled}", callback_data="switch_auto_bump_items_enabled")],
        [InlineKeyboardButton(text=f"📦 Bump: {auto_bump_items_all}", callback_data="switch_auto_bump_items_all")],
        [InlineKeyboardButton(text=f"⏲️ Bump interval: {auto_bump_items_interval}", callback_data="enter_auto_bump_items_interval")],
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
        <b>⬆️ Bumping</b>
        \n{placeholder}
    """)
    return txt