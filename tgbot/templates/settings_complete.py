import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_complete_text():
    config = sett.get('config')
    enabled = '🟢 Included' if config['playerok']['auto_complete_deals']['enabled'] else '🔴 Off'
    all = 'Всех items' if config['playerok']['auto_complete_deals']['all'] else 'Указанных items'
    auto_complete_deals = sett.get('auto_complete_deals')
    included = len(auto_complete_deals['included'])
    excluded = len(auto_complete_deals['excluded'])
    txt = textwrap.dedent(f'\n        <b>☑️ Авто-подтверждение</b>\n\n        <b>☑️ Авто-подтверждение сделок:</b> {enabled}\n        <b>📦 Подтверждать сделки:</b> {all}\n\n        <b>➕ Включенные:</b> {included}\n        <b>➖ Исключенные:</b> {excluded}\n\n        <b>Что за авто-подтверждение сделок?</b>\n        Бот будет автоматически подтверждать выполнение только что оформленных сделок.\n\n        <b>Примечание:</b>\n        Если вы выберете "Всех предметов", то будут подтверждаться сделки всех предметов, кроме тех, что указаны в исключениях. Если вы выберете "Указанных предметов", то будут подтверждаться сделки только тех товаров, которые вы добавите во включенные.\n    ')
    return txt

def settings_complete_kb():
    config = sett.get('config')
    enabled = '🟢 Included' if config['playerok']['auto_complete_deals']['enabled'] else '🔴 Off'
    all = 'Всех items' if config['playerok']['auto_complete_deals']['all'] else 'Указанных items'
    auto_complete_deals = sett.get('auto_complete_deals')
    included = len(auto_complete_deals['included'])
    excluded = len(auto_complete_deals['excluded'])
    rows = [[InlineKeyboardButton(text=f'☑️ Auto-confirmation deals: {enabled}', callback_data='switch_auto_complete_deals_enabled')], [InlineKeyboardButton(text=f'📦 Confirm deals: {all}', callback_data='switch_auto_complete_deals_all')], [InlineKeyboardButton(text=f'➕ Included: {included}', callback_data=calls.IncludedCompleteDealsPagination(page=0).pack()), InlineKeyboardButton(text=f'➖ Excluded: {excluded}', callback_data=calls.ExcludedCompleteDealsPagination(page=0).pack())], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_complete_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>☑️ Авто-подтверждение</b>\n        \n{placeholder}\n    ')
    return txt