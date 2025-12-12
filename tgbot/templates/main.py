import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .. import callback_datas as calls


def error_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>❌ An error occurred </b>

        <blockquote>{placeholder}</blockquote>
    """)
    return txt


def back_kb(cb: str):
    rows = [[InlineKeyboardButton(text="⬅️ Back", callback_data=cb)]]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def confirm_kb(confirm_cb: str, cancel_cb: str):
    rows = [[
        InlineKeyboardButton(text="✅ Confirm", callback_data=confirm_cb),
        InlineKeyboardButton(text="❌ Cancel", callback_data=cancel_cb)
    ]]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def destroy_kb():
    rows = [[InlineKeyboardButton(text="❌ Close", callback_data="destroy")]]
    return InlineKeyboardMarkup(inline_keyboard=rows)


def do_action_text(placeholder: str):
    txt = textwrap.dedent(f"""
        🧩 <b>Action</b>
        \n{placeholder}
    """)
    return txt


def log_text(title: str, text: str, by: str = "playerokuniversal"):
    txt = textwrap.dedent(f"""
        <b>{title}</b>
        \n{text}
        \n<i>{by}</i>
    """)
    return txt


def log_new_mess_kb(username: str):
    rows = [[InlineKeyboardButton(text="💬 Write", callback_data=calls.RememberUsername(name=username, do="send_mess").pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def log_new_deal_kb(username: str, deal_id: str):
    rows = [
        [
        InlineKeyboardButton(text="💬 Write", callback_data=calls.RememberUsername(name=username, do="send_mess").pack()),
        InlineKeyboardButton(text="☑️ Completed", callback_data=calls.RememberDealId(de_id=deal_id, do="complete").pack()),
        InlineKeyboardButton(text="📦 Refund", callback_data=calls.RememberDealId(de_id=deal_id, do="refund").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def log_new_review_kb(username: str, deal_id: str):
    rows = [
        [
        InlineKeyboardButton(text="💬🌟 Reply to Review", callback_data=calls.RememberDealId(de_id=deal_id, do="answer_rev").pack()),
        InlineKeyboardButton(text="💬 Write", callback_data=calls.RememberUsername(name=username, do="send_mess").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def sign_text(placeholder: str):
    txt = textwrap.dedent(f"""
        🔐 <b>Authorization</b>
        \n{placeholder}
    """)
    return txt


def call_seller_text(calling_name, chat_link):
    txt = textwrap.dedent(f"""
        🆘 <b>{calling_name}</b> needs your help!
        {chat_link}
    """)
    return txt