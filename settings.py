import os
import json
import copy
import tempfile
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
                "requests_timeout": 30
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
                "sold": True,
                "expired": False,
                "all": True
            },
            "auto_complete_deals": {
                "enabled": False,
                "all": True
            },
            "auto_bump_items": {
                "enabled": False,
                "interval": 3600,
                "all": False
            },
            "auto_withdrawal": {
                "enabled": False,
                "interval": 86400,
                "credentials_type": "",
                "card_id": "",
                "sbp_bank_id": "",
                "sbp_phone_number": "",
                "usdt_address": ""
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
                "token": "",
                "proxy": ""
            },
            "bot": {
                "password": "",
                "signed_users": []
            }
        },
        "logs": {
            "max_file_size": 300
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
                "👋 Hello, {username}, I'm a bot assistant 𝗣𝗹𝗮𝘆𝗲𝗿𝗼𝗸 𝗨𝗻𝗶𝘃𝗲𝗿𝘀𝗮𝗹",
                "",
                "💡 If you want to talk to the seller, write the command !seller so that I can invite him to this dialogue."
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
                "🕹️ Basic commands:",
                "・ !seller - notify and invite the seller to this chat"
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
                "📋 Thanks for your purchase «{deal_item_name}»",
                ""
                "The seller may not be available right now; to call him, use the command !seller."
            ]
        },
        "deal_pending": {
            "enabled": False,
            "text": [
                "⌛ Send the necessary information so that I can complete your order"
            ]
        },
        "deal_sent": {
            "enabled": False,
            "text": [
                "✅ I have confirmed your order! If you have not received the purchased product, write it in the chat"
            ]
        },
        "deal_confirmed": {
            "enabled": False,
            "text": [
                "🌟 Thank you for a successful transaction. I will be glad if you leave a review. I look forward to seeing you in my store next time, good luck!"
            ]
        },
        "deal_refunded": {
            "enabled": False,
            "text": [
                "📦 The order was returned. I hope this transaction did not cause you any inconvenience. I look forward to seeing you in my store next time, good luck!"
            ]
        },
        "new_review": {
            "enabled": False,
            "text": [
                "✨ Thanks for {review_rating}⭐ review! I hope you liked the quality of the work performed"
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
AUTO_COMPLETE_DEALS = SettingsFile(
    name="auto_complete_deals",
    path="bot_settings/auto_complete_deals.json",
    need_restore=False,
    default={
        "included": [],
        "excluded": []
    }
)
AUTO_BUMP_ITEMS = SettingsFile(
    name="auto_bump_items",
    path="bot_settings/auto_bump_items.json",
    need_restore=False,
    default={
        "included": [],
        "excluded": []
    }
)
DATA = [CONFIG, MESSAGES, CUSTOM_COMMANDS, AUTO_DELIVERIES, AUTO_RESTORE_ITEMS, AUTO_COMPLETE_DEALS, AUTO_BUMP_ITEMS]


def validate_config(config, default):
    """
    Checks the config structure for compliance with the standard template.

    :param config: Current config.
    :type config: `dict`

    :param default: Standard template configuration.
    :type default: `dict`

    :return: True if the structure is valid, otherwise False.
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
    Restores missing parameters in the config from the standard template.
    And removes parameters from the config that are not in the standard template.

    :param config: Current config.
    :type config: `dict`

    :param default: Standard template configuration.
    :type default: `dict`

    :return: Restored config.
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
    Retrieves settings file data.
    Creates a settings file if it does not exist.
    Adds new data, if any.

    :param path: Path to json file
    :type path: `str`

    :param default: Standard file template.
    :type default: `dict`

    :param need_restore: Is it necessary to check the integrity of the config.
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
    Sets new data to the settings file.

    :param path: Path to json file
    :type path: `str`

    :param new: New data.
    :type new: `dict`
    """
    dir_name = os.path.dirname(path)
    
    with tempfile.NamedTemporaryFile( # atomic file write
        "w",
        encoding="utf-8",
        dir=dir_name,
        delete=False
    ) as tmp:
        json.dump(new, tmp, ensure_ascii=False, indent=4)
        tmp.flush()
        os.fsync(tmp.fileno())

    os.replace(tmp.name, path)


class Settings:
    
    @staticmethod
    def get(name: str, data: list[SettingsFile] = DATA) -> dict | list | None:
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