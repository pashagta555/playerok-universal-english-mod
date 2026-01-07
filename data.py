import json
import os
from dataclasses import dataclass


@dataclass
class DataFile:
    name: str
    path: str
    default: list | dict


INITIALIZED_USERS = DataFile(
    name="initialized_users",
    path="bot_data/initialized_users.json",
    default=[]
)
SAVED_ITEMS = DataFile(
    name="saved_items",
    path="bot_data/saved_items.json",
    default=[]
)
DATA = [INITIALIZED_USERS, SAVED_ITEMS]


def get_json(path: str, default: dict | list) -> dict:
    """
    Gets the contents of a data file.
    Creates a data file if it doesn't exist.

    :param path: Path to json file.
    :type path: `str`

    :param default: Standard file structure.
    :type default: `dict`
    """
    folder_path = os.path.dirname(path)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    except:
        config = default
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
    finally:
        return config
    

def set_json(path: str, new: dict):
    """
    Sets new data in the data file.

    :param path: Path to json file.
    :type path: `str`

    :param new: New data.
    :type new: `dict`
    """
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(new, f, indent=4, ensure_ascii=False)


class Data:
    
    @staticmethod
    def get(name: str, data: list[DataFile] = DATA) -> dict | list | None:
        try: 
            file = [file for file in data if file.name == name][0]
            return get_json(file.path, file.default)
        except: return None

    @staticmethod
    def set(name: str, new: list | dict, data: list[DataFile] = DATA):
        try: 
            file = [file for file in data if file.name == name][0]
            set_json(file.path, new)
        except: pass