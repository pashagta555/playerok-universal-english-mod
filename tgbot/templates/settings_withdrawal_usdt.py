import textwrap

def settings_withdrawal_usdt_float_text(placeholder: str):
    txt = textwrap.dedent(f'\n        <b>💲 USDT (TRC20)</b>\n        \n{placeholder}\n    ')
    return txt