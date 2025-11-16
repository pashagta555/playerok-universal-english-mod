import os
import json
import copy
from dataclasses import dataclass


@dataclass
class SettingsFile:
    name: str
    path: str
    need_restore: bool
    default: list | dict


CONFIG = SettingsFile(
    name="config",
    path="bot_settings/config.json",
    need_restore=True,
    default={
        "playerok": {
            "api": {
                "token": "",
                "user_agent": "",
                "proxy": "",
                "requests_timeout": 30,
                "listener_requests_delay": 4
            },
            "watermark": {
                "enabled": True,
                "value": "©️ 𝗣𝗹𝗮𝘆𝗲𝗿𝗼𝗸 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗮𝗹"
            },
            "read_chat": {
                "enabled": True
            },
            "first_message": {
                "enabled": True
            },
            "custom_commands": {
                "enabled": True
            },
            "auto_deliveries": {
                "enabled": True
            },
            "auto_restore_items": {
                "enabled": True,
                "all": True
            },
            "auto_complete_deals": {
                "enabled": True
            },
            "tg_logging": {
                "enabled": True,
                "chat_id": "",
                "events": {
                    "new_user_message": True,
                    "new_system_message": True,
                    "new_deal": True,
                    "new_review": True,
                    "new_problem": True,
                    "deal_status_changed": True,
                }
            },
        },
        "telegram": {
            "api": {
                "token": ""
            },
            "bot": {
                "password": "",
                "signed_users": []
            }
        }
    }
)
MESSAGES = SettingsFile(
    name="messages",
    path="bot_settings/messages.json",
    need_restore=True,
    default={
        "first_message": {
            "enabled": True,
            "text": [
                "👋 Hi, {username}, it's bot-helper 𝗣𝗹𝗮𝘆𝗲𝗿𝗼𝗸 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗮𝗹",
                "",
                "💡 If you want to talk to the seller, write !seller, so that I invite him to this dialogue",
                "",
                "To find out all my commands, write !commands"
            ]
        },
        "cmd_error": {
            "enabled": True,
            "text": [
                "❌ An error occurred while entering the command: {error}"
            ]
        },
        "cmd_commands": {
            "enabled": True,
            "text": [
                "🕹️ Main commands:",
                "・ !seller - notify and call the seller to this chat"
            ]
        },
        "cmd_seller": {
            "enabled": True,
            "text": [
                "💬 The seller was called to this chat. Wait for him to join the dialogue..."
            ]
        },
        "new_deal": {
            "enabled": False,
            "text": [
                "📋 Thanks for the order «{deal_item_name}» amount {deal_amount} шт.",
                ""
                "The seller may not be there now, to call him, use the command! Seller."
            ]
        },
        "deal_pending": {
            "enabled": False,
            "text": [
                "⌛ Отправьте нужные данные, чтобы я смог выполнить ваш заказ"
            ]
        },
        "deal_sent": {
            "enabled": False,
            "text": [
                "✅ Я подтвердил выполнение вашего заказа! Если вы не получили купленный товар - напишите это в чате"
            ]
        },
        "deal_confirmed": {
            "enabled": False,
            "text": [
                "🌟Thank you for a successful deal. I will be glad if you leave a review. I'm waiting for you in my store next time, good luck!"
            ]
        },
        "deal_refunded": {
            "enabled": False,
            "text": [
                "📦 The order has been returned. I hope this deal didn't inconvenience you. I'm waiting for you in my store next time, good luck!"
            ]
        }
    }
)
CUSTOM_COMMANDS = SettingsFile(
    name="custom_commands",
    path="bot_settings/custom_commands.json",
    need_restore=False,
    default={}
)
AUTO_DELIVERIES = SettingsFile(
    name="auto_deliveries",
    path="bot_settings/auto_deliveries.json",
    need_restore=False,
    default=[]
)
AUTO_RESTORE_ITEMS = SettingsFile(
    name="auto_restore_items",
    path="bot_settings/auto_restore_items.json",
    need_restore=False,
    default={
        "included": [],
        "excluded": []
    }
)
DATA = [CONFIG, MESSAGES, CUSTOM_COMMANDS, AUTO_DELIVERIES, AUTO_RESTORE_ITEMS]


def validate_config(config, default):
    """
    Проверяет структуру конфига на соответствие стандартному шаблону.

    :param config: Текущий конфиг.
    :type config: `dict`

    :param default: Стандартный шаблон конфига.
    :type default: `dict`

    :return: True если структура валидна, иначе False.
    :rtype: bool
    """
    for key, value in default.items():
        if key not in config:
            return False
        if type(config[key]) is not type(value):
            return False
        if isinstance(value, dict) and isinstance(config[key], dict):
            if not validate_config(config[key], value):
                return False
    return True


def restore_config(config: dict, default: dict):
    """
    Восстанавливает недостающие параметры в конфиге из стандартного шаблона.
    И удаляет параметры из конфига, которых нету в стандартном шаблоне.

    :param config: Текущий конфиг.
    :type config: `dict`

    :param default: Стандартный шаблон конфига.
    :type default: `dict`

    :return: Восстановленный конфиг.
    :rtype: `dict`
    """
    config = copy.deepcopy(config)

    def check_default(config, default):
        for key, value in dict(default).items():
            if key not in config:
                config[key] = value
            elif type(value) is not type(config[key]):
                config[key] = value
            elif isinstance(value, dict) and isinstance(config[key], dict):
                check_default(config[key], value)
        return config

    config = check_default(config, default)
    return config
    

def get_json(path: str, default: dict, need_restore: bool = True) -> dict:
    """
    Получает данные файла настроек.
    Создаёт файл настроек, если его нет.
    Добавляет новые данные, если такие есть.

    :param path: Путь к json файлу.
    :type path: `str`

    :param default: Стандартный шаблон файла.
    :type default: `dict`

    :param need_restore: Нужно ли сделать проверку на целостность конфига.
    :type need_restore: `bool`
    """
    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        if need_restore:
            new_config = restore_config(config, default)
            if config != new_config:
                config = new_config
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(config, f, indent=4, ensure_ascii=False)
    except:
        config = default
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    finally:
        return config
    

def set_json(path: str, new: dict):
    """
    Устанавливает новые данные в файл настроек.

    :param path: Путь к json файлу.
    :type path: `str`

    :param new: Новые данные.
    :type new: `dict`
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(new, f, indent=4, ensure_ascii=False)


class Settings:
    
    @staticmethod
    def get(name: str, data: list[SettingsFile] = DATA) -> dict | None:
        try: 
            file = [file for file in data if file.name == name][0]
            return get_json(file.path, file.default, file.need_restore)
        except: return None

    @staticmethod
    def set(name: str, new: list | dict, data: list[SettingsFile] = DATA):
        try: 
            file = [file for file in data if file.name == name][0]
            set_json(file.path, new)
        except: pass
