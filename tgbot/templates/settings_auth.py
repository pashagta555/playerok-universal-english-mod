import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_auth_text():
    config = sett.get('config')
    cookies = config['playerok']['api']['cookies'][:30] + '*' * 10 or '❌ Not specified'
    user_agent = config['playerok']['api']['user_agent'] or '❌ Not specified'
    txt = textwrap.dedent(f'\n        <b>🔑 Авторизация</b>\n\n        <b>🍪 Cookie-данные:</b> {cookies}\n        <b>🎩 User Agent:</b> {user_agent}\n    ')
    return txt

def settings_auth_kb():
    config = sett.get('config')
    cookies = config['playerok']['api']['cookies'][:30] + '*' * 10 or '❌ Not specified'
    user_agent = config['playerok']['api']['user_agent'] or '❌ Not specified'
    rows = [[InlineKeyboardButton(text=f'🍪 Cookies: {cookies}', callback_data='enter_cookies')], [InlineKeyboardButton(text=f'🎩 User Agent: {user_agent}', callback_data='enter_user_agent')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_auth_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>🔑 Авторизация</b>\n        \n{placeholder}\n    ')
    return txt