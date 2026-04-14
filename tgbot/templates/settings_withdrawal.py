import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from playerokapi.types import UserBankCard, SBPBankMember
from settings import Settings as sett

from .. import callback_datas as calls


def settings_withdrawal_text(card: UserBankCard = None, sbp_bank: SBPBankMember = None):
    config = sett.get("config")
    
    enabled = "🟢 Included" if config["playerok"]["auto_withdrawal"]["enabled"] else "🔴 Off"
    interval = config["playerok"]["auto_withdrawal"]["interval"]
    usdt_address = config["playerok"]["auto_withdrawal"]["usdt_address"]
    
    if card: 
        card_name = f"{card.card_first_six}****{card.card_last_four}"
        details = f"{card_name} ({card.card_type.name})"
    elif sbp_bank:
        sbp_phone_number = config["playerok"]["auto_withdrawal"]["sbp_phone_number"]
        details = f"{sbp_phone_number} ({sbp_bank.name})"
    elif usdt_address: 
        details = f"{usdt_address} (USDT TRC20)"
    else: 
        details = "Not indicated"
    
    txt = textwrap.dedent(f"""
        <b>💸 Auto-withdrawal</b>

        <b>🔃 Auto-withdrawal funds:</b> {enabled}
        <b>⏱️ Interval:</b> {interval} sec.

        <b>💳 Details:</b> {details}

        <b>What such auto-conclusion funds?</b>
        Bot will automatically With specified interval create conclusion everyone funds on account By specified details
    """)
    return txt


def settings_withdrawal_kb(card: UserBankCard = None, sbp_bank: SBPBankMember = None):
    config = sett.get("config")
    
    enabled = "🟢 Included" if config["playerok"]["auto_withdrawal"]["enabled"] else "🔴 Off"
    interval = config["playerok"]["auto_withdrawal"]["interval"]
    usdt_address = config["playerok"]["auto_withdrawal"]["usdt_address"]
    
    if card: 
        card_name = f"{card.card_first_six}****{card.card_last_four}"
        details = f"{card_name} ({card.card_type.name})"
    elif sbp_bank:
        sbp_phone_number = config["playerok"]["auto_withdrawal"]["sbp_phone_number"]
        details = f"{sbp_phone_number} ({sbp_bank.name})"
    elif usdt_address: 
        details = f"{usdt_address} (USDT TRC20)"
    else: 
        details = "Not indicated"

    rows = [
        [InlineKeyboardButton(text=f"🔃 Auto-withdrawal funds: {enabled}", callback_data="switch_auto_withdrawal_enabled")],
        [InlineKeyboardButton(text=f"⏱️ Interval: {interval} sec.", callback_data="enter_auto_withdrawal_interval")],
        [InlineKeyboardButton(text=f"💳 Details: {details}", callback_data=calls.BankCardsPagination(page=0).pack())],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_withdrawal_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>💸 Auto-withdrawal</b>
        \n{placeholder}
    """)
    return txt