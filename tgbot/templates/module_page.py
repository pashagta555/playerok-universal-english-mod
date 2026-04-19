import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 
from uuid import UUID 

from core .modules import Module ,get_module_by_uuid 

from ..import callback_datas as calls 


def module_page_text (module_uuid :UUID ):
    module :Module =get_module_by_uuid (module_uuid )
    if not module :
        raise Exception ("Couldn't find the module")

    txt =textwrap .dedent (f"""
        <b>📄🔌 Страница модуля</b>

        <b>Модуль</b> <code>{module .meta .name }</code>:          
        ・ UUID: <b>{module .uuid }</b>
        ・ Версия: <b>{module .meta .version }</b>
        ・ Описание: <blockquote>{module .meta .description }</blockquote>
        ・ Авторы: <b>{module .meta .authors }</b>
        ・ Ссылки: <b>{module .meta .links }</b>

        🔌 <b>Состояние:</b> {'Enabled'if module .enabled else 'Disabled'}
    """)
    return txt 


def module_page_kb (module_uuid :UUID ,page :int =0 ):
    module :Module =get_module_by_uuid (module_uuid )
    if not module :
        raise Exception ("Could not find the module")

    rows =[
    [InlineKeyboardButton (text ="Turn off the module 🔴"if module .enabled else "Enable module",callback_data ="switch_module_enabled")],
    [InlineKeyboardButton (text ="Reload",callback_data ="reload_module")],
    [InlineKeyboardButton (text ="Backwards",callback_data =calls .ModulesPagination (page =page ).pack ())]
    ]
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def module_page_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""
        <b>🔧 Управление модулем</b>
        \n{placeholder }
    """)
    return txt 