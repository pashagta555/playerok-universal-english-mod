The provided code is in Python and uses the aiogram library for building Telegram bots. Here's a translation of the code to English:

```
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime

from settings import Settings as sett

from .. import callback_datas as calls


def logs_text():
    config = sett.get("config")
    max_file_size = config["logs"]["max_file_size"] or "❌ Not set"

    txt = textwrap.dedent(f"""
        <b>🗒️ Logs</b>

        <b>📄 Max file size:</b> {max_file_size} MB

        <b>Note:</b>
        The log file will automatically be cleared as soon as its size exceeds the one set in the config, so it won't take up too much space on your device.
    """)
    return txt


def logs_kb():
    config = sett.get("config")
    max_file_size = config["logs"]["max_file_size"] or "❌ Not set"

    rows = [
        [InlineKeyboardButton(text=f"📄 Max file size: {max_file_size} MB", callback_data="enter_logs_max_file_size")],
        [InlineKeyboardButton(text=f"📔 Get logs", callback_data="select_logs_file_lines")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.MenuNavigation(to="default").pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def logs_file_lines_kb():
    rows = [
        [
            InlineKeyboardButton(text=f"📗 Last 100 lines", callback_data=calls.SendLogsFile(lines=100).pack()),
            InlineKeyboardButton(text=f"📘 Last 250 lines", callback_data=calls.SendLogsFile(lines=250).pack())
        ],
        [
            InlineKeyboardButton(text=f"📕 Last 1000 lines", callback_data=calls.SendLogsFile(lines=1000).pack()),
            InlineKeyboardButton(text=f"📖 Entire file", callback_data=calls.SendLogsFile(lines=-1).pack())
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
```

Note that the `❌` symbol is likely being used to represent a red circle with a line through it, indicating "not set" or "not available".

