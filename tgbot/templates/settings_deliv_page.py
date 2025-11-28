import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls


def settings_deliv_page_text(index: int):
    auto_deliveries = sett.get("auto_deliveries")
    keyphrases = "</code>, <code>".join(auto_deliveries[index].get("keyphrases")) or "❌ Not set"
    message = "\n".join(auto_deliveries[index].get("message")) or "❌ Not set"
    txt = textwrap.dedent(f"""
        ✏️ <b>Editing auto-delivery</b>

        🔑 <b>Keyphrases:</b> <code>{keyphrases}</code>
        💬 <b>Message:</b> <blockquote>{message}</blockquote>

        Select parameter to change ↓
    """)
    return txt


def settings_deliv_page_kb(index: int, page: int = 0):
    auto_deliveries = sett.get("auto_deliveries")
    keyphrases = ", ".join(auto_deliveries[index].get("keyphrases")) or "❌ Not set"
    message = "\n".join(auto_deliveries[index].get("message")) or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"🔑 Keyphrases: {keyphrases}", callback_data="enter_auto_delivery_keyphrases")],
        [InlineKeyboardButton(text=f"💬 Message: {message}", callback_data="enter_auto_delivery_message")],
        [InlineKeyboardButton(text="🗑️ Delete auto-delivery", callback_data="confirm_deleting_auto_delivery")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.AutoDeliveriesPagination(page=page).pack()), 
        InlineKeyboardButton(text="🔄️ Refresh", callback_data=calls.AutoDeliveryPage(index=index).pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_deliv_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ✏️ <b>Editing auto-delivery</b>
        \n{placeholder}
    """)
    return txt