import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 

from settings import Settings as sett 

from ..import callback_datas as calls 


def settings_mess_page_text (message_id :int ):
    messages =sett .get ('messages')

    enabled ='🟢 Included'if messages [message_id ]['enabled']else '🔴 Off'
    message_text ='\n'.join (messages [message_id ]['text'])or '❌ Not specified'

    txt =textwrap .dedent (f"""
        <b>📄💬 Страница сообщения</b>

        <b>🆔 ID сообщения:</b> {message_id }
        <b>💡 Состояние:</b> {enabled }
        <b>💬 Текст сообщения:</b> <blockquote>{message_text }</blockquote>
    """)
    return txt 


def settings_mess_page_kb (message_id :int ,page :int =0 ):
    messages =sett .get ('messages')

    enabled ='🟢 Included'if messages [message_id ]['enabled']else '🔴 Off'
    message_text ='\n'.join (messages [message_id ]['text'])or '❌ Not specified'

    rows =[
    [InlineKeyboardButton (text =f"💡 Состояние: {enabled }",callback_data ='switch_message_enabled')],
    [InlineKeyboardButton (text =f"💬 Текст сообщения: {message_text }",callback_data ='enter_message_text')],
    [InlineKeyboardButton (text ='⬅️ Back',callback_data =calls .MessagesPagination (page =page ).pack ())]
    ]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def settings_mess_page_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""
        <b>📄💬 Страница сообщения</b>
        \n{placeholder }
    """)
    return txt 