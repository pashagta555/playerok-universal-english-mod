Here is the translation of the text to English:

from aiogram.filters.callback_data import CallbackData
from uuid import UUID


class ModulePage(CallbackData, prefix="module page"):
    uuid: UUID


class MessagePage(CallbackData, prefix="message page"):
    message_id: str


class CustomCommandPage(CallbackData, prefix="custom command page"):
    command: str


class AutoDeliveryPage(CallbackData, prefix="auto delivery page"):
    index: int

