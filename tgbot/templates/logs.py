import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
from settings import Settings as sett
from .. import callback_datas as calls

def logs_text():
    config = sett.get('config')
    max_file_size = config['logs']['max_file_size'] or '❌ Not specified'
    txt = textwrap.dedent(f'\n        <b>🗒️ Логи</b>\n\n        <b>📄 Макс. размер файла:</b> {max_file_size} MB\n\n        <b>Примечание:</b>\n        Файл логов будет автоматически очищаться, как только его размер превысит указанный в конфиге, чтобы не занимать много места на вашем устройстве.\n    ')
    return txt

def logs_kb():
    config = sett.get('config')
    max_file_size = config['logs']['max_file_size'] or '❌ Not specified'
    rows = [[InlineKeyboardButton(text=f'📄 Макс. размер файла: {max_file_size} MB', callback_data='enter_logs_max_file_size')], [InlineKeyboardButton(text=f'📔 Get logs', callback_data='select_logs_file_lines')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def logs_file_lines_kb():
    rows = [[InlineKeyboardButton(text=f'📗 Last 100 lines', callback_data=calls.SendLogsFile(lines=100).pack()), InlineKeyboardButton(text=f'📘 Last 250 lines', callback_data=calls.SendLogsFile(lines=250).pack())], [InlineKeyboardButton(text=f'📕 Last 1000 lines', callback_data=calls.SendLogsFile(lines=1000).pack()), InlineKeyboardButton(text=f'📖 Entire file', callback_data=calls.SendLogsFile(lines=-1).pack())], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to='logs').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def logs_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>🗒️ Логи</b>\n        \n{placeholder}\n    ')
    return txt