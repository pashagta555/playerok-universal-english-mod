import os
import sys
import importlib
import uuid
from uuid import UUID
from colorama import Fore
from dataclasses import dataclass
from logging import getLogger

from __init__ import ACCENT_COLOR
from core.handlers import (
    register_bot_event_handlers, 
    register_playerok_event_handlers, 
    remove_bot_event_handlers, 
    remove_playerok_event_handlers, 
    call_bot_event
)
from core.utils import install_requirements


logger = getLogger("universal.modules")


@dataclass
class ModuleMeta:
    prefix: str
    version: str
    name: str
    description: str
    authors: str
    links: str

@dataclass
class Module:
    uuid: UUID
    enabled: bool
    meta: ModuleMeta
    bot_event_handlers: dict
    playerok_event_handlers: dict
    telegram_bot_routers: list
    _dir_name: str


loaded_modules: list[Module] = []


def get_modules():
    """
    Returns loaded modules.

    :return: Loaded modules
    :rtype: `list` of `core.modules.Module`
    """
    return loaded_modules


def set_modules(modules: list[Module]):
    """
    Sets the loaded modules.

    :param modules: New loaded modules
    :type modules: `list` of `core.modules.Module`
    """
    global loaded_modules
    loaded_modules = modules


def get_module_by_uuid(module_uuid: UUID) -> Module | None:
    """ 
    Gets a module by UUID.
    
    :param module_uuid: UUID of the module.
    :type module_uuid: `uuid.UUID`

    :return: Module object.
    :rtype: `core.modules.Module` or `None`
    """
    try: return [module for module in loaded_modules if module.uuid == module_uuid][0]
    except: return None


async def _enable_module(module: Module) -> bool:
    global loaded_modules

    register_bot_event_handlers(module.bot_event_handlers)
    register_playerok_event_handlers(module.playerok_event_handlers)

    module.enabled = True
    loaded_modules[loaded_modules.index(module)] = module

    handlers = module.bot_event_handlers.get("ON_MODULE_ENABLED", [])
    for handler in handlers:
        await call_bot_event("ON_MODULE_ENABLED", [module], handler)


async def enable_module(module_uuid: UUID) -> bool:
    """
    Enables the module and adds its handlers.

    :param module_uuid: UUID of the module.
    :type module_uuid: `uuid.UUID`

    :return: True if the module was enabled, False otherwise.
    :rtype: `bool`
    """
    try:
        module = get_module_by_uuid(module_uuid)
        await _enable_module(module)
        logger.info(f"Module {Fore.LIGHTWHITE_EX}{module.meta.name} {Fore.WHITE}enabled")
        
        return True
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}Error while enabling module {module_uuid}: {Fore.WHITE}{e}")
        return False


async def _disable_module(module: Module) -> bool:
    global loaded_modules
        
    remove_bot_event_handlers(module.bot_event_handlers)
    remove_playerok_event_handlers(module.playerok_event_handlers)

    module.enabled = False
    loaded_modules[loaded_modules.index(module)] = module

    handlers = module.bot_event_handlers.get("ON_MODULE_DISABLED", [])
    for handler in handlers:
        await call_bot_event("ON_MODULE_DISABLED", [module], handler)


async def disable_module(module_uuid: UUID) -> bool:
    """ 
    Disables the module and removes its handlers.
    
    :param module_uuid: UUID of the module.
    :type module_uuid: `uuid.UUID`

    :return: True if the module was disabled, False otherwise.
    :rtype: `bool`
    """
    try:
        module = get_module_by_uuid(module_uuid)
        await _disable_module(module)
        logger.info(f"Module {Fore.LIGHTWHITE_EX}{module.meta.name} {Fore.WHITE}disabled")
        
        return True
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}Error while disabling module {module_uuid}: {Fore.WHITE}{e}")
        return False


async def reload_module(module_uuid: str):
    """
    Reloads a module (unloads and imports it again).
    
    :param module_uuid: UUID of the module.
    :type module_uuid: `uuid.UUID`

    :return: True if the module was reloaded, False otherwise.
    :rtype: `bool`
    """
    try:
        module = get_module_by_uuid(module_uuid)
        
        await _disable_module(module)
        if module._dir_name in sys.modules:
            del sys.modules[f"modules.{module._dir_name}"]
        importlib.import_module(f"modules.{module._dir_name}")
        await _enable_module(module)

        logger.info(f"Module {Fore.LIGHTWHITE_EX}{module.meta.name} {Fore.WHITE}reloaded")
        return True
    except Exception as e:
        logger.error(f"{Fore.LIGHTRED_EX}Error while reloading module {module_uuid}: {Fore.WHITE}{e}")
        return False


def load_modules() -> list[Module]:
    """Loads all modules from the modules folder."""
    global loaded_modules
    
    modules = []
    modules_path = "modules"
    os.makedirs(modules_path, exist_ok=True)

    for name in os.listdir(modules_path):
        bot_event_handlers = {}
        playerok_event_handlers = {}
        telegram_bot_routers = []
        module_path = os.path.join(modules_path, name)
        
        if os.path.isdir(module_path) and "__init__.py" in os.listdir(module_path):
            try:
                install_requirements(os.path.join(module_path, "requirements.txt"))
                module = importlib.import_module(f"modules.{name}")
                if hasattr(module, "BOT_EVENT_HANDLERS"):
                    for key, funcs in module.BOT_EVENT_HANDLERS.items():
                        bot_event_handlers.setdefault(key, []).extend(funcs)
                if hasattr(module, "PLAYEROK_EVENT_HANDLERS"):
                    for key, funcs in module.PLAYEROK_EVENT_HANDLERS.items():
                        playerok_event_handlers.setdefault(key, []).extend(funcs)
                if hasattr(module, "TELEGRAM_BOT_ROUTERS"):
                    telegram_bot_routers.extend(module.TELEGRAM_BOT_ROUTERS)
                module_data = Module(
                    uuid.uuid4(),
                    enabled=False,
                    meta=ModuleMeta(
                        module.PREFIX,
                        module.VERSION,
                        module.NAME,
                        module.DESCRIPTION,
                        module.AUTHORS,
                        module.LINKS
                    ),
                    bot_event_handlers=bot_event_handlers,
                    playerok_event_handlers=playerok_event_handlers,
                    telegram_bot_routers=telegram_bot_routers,
                    _dir_name=name
                )
                modules.append(module_data)
            except Exception as e:
                logger.error(f"{Fore.LIGHTRED_EX}Error while loading module {name}: {Fore.WHITE}{e}")
    
    return modules


def _format_string(count: int):
    last_num = int(str(count)[-1])
    if last_num == 1: return f"{Fore.LIGHTWHITE_EX}{count} module connected"
    elif 2 <= last_num <= 4: return f"{Fore.LIGHTWHITE_EX}{count} modules connected"
    elif 5 <= last_num <= 9 or last_num == 0: return f"{Fore.LIGHTWHITE_EX}{count} modules connected"


async def connect_modules(modules: list[Module]):
    """
    Connects loaded modules.
    
    :param modules: Loaded modules
    :type modules: `list` of `core.modules.Module`
    """
    global loaded_modules

    for module in modules:
        try:
            await _enable_module(module)
        except Exception as e:
            logger.error(f"{Fore.LIGHTRED_EX}Error while connecting module {module.meta.name}: {Fore.WHITE}{e}")
    
    connected_modules = [module for module in loaded_modules if module.enabled]
    names = [f"{Fore.YELLOW}{module.meta.name} {Fore.LIGHTWHITE_EX}{module.meta.version}" for module in connected_modules]
    if names:
        logger.info(f'{_format_string(len(connected_modules))}{Fore.WHITE}: {f"{Fore.WHITE}, ".join(names)}')