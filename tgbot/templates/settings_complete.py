import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_complete_text():
    config = sett.get("config")
    
    enabled = "🟢 Included" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Off"
    all = "All items" if config["playerok"]["auto_complete_deals"]["all"] else "Specified items"
    
    auto_complete_deals = sett.get("auto_complete_deals")
    included = len(auto_complete_deals["included"])
    excluded = len(auto_complete_deals["excluded"])
    
    txt = textwrap.dedent(f"""
        <b>☑️ Auto-confirmation</b>

        <b>☑️ Auto-confirm deals:</b> {enabled}
        <b>📦 Confirm deals:</b> {all}

        <b>➕ Included:</b> {included}
        <b>➖ Excluded:</b> {excluded}

        <b>What is auto-confirmation?</b>
        The bot will automatically confirm completed deals for matching items.

        <b>Note:</b>
        If you choose "All items", deals for all items will be confirmed except items in the excluded list.
        If you choose "Specified items", only deals for items in the included list will be confirmed.
    """)
    return txt


def settings_complete_kb():
    config = sett.get("config")
    
    enabled = "🟢 Included" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Off"
    all = "All items" if config["playerok"]["auto_complete_deals"]["all"] else "Specified items"
    
    auto_complete_deals = sett.get("auto_complete_deals")
    included = len(auto_complete_deals["included"])
    excluded = len(auto_complete_deals["excluded"])
    
    rows = [
        [InlineKeyboardButton(text=f"☑️ Auto-confirm deals: {enabled}", callback_data="switch_auto_complete_deals_enabled")],
        [InlineKeyboardButton(text=f"📦 Confirm deals: {all}", callback_data="switch_auto_complete_deals_all")],
        [
        InlineKeyboardButton(text=f"➕ Included: {included}", callback_data=calls.IncludedCompleteDealsPagination(page=0).pack()),
        InlineKeyboardButton(text=f"➖ Excluded: {excluded}", callback_data=calls.ExcludedCompleteDealsPagination(page=0).pack())
        ],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_complete_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>☑️ Auto-confirmation</b>
        \n{placeholder}
    """)
    return txt