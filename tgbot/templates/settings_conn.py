import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_conn_text():
    config = sett.get('config')
    pl_proxy = config['playerok']['api']['proxy'] or '❌ Not specified'
    tg_proxy = config['telegram']['api']['proxy'] or '❌ Not specified'
    requests_timeout = config['playerok']['api']['requests_timeout'] or '❌ Not specified'
    txt = textwrap.dedent(f'\n        <b>📶 Соединение</b>\n\n        <b>🌐 Прокси для Playerok:</b> {pl_proxy}\n        <b>🌐 Прокси для Telegram:</b> {tg_proxy}\n\n        <b>🛜 Таймаут подключения к playerok.com:</b> {requests_timeout}\n\n        <b>Что за таймаут подключения к playerok.com?</b>\n        Это максимальное время, за которое должен прийти ответ на запрос с сайта Playerok. Если время истекло, а ответ не пришёл — бот выдаст ошибку. Если у вас слабый интернет, указывайте значение больше\n    ')
    return txt

def settings_conn_kb():
    config = sett.get('config')
    pl_proxy = config['playerok']['api']['proxy'] or '❌ Not specified'
    tg_proxy = config['telegram']['api']['proxy'] or '❌ Not specified'
    requests_timeout = config['playerok']['api']['requests_timeout'] or '❌ Not specified'
    rows = [[InlineKeyboardButton(text=f'🌐 Proxy for Playerok: {pl_proxy}', callback_data='enter_pl_proxy')], [InlineKeyboardButton(text=f'🌐 Proxy for Telegram: {tg_proxy}', callback_data='enter_tg_proxy')], [InlineKeyboardButton(text=f'🛜 Таймаут подключения к playerok.com: {requests_timeout}', callback_data='enter_playerokapi_requests_timeout')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to='default').pack())]]
    if config['playerok']['api']['proxy']:
        rows[0].append(InlineKeyboardButton(text=f'❌ Remove proxy', callback_data='clean_pl_proxy'))
    if config['telegram']['api']['proxy']:
        rows[1].append(InlineKeyboardButton(text=f'❌ Remove proxy', callback_data='clean_tg_proxy'))
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_conn_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>📶 Соединение</b>\n        \n{placeholder}\n    ')
    return txt