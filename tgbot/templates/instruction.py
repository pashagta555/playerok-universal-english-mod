import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from .. import callback_datas as calls

def instruction_text():
    txt = textwrap.dedent(f'\n        <b>📖 Инструкция</b>\n    ')
    return txt

def instruction_kb():
    rows = [[InlineKeyboardButton(text='⌨️ Commands', callback_data=calls.InstructionNavigation(to='commands').pack())], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.MenuNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def instruction_comms_text():
    txt = textwrap.dedent(f'\n        <b>⌨️ Команды</b>\n                          \n        ・ <code>!команды</code> — отображает меню с доступными для покупателя командами\n        ・ <code>!продавец</code> — уведомляет и вызывает продавца в диалог с покупателем (пишет вам в Telegram сообщение с просьбой о помощи)\n    ')
    return txt

def instruction_comms_kb():
    rows = [[InlineKeyboardButton(text='⬅️ Back', callback_data=calls.InstructionNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb