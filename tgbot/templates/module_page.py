import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from uuid import UUID
from core.modules import Module, get_module_by_uuid
from .. import callback_datas as calls

def module_page_text(module_uuid: UUID):
    module: Module = get_module_by_uuid(module_uuid)
    if not module:
        raise Exception('Could not find module')
    txt = textwrap.dedent(f"\n        <b>📄🔌 Страница модуля</b>\n\n        <b>Модуль</b> <code>{module.meta.name}</code>:          \n        ・ UUID: <b>{module.uuid}</b>\n        ・ Версия: <b>{module.meta.version}</b>\n        ・ Описание: <blockquote>{module.meta.description}</blockquote>\n        ・ Авторы: <b>{module.meta.authors}</b>\n        ・ Ссылки: <b>{module.meta.links}</b>\n\n        🔌 <b>Состояние:</b> {('🟢 Включен' if module.enabled else '🔴 Выключен')}\n    ")
    return txt

def module_page_kb(module_uuid: UUID, page: int=0):
    module: Module = get_module_by_uuid(module_uuid)
    if not module:
        raise Exception('Could not find module')
    rows = [[InlineKeyboardButton(text='🔴 Turn off module' if module.enabled else '🟢 Enable module', callback_data='switch_module_enabled')], [InlineKeyboardButton(text='♻️ Reboot', callback_data='reload_module')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.ModulesPagination(page=page).pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def module_page_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>🔧 Управление модулем</b>\n        \n{placeholder}\n    ')
    return txt