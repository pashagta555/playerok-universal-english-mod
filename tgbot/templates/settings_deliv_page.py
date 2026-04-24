import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 

from settings import Settings as sett 

from ..import callback_datas as calls 


def settings_deliv_page_text (index :int ):
    auto_deliveries =sett .get ("auto_deliveries")
    deliv =auto_deliveries [index ]

    piece =deliv .get ("piece")
    piece_str ='Piece by piece'if piece else 'Message'
    keyphrases ="</code>, <code>".join (deliv .get ("keyphrases"))or '❌ Not specified'

    if piece :
        total_goods =len (deliv .get ("goods",[]))
        part =f"<b>📦 Products:</b>{total_goods }pcs."
    else :
        message ="\n".join (deliv .get ("message"))or '❌ Not specified'
        part =f"<b>💬 Message:</b> <blockquote>{message }</blockquote>"

    txt =textwrap .dedent (f"""<b>📄🚀 Auto-issue page</b>

        <b>⚡ Issue type:</b>{piece_str }<b>🔑 Key phrases:</b> <code>{keyphrases }</code>
        
        {part }
    """)
    return txt 


def settings_deliv_page_kb (index :int ,page :int =0 ):
    auto_deliveries =sett .get ("auto_deliveries")
    deliv =auto_deliveries [index ]

    piece =deliv .get ("piece")
    piece_str ='Piece by piece'if piece else 'Message'
    keyphrases =", ".join (deliv .get ("keyphrases"))or '❌ Not specified'

    total_goods =len (deliv .get ("goods",[]))
    message ="\n".join (deliv .get ("message",[]))or '❌ Not specified'

    rows =[
    [InlineKeyboardButton (text =f"⚡ Issue type:{piece_str }",callback_data ="switch_auto_delivery_piece")],
    [InlineKeyboardButton (text =f"🔑 Key phrases:{keyphrases }",callback_data ="enter_auto_delivery_keyphrases")],
    [
    InlineKeyboardButton (text =f"💬 Message:{message }",callback_data ="enter_auto_delivery_message")
    if not piece else InlineKeyboardButton (text =f"📦 Products:{total_goods }pcs. | 👈 Click to edit",callback_data =calls .DelivGoodsPagination (page =0 ).pack ())
    ],
    [InlineKeyboardButton (text ='🗑️ Delete',callback_data ="confirm_deleting_auto_delivery")],
    [InlineKeyboardButton (text ='⬅️ Back',callback_data =calls .AutoDeliveriesPagination (page =page ).pack ())]
    ]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def settings_deliv_page_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""<b>📄🚀 Auto-issue page</b>
        \n{placeholder }
    """)
    return txt 


def settings_deliv_page_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""<b>📄🚀 Auto-issue page</b>
        \n{placeholder }
    """)
    return txt 