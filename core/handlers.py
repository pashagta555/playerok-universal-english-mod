from colorama import Fore
from logging import getLogger

from playerokapi.listener.events import EventTypes


logger = getLogger("universal.handlers")

_bot_event_handlers: dict[str, list[callable]] = {
    "ON_MODULE_CONNECTED": [],
    "ON_MODULE_ENABLED": [],
    "ON_INIT": [],
    "ON_PLAYEROK_BOT_INIT": [], 
    "ON_TELEGRAM_BOT_INIT": []
}
_playerok_event_handlers: dict[EventTypes, list[callable]] = {
    EventTypes.CHAT_INITIALIZED: [],
    EventTypes.NEW_MESSAGE: [],
    EventTypes.NEW_DEAL: [],
    EventTypes.NEW_REVIEW: [],
    EventTypes.DEAL_CONFIRMED: [],
    EventTypes.DEAL_CONFIRMED_AUTOMATICALLY: [],
    EventTypes.DEAL_ROLLED_BACK: [],
    EventTypes.DEAL_HAS_PROBLEM: [],
    EventTypes.DEAL_PROBLEM_RESOLVED: [],
    EventTypes.DEAL_STATUS_CHANGED: [],
    EventTypes.ITEM_PAID: [],
    EventTypes.ITEM_SENT: []
}


def get_bot_event_handlers() -> dict[str, list[callable]]:
    """
    Returns handlers events bot.

    :return: Dictionary With events And lists handlers.
    :rtype: `dict[str, list[callable]]`
    """
    return _bot_event_handlers


def set_bot_event_handlers(data: dict[str, list[callable]]):
    """
    Installs new handlers events bot.

    :param data: Dictionary With names events And lists handlers.
    :type data: `dict[str, list[callable]]`
    """
    global _bot_event_handlers
    _bot_event_handlers = data


def add_bot_event_handler(event: str, handler: callable, index: int | None = None):
    """
    Adds new handler V events bot.

    :param event: Name events, For whom is added handler.
    :type event: `str`

    :param handler: Called method.
    :type handler: `callable`

    :param index: Index V array handlers, _optional_.
    :type index: `int` or `None`
    """
    global _bot_event_handlers
    if not index: _bot_event_handlers[event].append(handler)
    else: _bot_event_handlers[event].insert(index, handler)


def register_bot_event_handlers(handlers: dict[str, list[callable]]):
    """
    Registers handlers events bot (adds transferred handlers, If their There is not). 

    :param data: Dictionary With names events And lists handlers.
    :type data: `dict[str, list[callable]]`
    """
    global _bot_event_handlers
    for event_type, funcs in handlers.items():
        if event_type not in _bot_event_handlers:
            _bot_event_handlers[event_type] = []
        _bot_event_handlers[event_type].extend(funcs)


def remove_bot_event_handlers(handlers: dict[str, list[callable]]):
    """
    Deletes transferred handlers bot.

    :param handlers: Dictionary With events And lists handlers bot.
    :type handlers: `dict[str, list[callable]]`
    """
    for event, funcs in handlers.items():
        if event in _bot_event_handlers:
            for func in funcs:
                if func in _bot_event_handlers[event]:
                    _bot_event_handlers[event].remove(func)


def get_playerok_event_handlers() -> dict[EventTypes, list]:
    """
    Returns handlers events Playerok.

    :return: Dictionary With events And lists handlers.
    :rtype: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    return _playerok_event_handlers


def set_playerok_event_handlers(data: dict[EventTypes, list[callable]]):
    """
    Installs new handlers events Playerok.

    :param data: Dictionary With events And lists handlers.
    :type data: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    global _playerok_event_handlers
    _playerok_event_handlers = data


def add_playerok_event_handler(event: EventTypes, handler: callable, index: int | None = None):
    """
    Adds new handler V events Playerok.

    :param event: Event, For whom is added handler.
    :type event: `playerokapi.listener.events.EventTypes`

    :param handler: Called method.
    :type handler: `callable`

    :param index: Index V array handlers, _optional_.
    :type index: `int` or `None`
    """
    global _playerok_event_handlers
    if not index: _playerok_event_handlers[event].append(handler)
    else: _playerok_event_handlers[event].insert(index, handler)


def register_playerok_event_handlers(handlers: dict[EventTypes, list[callable]]):
    """
    Registers handlers events Playerok (adds transferred handlers, If their There is not). 

    :param data: Dictionary With events And lists handlers.
    :type data: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    global _playerok_event_handlers
    for event_type, funcs in handlers.items():
        if event_type not in _playerok_event_handlers:
            _playerok_event_handlers[event_type] = []
        _playerok_event_handlers[event_type].extend(funcs)


def remove_playerok_event_handlers(handlers: dict[EventTypes, list[callable]]):
    """
    Deletes transferred handlers Playerok.

    :param handlers: Dictionary With events And lists handlers Playerok.
    :type handlers: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    global _playerok_event_handlers
    for event, funcs in handlers.items():
        if event in _playerok_event_handlers:
            for func in funcs:
                if func in _playerok_event_handlers[event]:
                    _playerok_event_handlers[event].remove(func)


async def call_bot_event(event: str, args: list = [], func = None):
    """
    Calls event bot.

    :param event: Type event.
    :type event: `str`

    :param args: Arguments.
    :type args: `list`
    
    :param func: Function, For which need to call event (If need to call only For one certain), _optional_.
    :type func: `callable` or `None`
    """
    if not func: 
        handlers = get_bot_event_handlers().get(event, [])
    else:
        handlers = [func]
    for handler in handlers:
        try:
            await handler(*args)
        except Exception as e:
            logger.error(f"{Fore.LIGHTRED_EX}Error at processing handler «{handler.__module__}.{handler.__qualname__}» For event bot «{event}»: {Fore.WHITE}{e}")


async def call_playerok_event(event: EventTypes, args: list = []):
    """
    Calls event bot.

    :param event: Type event.
    :type event: `playerokapi.enums.EventTypes`

    :param args: Arguments.
    :type args: `list`
    """
    handlers = get_playerok_event_handlers().get(event, [])
    for handler in handlers:
        try:
            await handler(*args)
        except Exception as e:
            logger.error(f"{Fore.LIGHTRED_EX}Error at processing handler «{handler.__module__}.{handler.__qualname__}» For event Playerok «{event.name}»: {Fore.WHITE}{e}")