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
        <b>⬆️ Auto-raising</b>

        <b>⬆️ Auto-raising items:</b> {auto_bump_items_enabled}
        <b>📦 lift:</b> {auto_bump_items_all}
        <b>⏲️ Interval raising:</b> {auto_bump_items_interval} sec.

        <b>➕ Included:</b> {auto_bump_items_included}
        <b>➖ Excluded:</b> {auto_bump_items_excluded}

        <b>What for auto-raising items?</b>
        Bot will automatically lift items, which will come out for specified position V table general goods. That There is, will update their PREMIUM status, to They again were V top. Allows bypass competitors, those the most receiving more clients.

        <b>Note:</b>
        If You choose "All items", That will get up All goods, except those, What indicated V exceptions. If You choose "Specified items", That will get up only those goods, which You add in included.
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
        [InlineKeyboardButton(text=f"⬆️ Auto-raising items: {auto_bump_items_enabled}", callback_data="switch_auto_bump_items_enabled")],
        [InlineKeyboardButton(text=f"📦 lift: {auto_bump_items_all}", callback_data="switch_auto_bump_items_all")],
        [InlineKeyboardButton(text=f"⏲️ Interval raising: {auto_bump_items_interval} sec.", callback_data="enter_auto_bump_items_interval")],
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
        <b>⬆️ Auto-raising</b>
        \n{placeholder}
    """)
    return txt