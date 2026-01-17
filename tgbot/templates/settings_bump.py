import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_bump_text():
    config = sett.get("config")
    auto_bump_items_enabled = "🟢 Enabled" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Disabled"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_day_max_sequence = config["playerok"]["auto_bump_items"]["day_max_sequence"] or "❌ Not specified"
    auto_bump_items_night_max_sequence = config["playerok"]["auto_bump_items"]["night_max_sequence"] or "❌ Not specified"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    txt = textwrap.dedent(f"""
        <b>⚙️ Settings → ⬆️ Bump</b>

        <b>⬆️ Auto-bump items:</b> {auto_bump_items_enabled}
        <b>📦 Bump:</b> {auto_bump_items_all}

        <b>👥☀️ Max position during day:</b> {auto_bump_items_day_max_sequence}
        <b>👥🌙 Max position during night:</b> {auto_bump_items_night_max_sequence}

        <b>➕ Included:</b> {auto_bump_items_included}
        <b>➖ Excluded:</b> {auto_bump_items_excluded}

        <b>What is auto-bump items?</b>
        The bot will automatically bump items that fall beyond the specified position in the general goods table. That is, it will update their PREMIUM status so they are back on top. Allows you to bypass competitors, thereby getting more customers.

        <b>What is maximum position?</b>
        Maximum position in the general goods table, upon reaching which the bot will bump the item. For example, if you specify 10, the bot will bump items that have fallen to 10th place and below. Can be configured for day (from 06:00 to 22:00 MSK) and night (from 22:00 to 06:00 MSK).

        <b>Note:</b>
        If you choose "All items", then all items will be bumped, except those specified in exclusions. If you choose "Specified items", then only the items you add to included will be bumped.

        Select a parameter to change ↓
    """)
    return txt


def settings_bump_kb():
    config = sett.get("config")
    auto_bump_items_enabled = "🟢 Enabled" if config["playerok"]["auto_bump_items"]["enabled"] else "🔴 Disabled"
    auto_bump_items_all = "All items" if config["playerok"]["auto_bump_items"]["all"] else "Specified items"
    auto_bump_items_day_max_sequence = config["playerok"]["auto_bump_items"]["day_max_sequence"] or "❌ Not specified"
    auto_bump_items_night_max_sequence = config["playerok"]["auto_bump_items"]["night_max_sequence"] or "❌ Not specified"
    auto_bump_items = sett.get("auto_bump_items")
    auto_bump_items_included = len(auto_bump_items["included"])
    auto_bump_items_excluded = len(auto_bump_items["excluded"])
    rows = [
        [InlineKeyboardButton(text=f"⬆️ Auto-bump items: {auto_bump_items_enabled}", callback_data="switch_auto_bump_items_enabled")],
        [InlineKeyboardButton(text=f"📦 Bump: {auto_bump_items_all}", callback_data="switch_auto_bump_items_all")],
        [
        InlineKeyboardButton(text=f"👥☀️ Max position during day: {auto_bump_items_day_max_sequence}", callback_data="enter_auto_bump_items_day_max_sequence"),
        InlineKeyboardButton(text=f"👥🌙 Max position during night: {auto_bump_items_night_max_sequence}", callback_data="enter_auto_bump_items_night_max_sequence")
        ],
        [
        InlineKeyboardButton(text=f"➕ Included: {auto_bump_items_included}", callback_data=calls.IncludedBumpItemsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded: {auto_bump_items_excluded}", callback_data=calls.ExcludedBumpItemsPagination(page=0).pack())
        ],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.SettingsNavigation(to="bump").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_bump_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>⚙️ Settings → ⬆️ Bump</b>
        \n{placeholder}
    """)
    return txt