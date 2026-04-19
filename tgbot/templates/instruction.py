import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 

from ..import callback_datas as calls 


def instruction_text ():
    txt =textwrap .dedent (f"""
        <b>📖 Инструкция</b>
    """)
    return txt 


def instruction_kb ():
    rows =[
    [InlineKeyboardButton (text ='⌨️ Teams',callback_data =calls .InstructionNavigation (to ='commands').pack ())],
    [InlineKeyboardButton (text ='⬅️ Back',callback_data =calls .MenuNavigation (to ='default').pack ())]
    ]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def instruction_comms_text ():
    txt =textwrap .dedent (f"""
        <b>⌨️ Команды</b>
                          
        ・ <code>!команды</code> — отображает меню с доступными для покупателя командами
        ・ <code>!продавец</code> — уведомляет и вызывает продавца в диалог с покупателем (пишет вам в Telegram сообщение с просьбой о помощи)
    """)
    return txt 


def instruction_comms_kb ():
    rows =[[InlineKeyboardButton (text ='⬅️ Back',callback_data =calls .InstructionNavigation (to ='default').pack ())]]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 