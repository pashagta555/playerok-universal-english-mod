import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_other_text():
    config = sett.get('config')
    switch_read_chat_enabled = '🟢 Included' if config['playerok']['read_chat']['enabled'] else '🔴 Off'
    custom_commands_enabled = '🟢 Included' if config['playerok']['custom_commands']['enabled'] else '🔴 Off'
    auto_deliveries_enabled = '🟢 Included' if config['playerok']['auto_deliveries']['enabled'] else '🔴 Off'
    watermark_enabled = '🟢 Included' if config['playerok']['watermark']['enabled'] else '🔴 Off'
    watermark_value = config['playerok']['watermark']['value'] or '❌ Not specified'
    txt = textwrap.dedent(f'\n        <b>🔧 Прочее</b>\n\n        <b>👀 Чтение чата перед отправкой сообщения:</b> {switch_read_chat_enabled}\n        <b>❗ Команды:</b> {custom_commands_enabled}\n        <b>🚀 Авто-выдача:</b> {auto_deliveries_enabled}\n        \n        <b>©️ Водяной знак под сообщениями:</b> {watermark_enabled}\n        <b>✍️©️ Водяной знак:</b> {watermark_value}\n    ')
    return txt

def settings_other_kb():
    config = sett.get('config')
    switch_read_chat_enabled = '🟢 Included' if config['playerok']['read_chat']['enabled'] else '🔴 Off'
    custom_commands_enabled = '🟢 Included' if config['playerok']['custom_commands']['enabled'] else '🔴 Off'
    auto_deliveries_enabled = '🟢 Included' if config['playerok']['auto_deliveries']['enabled'] else '🔴 Off'
    watermark_enabled = '🟢 Included' if config['playerok']['watermark']['enabled'] else '🔴 Off'
    watermark_value = config['playerok']['watermark']['value'] or '❌ Not specified'
    rows = [[InlineKeyboardButton(text=f'👀 Reading a chat before sending a message: {switch_read_chat_enabled}', callback_data='switch_read_chat_enabled')], [InlineKeyboardButton(text=f'❗ Commands: {custom_commands_enabled}', callback_data='switch_custom_commands_enabled')], [InlineKeyboardButton(text=f'🚀 Auto-delivery: {auto_deliveries_enabled}', callback_data='switch_auto_deliveries_enabled')], [InlineKeyboardButton(text=f'©️ Watermark under messages: {watermark_enabled}', callback_data='switch_watermark_enabled')], [InlineKeyboardButton(text=f'✍️©️ Watermark: {watermark_value}', callback_data='enter_watermark_value')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_other_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>🔧 Прочее</b>\n        \n{placeholder}\n    ')
    return txt