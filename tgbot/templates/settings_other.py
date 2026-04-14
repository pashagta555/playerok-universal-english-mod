import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls
    

def settings_other_text():
    config = sett.get("config")
    
    switch_read_chat_enabled = "🟢 Included" if config["playerok"]["read_chat"]["enabled"] else "🔴 Off"
    custom_commands_enabled = "🟢 Included" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Off"
    auto_deliveries_enabled = "🟢 Included" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Off"
    watermark_enabled = "🟢 Included" if config["playerok"]["watermark"]["enabled"] else "🔴 Off"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Not given"
    
    txt = textwrap.dedent(f"""
        <b>🔧 Other</b>

        <b>👀 Reading chat before sending messages:</b> {switch_read_chat_enabled}
        <b>❗ Teams:</b> {custom_commands_enabled}
        <b>🚀 Auto-issuance:</b> {auto_deliveries_enabled}
        
        <b>©️ Water sign under messages:</b> {watermark_enabled}
        <b>✍️©️ Water sign:</b> {watermark_value}
    """)
    return txt


def settings_other_kb():
    config = sett.get("config")
    
    switch_read_chat_enabled = "🟢 Included" if config["playerok"]["read_chat"]["enabled"] else "🔴 Off"
    custom_commands_enabled = "🟢 Included" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Off"
    auto_deliveries_enabled = "🟢 Included" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Off"
    watermark_enabled = "🟢 Included" if config["playerok"]["watermark"]["enabled"] else "🔴 Off"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Not given"
    
    rows = [
        [InlineKeyboardButton(text=f"👀 Reading chat before sending messages: {switch_read_chat_enabled}", callback_data="switch_read_chat_enabled")],
        [InlineKeyboardButton(text=f"❗ Teams: {custom_commands_enabled}", callback_data="switch_custom_commands_enabled")],
        [InlineKeyboardButton(text=f"🚀 Auto-issuance: {auto_deliveries_enabled}", callback_data="switch_auto_deliveries_enabled")],
        [InlineKeyboardButton(text=f"©️ Water sign under messages: {watermark_enabled}", callback_data="switch_watermark_enabled")],
        [InlineKeyboardButton(text=f"✍️©️ Water sign: {watermark_value}", callback_data="enter_watermark_value")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_other_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>🔧 Other</b>
        \n{placeholder}
    """)
    return txt