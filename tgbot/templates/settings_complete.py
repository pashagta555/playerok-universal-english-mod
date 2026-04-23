import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as set

from .. import callback_datas as calls


def settings_complete_text():
    config = sett.get("config")
    
    enabled = "🟢 Enabled" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Disabled"
    all = "All items" if config["playerok"]["auto_complete_deals"]["all"] else "Specified items"
    
    auto_complete_deals = sett.get("auto_complete_deals")
    included = len(auto_complete_deals["included"])
    excluded = len(auto_complete_deals["excluded"])
    
    txt = textwrap.dedent(f"""
        <b>☑️ Auto-confirmation</b>

        <b>☑️ Auto-confirmation of transactions:</b> {enabled}
        <b>📦 Confirm deal:</b> {all}

        <b>➕ Included:</b> {included}
        <b>➖ Excluded:</b> {excluded}

        <b>What kind of auto-confirmation of transactions?</b>
        The bot will automatically confirm the execution of newly completed transactions.

        <b>Note:</b>
        If you select "All items", then the deal of all items will be confirmed, except those specified in the exceptions. If you select "Specified items", then the deal will be confirmed only for those items that you add to the included ones.
    """)
    return txt


def settings_complete_kb():
    config = sett.get("config")
    
    enabled = "🟢 Enabled" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Disabled"
    all = "All items" if config["playerok"]["auto_complete_deals"]["all"] else "Specified items"
    
    auto_complete_deals = sett.get("auto_complete_deals")
    included = len(auto_complete_deals["included"])
    excluded = len(auto_complete_deals["excluded"])
    
    rows = [
        [InlineKeyboardButton(text=f"☑️ Auto-confirm deals: {enabled}", callback_data="switch_auto_complete_deals_enabled")],
        [InlineKeyboardButton(text=f"📦 Confirm deal: {all}", callback_data="switch_auto_complete_deals_all")],
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