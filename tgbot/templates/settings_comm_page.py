import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 

from settings import Settings as sett 

from ..import callback_datas as calls 


def settings_comm_page_text (command :str ):
    custom_commands =sett .get ("custom_commands")
    command_text ="\n".join (custom_commands [command ])or "Not set"

    txt =textwrap .dedent (f"""
        <b>📄❗ Страница команды</b>

        <b>⌨️ Команда:</b> {command }
        <b>💬 Ответ:</b> <blockquote>{command_text }</blockquote>
    """)
    return txt 


def settings_comm_page_kb (command :str ,page :int =0 ):
    custom_commands =sett .get ("custom_commands")
    command_text ="\n".join (custom_commands [command ])or "Not Set"

    rows =[
    [InlineKeyboardButton (text =f"💬 Ответ: {command_text }",callback_data ="enter_custom_command_answer")],
    [InlineKeyboardButton (text ="Delete",callback_data ="confirm_deleting_custom_command")],
    [InlineKeyboardButton (text ="Backwards ⬅️",callback_data =calls .CustomCommandsPagination (page =page ).pack ())]
    ]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def settings_comm_page_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""
        <b>📄❗ Страница команды</b>
        \n{placeholder }
    """)
    return txt 