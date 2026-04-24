import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from settings import Settings as sett
from .. import callback_datas as calls

def settings_deliv_page_text(index: int):
    auto_deliveries = sett.get('auto_deliveries')
    deliv = auto_deliveries[index]
    piece = deliv.get('piece')
    piece_str = 'Piece by piece' if piece else 'Message'
    keyphrases = '</code>, <code>'.join(deliv.get('keyphrases')) or '❌ Not specified'
    if piece:
        total_goods = len(deliv.get('goods', []))
        part = f'<b>📦 Товары:</b> {total_goods} pcs.'
    else:
        message = '\n'.join(deliv.get('message')) or '❌ Not specified'
        part = f'<b>💬 Сообщение:</b> <blockquote>{message}</blockquote>'
    txt = textwrap.dedent(f'\n        <b>📄🚀 Страница авто-выдачи</b>\n\n        <b>⚡ Тип выдачи:</b> {piece_str}\n        <b>🔑 Ключевые фразы:</b> <code>{keyphrases}</code>\n        \n        {part}\n    ')
    return txt

def settings_deliv_page_kb(index: int, page: int=0):
    auto_deliveries = sett.get('auto_deliveries')
    deliv = auto_deliveries[index]
    piece = deliv.get('piece')
    piece_str = 'Piece by piece' if piece else 'Message'
    keyphrases = ', '.join(deliv.get('keyphrases')) or '❌ Not specified'
    total_goods = len(deliv.get('goods', []))
    message = '\n'.join(deliv.get('message', [])) or '❌ Not specified'
    rows = [[InlineKeyboardButton(text=f'⚡ Delivery type: {piece_str}', callback_data='switch_auto_delivery_piece')], [InlineKeyboardButton(text=f'🔑 Key phrases: {keyphrases}', callback_data='enter_auto_delivery_keyphrases')], [InlineKeyboardButton(text=f'💬 Message: {message}', callback_data='enter_auto_delivery_message') if not piece else InlineKeyboardButton(text=f'📦 Items: {total_goods} pcs. | 👈 Нажми для редактирования', callback_data=calls.DelivGoodsPagination(page=0).pack())], [InlineKeyboardButton(text='🗑️ Delete', callback_data='confirm_deleting_auto_delivery')], [InlineKeyboardButton(text='⬅️ Back', callback_data=calls.AutoDeliveriesPagination(page=page).pack())]]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb

def settings_deliv_page_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>📄🚀 Страница авто-выдачи</b>\n        \n{placeholder}\n    ')
    return txt

def settings_deliv_page_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>📄🚀 Страница авто-выдачи</b>\n        \n{placeholder}\n    ')
    return txt