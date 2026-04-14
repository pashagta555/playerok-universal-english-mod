import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from settings import Settings as sett

from .. import callback_datas as calls


def logs_text():
    config = sett.get("config")
    max_file_size = config["logs"]["max_file_size"] or "❌ Not given"
    
    txt = textwrap.dedent(f"""
        <b>🗒️ Logs</b>

        <b>📄 Max. size file:</b> {max_file_size} MB

        <b>Note:</b>
        File lairs will automatically cleanse, How only his size will exceed specified V config, to Not occupy many places on yours device.
    """)
    return txt


def logs_kb():
    config = sett.get("config")
    max_file_size = config["logs"]["max_file_size"] or "❌ Not given"

    rows = [
        [InlineKeyboardButton(text=f"📄 Max. size file: {max_file_size} MB", callback_data="enter_logs_max_file_size")],
        [InlineKeyboardButton(text=f"📔 Get logs", callback_data="select_logs_file_lines")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def logs_file_lines_kb():
    rows = [
        [
        InlineKeyboardButton(text=f"📗 Latest 100 lines", callback_data=calls.SendLogsFile(lines=100).pack()),
        InlineKeyboardButton(text=f"📘 Latest 250 lines", callback_data=calls.SendLogsFile(lines=250).pack())
        ],
        [
        InlineKeyboardButton(text=f"📕 Latest 1000 lines", callback_data=calls.SendLogsFile(lines=1000).pack()),
        InlineKeyboardButton(text=f"📖 All file", callback_data=calls.SendLogsFile(lines=-1).pack())
        ],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="logs").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def logs_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>🗒️ Logs</b>
        \n{placeholder}
    """)
    return txt