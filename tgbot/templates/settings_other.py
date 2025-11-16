import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from settings import Settings as sett

from .. import callback_datas as calls
    

def settings_other_text():
    config = sett.get("config")
    switch_read_chat_enabled = "🟢 Turned on" if config["playerok"]["read_chat"]["enabled"] else "🔴 Turned off"
    auto_complete_deals_enabled = "🟢 Turned on" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Turned off"
    custom_commands_enabled = "🟢 Turned on" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Turned off"
    auto_deliveries_enabled = "🟢 Turned on" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Turned off"
    watermark_enabled = "🟢 Turned on" if config["playerok"]["watermark"]["enabled"] else "🔴 Turned off"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Не задано"
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → ⌨️ Other</b>

        👀 <b>Reading of the chat before sending:</b> {switch_read_chat_enabled}
        ☑️ <b>Auto confirm orders:</b> {auto_complete_deals_enabled}
        ⌨️ <b>User commands:</b> {custom_commands_enabled}
        🚀 <b>Auto-delivery:</b> {auto_deliveries_enabled}
        ©️ <b>Watermark under messages:</b> {watermark_enabled}
        ✍️©️ <b>Watermark:</b> {watermark_value}

        Select paramettre to be changed ↓
    """)
    return txt


def settings_other_kb():
    config = sett.get("config")
    switch_read_chat_enabled = "🟢 Turned on" if config["playerok"]["read_chat"]["enabled"] else "🔴 Turned off"
    auto_complete_deals_enabled = "🟢 Turned on" if config["playerok"]["auto_complete_deals"]["enabled"] else "🔴 Turned off"
    custom_commands_enabled = "🟢 Turned on" if config["playerok"]["custom_commands"]["enabled"] else "🔴 Turned off"
    auto_deliveries_enabled = "🟢 Turned on" if config["playerok"]["auto_deliveries"]["enabled"] else "🔴 Turned off"
    watermark_enabled = "🟢 Turned on" if config["playerok"]["watermark"]["enabled"] else "🔴 Turned off"
    watermark_value = config["playerok"]["watermark"]["value"] or "❌ Не задано"
    rows = [
        [InlineKeyboardButton(text=f"👀 Reading the chat before sending message: {switch_read_chat_enabled}", callback_data="switch_read_chat_enabled")],
        [InlineKeyboardButton(text=f"☑️ Auto confirm orders: {auto_complete_deals_enabled}", callback_data="switch_auto_complete_deals_enabled")],
        [InlineKeyboardButton(text=f"⌨️ User commands: {custom_commands_enabled}", callback_data="switch_custom_commands_enabled")],
        [InlineKeyboardButton(text=f"🚀 Autodelivery: {auto_deliveries_enabled}", callback_data="switch_auto_deliveries_enabled")],
        [InlineKeyboardButton(text=f"©️ Watermark under messages: {watermark_enabled}", callback_data="switch_watermark_enabled")],
        [InlineKeyboardButton(text=f"✍️©️ Watermark: {watermark_value}", callback_data="enter_watermark_value")],
        [
        InlineKeyboardButton(text="⬅️ Back", callback_data=calls.SettingsNavigation(to="default").pack()),
        InlineKeyboardButton(text="🔄️ Update", callback_data=calls.SettingsNavigation(to="other").pack())
        ]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def settings_other_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        ⚙️ <b>Settings → ⌨️ Other</b>
        \n{placeholder}
    """)
    return txt
