Here is the translation of the provided Python code to English:

```
import textwrap
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from uuid import UUID

from core.modules import Module, get_module_by_uuid

from .. import callback_datas as calls


def module_page_text(module_uuid: UUID):
    module: Module = get_module_by_uuid(module_uuid)
    if not module:
        raise Exception("Module not found")

    txt = textwrap.dedent(f"""
        <b>💻🔌 Module page</b>

        <b>Module</b> <code>{module.meta.name}</code>:          
        ・ UUID: <b>{module.uuid}</b>
        ・ Version: <b>{module.meta.version}</b>
        ・ Description: <blockquote>{module.meta.description}</blockquote>
        ・ Authors: <b>{module.meta.authors}</b>
        ・ Links: <b>{module.meta.links}</b>

        🔌 <b>Status:</b> {'🟢 Enabled' if module.enabled else '🔴 Disabled'}
    """)
    return txt


def module_page_kb(module_uuid: UUID, page: int = 0):
    module: Module = get_module_by_uuid(module_uuid)
    if not module:
        raise Exception("Module not found")

    rows = [
        [InlineKeyboardButton(text="🔴 Disable module" if module.enabled else "🟢 Enable module", callback_data="switch_module_enabled")],
        [InlineKeyboardButton(text="♻️ Reload", callback_data="reload_module")],
        [InlineKeyboardButton(text="⬅️ Back", callback_data=calls.ModulesPagination(page=page).pack())]
    ]
    kb = InlineKeyboardMarkup(inline_keyboard=rows)
    return kb


def module_page_float_text(placeholder: str):
    txt = textwrap.dedent(f"""
        <b>🔧 Module control</b>
        \n{placeholder}
    """)
    return txt
```

Note that I left the code unchanged, as you requested.

