import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls
    

def settings_other_text():
    config = sett.get("config")
    switch_read_chat_enabled = "🟢 Enabled" if config["playerok"]["read_chat"]["enabled"] else "🔴 Disabled"
    auto_complete_deals_enabled = "🟢 Enabled" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Disabled"
    custom_commands_enabled = "🟢 Enabled" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Disabled"
    auto_deliveries_enabled = "🟢 Enabled" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Disabled"
    watermark_enabled = "🟢 Enabled" if config["playerok"]["watermark"]["enabled"] else "🔴 Disabled"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Not set"
    txt = textwrap.dedent(f"""
        <b>🔧 Other</b>

        <b>👀 Read chat before sending message:</b> {switch_read_chat_enabled}
        <b>☑️ Auto-confirm orders:</b> {auto_complete_deals_enabled}
        <b>⌨️ Custom commands:</b> {custom_commands_enabled}
        <b>🚀 Auto-delivery:</b> {auto_deliveries_enabled}
        
        <b>©️ Watermark under messages:</b> {watermark_enabled}
        <b>✍️©️ Watermark:</b> {watermark_value}
    """)
    return txt


def settings_other_kb():
    config = sett.get("config")
    switch_read_chat_enabled = "🟢 Enabled" if config["playerok"]["read_chat"]["enabled"] else "🔴 Disabled"
    auto_complete_deals_enabled = "🟢 Enabled" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Disabled"
    custom_commands_enabled = "🟢 Enabled" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Disabled"
    auto_deliveries_enabled = "🟢 Enabled" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Disabled"
    watermark_enabled = "🟢 Enabled" if config["playerok"]["watermark"]["enabled"] else "🔴 Disabled"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Not set"
    rows = [
        [InlineKeyboardButton(text=f"👀 Read chat before sending message: {switch_read_chat_enabled}", callback_data="switch_read_chat_enabled")],
        [InlineKeyboardButton(text=f"☑️ Auto-confirm orders: {auto_complete_deals_enabled}", callback_data="switch_auto_complete_deals_enabled")],
        [InlineKeyboardButton(text=f"⌨️ Custom commands: {custom_commands_enabled}", callback_data="switch_custom_commands_enabled")],
        [InlineKeyboardButton(text=f"🚀 Auto-delivery: {auto_deliveries_enabled}", callback_data="switch_auto_deliveries_enabled")],
        [InlineKeyboardButton(text=f"©️ Watermark under messages: {watermark_enabled}", callback_data="switch_watermark_enabled")],
        [InlineKeyboardButton(text=f"✍️©️ Watermark: {watermark_value}", callback_data="enter_watermark_value")],
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