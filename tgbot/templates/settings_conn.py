import textwrap 
from aiogram .types import InlineKeyboardMarkup ,InlineKeyboardButton 

from settings import Settings as sett 

from ..import callback_datas as calls 


def settings_conn_text ():
    config =sett .get ("config")

    pl_proxy =config ["playerok"]["api"]["proxy"]or '❌ Not specified'
    tg_proxy =config ["telegram"]["api"]["proxy"]or '❌ Not specified'
    requests_timeout =config ["playerok"]["api"]["requests_timeout"]or '❌ Not specified'

    txt =textwrap .dedent (f"""<b>📶 Connection</b>

        <b>🌐 Proxy for Playerok:</b>{pl_proxy }<b>🌐 Proxy for Telegram:</b>{tg_proxy }<b>🛜 Connection timeout to playerok.com:</b>{requests_timeout }<b>What is the connection timeout to playerok.com?</b>
        This is the maximum time within which a response to a request from the Playerok website should arrive. If the time has expired and the answer has not arrived, the bot will throw an error. If you have a weak Internet, specify a higher value""")
    return txt 


def settings_conn_kb ():
    config =sett .get ("config")

    pl_proxy =config ["playerok"]["api"]["proxy"]or '❌ Not specified'
    tg_proxy =config ["telegram"]["api"]["proxy"]or '❌ Not specified'
    requests_timeout =config ["playerok"]["api"]["requests_timeout"]or '❌ Not specified'

    rows =[
    [InlineKeyboardButton (text =f"🌐 Proxy for Playerok:{pl_proxy }",callback_data ="enter_pl_proxy")],
    [InlineKeyboardButton (text =f"🌐 Proxy for Telegram:{tg_proxy }",callback_data ="enter_tg_proxy")],
    [InlineKeyboardButton (text =f"🛜 Connection timeout to playerok.com:{requests_timeout }",callback_data ="enter_playerokapi_requests_timeout")],
    [InlineKeyboardButton (text ='⬅️ Back',callback_data =calls .SettingsNavigation (to ="default").pack ())]
    ]
    if config ["playerok"]["api"]["proxy"]:
        rows [0 ].append (InlineKeyboardButton (text =f"❌ Remove proxy",callback_data ="clean_pl_proxy"))
    if config ["telegram"]["api"]["proxy"]:
        rows [1 ].append (InlineKeyboardButton (text =f"❌ Remove proxy",callback_data ="clean_tg_proxy"))
    kb =InlineKeyboardMarkup (inline_keyboard =rows )
    return kb 


def settings_conn_float_text (placeholder :str ):
    txt =textwrap .dedent (f"""<b>📶 Connection</b>
        \n{placeholder }
    """)
    return txt 