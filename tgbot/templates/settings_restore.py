import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_restore_text():
    config = sett.get('config')
    auto_restore_items_sold = '🟢 Included' if config['playerok']['auto_restore_items']['sold'] else '🔴 Off'
    auto_restore_items_expired = '🟢 Included' if config['playerok']['auto_restore_items']['expired'] else '🔴 Off'
    auto_restore_items_all = 'All items' if config['playerok']['auto_restore_items']['all'] else 'Specified items'
    auto_restore_items = sett.get('auto_restore_items')
    auto_restore_items_included = len(auto_restore_items['included'])
    auto_restore_items_excluded = len(auto_restore_items['excluded'])
    txt = textwrap.dedent(f'\n        <b>♻️ Авто-восстановление</b>\n\n        <b>♻️ Авто-восстановление предметов:</b>\n        <b>・ Проданные:</b> {auto_restore_items_sold}\n        <b>・ Истёкшие:</b> {auto_restore_items_expired}\n\n        <b>📦 Восстанавливать:</b> {auto_restore_items_all}\n\n        <b>➕ Включенные:</b> {auto_restore_items_included}\n        <b>➖ Исключенные:</b> {auto_restore_items_excluded}\n\n        <b>Что за авто-восстановление предметов?</b>\n        Эта функция позволит автоматически восстанавливать (заново выставлять) предмет, который только что купили или который истёк, чтобы он снова был на продаже. Предмет будет выставлен с тем же статусом приоритета, что и был раньше.\n\n        <b>Примечание:</b>\n        Если вы выберете "Все предметы", то будут восстанавливаться все товары, кроме тех, что указаны в исключениях. Если вы выберете "Указанные предметы", то будут восстанавливаться только те товары, которые вы добавите во включенные.\n    ')
    return txt

def settings_restore_kb():
    config = sett.get('config')
    auto_restore_items_sold = '🟢 Included' if config['playerok']['auto_restore_items']['sold'] else '🔴 Off'
    auto_restore_items_expired = '🟢 Included' if config['playerok']['auto_restore_items']['expired'] else '🔴 Off'
    auto_restore_items_all = 'All items' if config['playerok']['auto_restore_items']['all'] else 'Specified items'
    auto_restore_items = sett.get('auto_restore_items')
    auto_restore_items_included = len(auto_restore_items['included'])
    auto_restore_items_excluded = len(auto_restore_items['excluded'])
    rows = [[InlineKeyboardButton(text=f'🛒 Sold: {auto_restore_items_sold}', callback_data='switch_auto_restore_items_sold')], [InlineKeyboardButton(text=f'⏰ Wanted: {auto_restore_items_expired}', callback_data='switch_auto_restore_items_expired')], [InlineKeyboardButton(text=f'📦 Restore: {auto_restore_items_all}', callback_data='switch_auto_restore_items_all')], [InlineKeyboardButton(text=f'➕ Included: {auto_restore_items_included}', callback_data=calls.IncludedRestoreItemsPagination(page=0).pack()), InlineKeyboardButton(text=f'➖ Excluded: {auto_restore_items_excluded}', callback_data=calls.ExcludedRestoreItemsPagination(page=0).pack())], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.SettingsNavigation(to='default').pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_restore_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>♻️ Автор-восстановление</b>\n        \n{placeholder}\n    ')
    return txt