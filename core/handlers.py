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
    Returns bot event handlers.

    :return: A dictionary with events and handler lists.
    :rtype: `dict[str, list[callable]]`
    """
    return _bot_event_handlers


def set_bot_event_handlers(data: dict[str, list[callable]]):
    """
    Sets new bot event handlers.

    :param data: A dictionary with event names and handler lists.
    :type data: `dict[str, list[callable]]`
    """
    global _bot_event_handlers
    _bot_event_handlers = data


def add_bot_event_handler(event: str, handler: callable, index: int | None = None):
    """
    Adds a new handler to bot events.

    :param event: Event name to add the handler to.
    :type event: `str`

    :param handler: Callable handler.
    :type handler: `callable`

    :param index: Index in the handlers list, _optional_.
    :type index: `int` or `None`
    """
    global _bot_event_handlers
    if not index: _bot_event_handlers[event].append(handler)
    else: _bot_event_handlers[event].insert(index, handler)


def register_bot_event_handlers(handlers: dict[str, list[callable]]):
    """
    Registers bot event handlers (adds passed handlers if they are missing).

    :param data: A dictionary with event names and handler lists.
    :type data: `dict[str, list[callable]]`
    """
    global _bot_event_handlers
    for event_type, funcs in handlers.items():
        if event_type not in _bot_event_handlers:
            _bot_event_handlers[event_type] = []
        _bot_event_handlers[event_type].extend(funcs)


def remove_bot_event_handlers(handlers: dict[str, list[callable]]):
    """
    Removes passed bot handlers.

    :param handlers: A dictionary with events and bot handler lists.
    :type handlers: `dict[str, list[callable]]`
    """
    for event, funcs in handlers.items():
        if event in _bot_event_handlers:
            for func in funcs:
                if func in _bot_event_handlers[event]:
                    _bot_event_handlers[event].remove(func)


def get_playerok_event_handlers() -> dict[EventTypes, list]:
    """
    Returns Playerok event handlers.

    :return: A dictionary with events and handler lists.
    :rtype: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    return _playerok_event_handlers


def set_playerok_event_handlers(data: dict[EventTypes, list[callable]]):
    """
    Sets new Playerok event handlers.

    :param data: A dictionary with events and handler lists.
    :type data: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    global _playerok_event_handlers
    _playerok_event_handlers = data


def add_playerok_event_handler(event: EventTypes, handler: callable, index: int | None = None):
    """
    Adds a new handler to Playerok events.

    :param event: Event to add the handler to.
    :type event: `playerokapi.listener.events.EventTypes`

    :param handler: Callable handler.
    :type handler: `callable`

    :param index: Index in the handlers list, _optional_.
    :type index: `int` or `None`
    """
    global _playerok_event_handlers
    if not index: _playerok_event_handlers[event].append(handler)
    else: _playerok_event_handlers[event].insert(index, handler)


def register_playerok_event_handlers(handlers: dict[EventTypes, list[callable]]):
    """
    Registers Playerok event handlers (adds passed handlers if they are missing).

    :param data: A dictionary with events and handler lists.
    :type data: `dict[playerokapi.listener.events.EventTypes, list[callable]]`
    """
    global _playerok_event_handlers
    for event_type, funcs in handlers.items():
        if event_type not in _playerok_event_handlers:
            _playerok_event_handlers[event_type] = []
        _playerok_event_handlers[event_type].extend(funcs)


def remove_playerok_event_handlers(handlers: dict[EventTypes, list[callable]]):
    """
    Removes passed Playerok handlers.

    :param handlers: A dictionary with events and Playerok handler lists.
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
    Calls a bot event.

    :param event: Event type.
    :type event: `str`

    :param args: Arguments.
    :type args: `list`
    
    :param func: Function to call the event for (if you want to call it only for a specific one), _optional_.
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
            logger.error(f"{Fore.LIGHTRED_EX}Error while handling bot event handler «{handler.__module__}.{handler.__qualname__}» for event «{event}»: {Fore.WHITE}{e}")


async def call_playerok_event(event: EventTypes, args: list = []):
    """
    Calls a Playerok event.

    :param event: Event type.
    :type event: `playerokapi.enums.EventTypes`

    :param args: Arguments.
    :type args: `list`
    """
    handlers = get_playerok_event_handlers().get(event, [])
    for handler in handlers:
        try:
            await handler(*args)
        except Exception as e:
            logger.error(f"{Fore.LIGHTRED_EX}Error while handling Playerok event handler «{handler.__module__}.{handler.__qualname__}» for event «{event.name}»: {Fore.WHITE}{e}")