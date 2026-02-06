# Playerok Universal
[![telegram](https://img.shields.io/badge/telegram-channel-blue?style=for-the-badge&logo=telegram)](https://t.me/alexeyproduction)
[![modules](https://img.shields.io/badge/%F0%9F%A7%A9-modules-bot-green?style=for-the-badge)](https://t.me/alexey_production_bot)
[![python](https://img.shields.io/badge/python-3.12.x-yellow?style=for-the-badge&logo=python&link=https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftelegram-%25D0%25BA%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB-blue%3Fstyle%3Dfor-the-badge%26logo%3Dtelegram)](https://www.python.org/downloads/release/python-3119/)
[![stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.stargazers_count&style=for-the-badge&label=stars&color=43d433&logo=github)](https://github.com/alleexxeeyy/playerok-universal/stargazers)
[![forks](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.forks_count&style=for-the-badge&label=forks&color=%236c70e6&logo=github)](https://github.com/alleexxeeyy/playerok-universal/forks)

Modern assistant bot for Playerok 🤖🟦

---

## 🗺️ Navigation
- [Bot features](#-features)
- [Bot installation](#%EF%B8%8F-installation)
- [Useful links](#-useful-links)
- [For developers](#-for-developers)

## 🔧 Features
### 🤖💬 Telegram bot with full control
- Configure any parameter from the config in just a few actions
- View bot statistics and account profile
- Manage bot events

### ⚙️ Wide feature set
- Modular system (plugins that can be connected to the bot)
- Permanent online status on the site
- Auto-restore items
- Auto-bump items
- Auto-deliver goods
- Auto-withdraw funds
- Welcome message
- Custom commands
- Custom auto-delivery
- Command `!seller` to call the seller into the chat
- Edit and enable/disable each message
- Telegram notifications about new messages, orders, reviews, etc.

### 🌐 More advanced features
- Connect via HTTPS IPv4 proxy
- Configure request intervals

## ⬇️ Installation
1. Download the [latest release version](https://github.com/alleexxeeyy/playerok-universal/releases/latest) and unpack it anywhere convenient for you.
2. Make sure you have **Python version 3.12.x** installed (the bot is not guaranteed to work on other versions). If it is not installed, do so by visiting https://www.python.org/downloads/release/python-31210/ (during installation, check the `Add to PATH` option).
3. Open `install_requirements.bat` and wait for all required libraries to be installed, then close the window.
4. To start the bot, open the launcher `start.bat`.
5. After the first launch, you will be asked to configure the bot for work.

[Having trouble with installation? Click me](https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26)

## 📚 For developers

The modular system helps extend the bot with additional functionality made by enthusiasts. In essence, it is the same as plugins, but in a more convenient format.
You can create your own module based on the [template](.templates/forms_module).

<details>
  <summary><strong>📌 Main events</strong></summary>

  ### Bot events (BOT_EVENT_HANDLERS)

  Events that are triggered on specific bot actions.

  | Event | When it is called | Passed arguments |
  |-------|------------------|------------------------|
  | `ON_MODULE_ENABLED` | When a module is enabled | `Module` |
  | `ON_MODULE_DISABLED` | When a module is disabled | `Module` |
  | `ON_INIT` | On bot initialization | `-` |
  | `ON_PLAYEROK_BOT_INIT` | On Playerok bot initialization (start) | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | On Telegram bot initialization (start) | `TelegramBot` |

  ### Playerok events (PLAYEROK_EVENT_HANDLERS)

  Events received by the event listener in the Playerok bot.

  | Event | When it is called | Passed arguments |
  |-------|------------------|------------------------|
  | `EventTypes.CHAT_INITIALIZED` | Chat initialized | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | New message in chat | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | New deal created (when the buyer paid for the item) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.NEW_REVIEW` | New review for a deal | `PlayerokBot`, `NewReviewEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Deal confirmed | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | Seller issued a refund for the deal | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | User reported a problem with the deal | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | Problem with the deal resolved | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Deal status changed | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | User paid for an item | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Item sent (seller confirmed the deal) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Module structure</strong></summary>  
  
  </br>A module is a folder that contains important components. You can study the structure of a module using the [template module](.templates/forms_module), but keep in mind that it is only an example we created.

  Required handler constants:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | This dictionary defines handlers for bot events |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | This dictionary defines handlers for Playerok events |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | This list defines routers for the module’s Telegram bot |

  Required metadata constants:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `PREFIX` | `str` | Prefix |
  | `VERSION` | `str` | Version |
  | `NAME` | `str` | Name |
  | `DESCRIPTION` | `str` | Description |
  | `AUTHORS` | `str` | Authors |
  | `LINKS` | `str` | Author links |

  Also, if a module requires additional dependencies, it must contain a **requirements.txt** file whose packages will be automatically installed when all bot modules are loaded.

  #### 🔧 Example contents:
  Note that the metadata is moved into a separate file `meta.py`, but imported in `__init__.py`.
  This is done to avoid import conflicts in the rest of the module code.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Test module. /test_module in the Telegram bot for management"
  AUTHORS = "@alleexxeeyy"
  LINKS = "https://t.me/alleexxeeyy, https://t.me/alexeyproduction"
  ```

  **`__init__.py`**:
  ```python
  from playerokapi.listener.events import EventTypes
  from core.modules_manager import Module, disable_module

  from .plbot.handlers import on_playerok_bot_init, on_new_message, on_new_deal
  from .tgbot import router
  from .tgbot._handlers import on_telegram_bot_init
  from .meta import *
  

  _module: Module = None


  def set_module(module: Module):
      global _module
      _module = module

  def get_module():
      return _module
  
  async def on_module_enabled(module: Module):
      try:
          set_module(module)
          print(f"{PREFIX} Module is connected and active")
      except:
          await disable_module(_module.uuid)
  

  BOT_EVENT_HANDLERS = {
      "ON_MODULE_ENABLED": [on_module_enabled],
      "ON_PLAYEROK_BOT_INIT": [on_playerok_bot_init],
      "ON_TELEGRAM_BOT_INIT": [on_telegram_bot_init]
  }
  PLAYEROK_EVENT_HANDLERS = {
      EventTypes.NEW_MESSAGE: [on_new_message],
      EventTypes.NEW_DEAL: [on_new_deal],
      # ...
  }
  TELEGRAM_BOT_ROUTERS = [router]
  ```

</details>

<details>
  <summary><strong>🛠️ Useful tools</strong></summary>  

  ### 📝 Ready-made wrappers for configuration and data files
  Instead of constantly dealing with configuration files and writing code to manage them, we have prepared a ready-made solution for you.
  The bot already has configured classes in [`settings.py`](settings.py) and [`data.py`](data.py).

  #### How does it work?
  Suppose you want to create a configuration file in your module. To do this, you need to create a `settings.py` file in the root of the module folder.
  The contents of `settings.py` should look something like this:
  ```python
  import os
  from settings import (
      Settings as sett,
      SettingsFile
  )


  CONFIG = SettingsFile(
      name="config", #  name of the configuration file
      path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"), #  path to the configuration file (in this case, relative to the module folder)
      need_restore=True, #  whether the config should be restored
      default={
          "bool_param": True,
          "str_param": "qwerty",
          "int_param": 123
      } #  default contents of the file
  )

  DATA = [CONFIG]


  class Settings:
    
      @staticmethod
      def get(name: str) -> dict:
          return sett.get(name, DATA)

      @staticmethod
      def set(name: str, new: list | dict) -> dict:
          return sett.set(name, new, DATA)
  ```

  The configuration file is defined using the `SettingsFile` dataclass, which in turn is passed to the `DATA` array.
  
  Then you can get data from the config or save data to the config like this:
  ```python
  from . import settings as sett

  config = sett.get("config") #  get the config
  print(config["bool_param"]) # -> True
  print(config["str_param"]) #  -> qwerty
  print(config["int_param"]) #  -> 123
  config["bool_param"] = False
  config["str_param"] = "uiop"
  config["int_param"] = 456
  sett.set("config", config) #  save new values to the config
  ```

  When you assign a new value to the config, it is immediately written to its file. When reading, the most up-to-date data is taken from the file.

  Description of the `SettingsFile` dataclass arguments:
  | Argument | Description |
  |----------|----------|
  | `name` | Name of the configuration file that will be used when reading and writing |
  | `path` | Path to the configuration file |
  | `need_restore` | Whether the config should be restored. Suppose new data has been added to the default config value, but it is missing in an already created configuration file. If this parameter is enabled, the script will compare the current config data with the specified defaults, and if any key is missing in the current data but present in the default, it will be automatically added. Likewise, if the type of a default value does not match the existing type (for example, the file has a **string** but the default has a **number**), that key in the current config will be replaced with the default value. |
  | `default` | Default value of the configuration file |


  </br>The data file works exactly the same way, but it is used to store information collected by the script itself, not entered by the user.
  For example, if you want to create a data file in your module, you need to create a `data.py` file in the root of the module folder.
  
  The contents of `data.py` should look something like this:
  ```python
  import os
  from data import (
      Data as data,
      DataFile
  )


  LATEST_EVENTS_TIMES = DataFile(
      name="new_forms", #  name of the data file
      path=os.path.join(os.path.dirname(__file__), "module_data", "new_forms.json"), #  path to the data file (in this case, relative to the module folder)
      default={} #  default contents of the file
  )

  DATA = [LATEST_EVENTS_TIMES]


  class Data:

      @staticmethod
      def get(name: str) -> dict:
          return data.get(name, DATA)

      @staticmethod
      def set(name: str, new: list | dict) -> dict:
          return data.set(name, new, DATA)
  ```

  Everything here is similar to the configuration file, but serves a different purpose.


  ### 🔌 Convenient module state management
  Using the methods from `core/modules.py`, you can easily enable/disable/reload the current module.
  To do this, you first need to get the UUID of the currently running module, which is generated during its initialization.
  
  For example, in the `__init__.py` file you can do this:
  ```python
  # import ...


  _module: Module = None


  async def set_module(module: Module):
      global _module
      _module = module

  def get_module():
      return _module
  

  BOT_EVENT_HANDLERS = {
      "ON_MODULE_ENABLED": [set_module],
      # ...
  }
  # ...
  ```

  And then, you can manage the module anywhere you like:
  ```python
  from core.modules import enable_module, disable_module, reload_module

  from . import get_module


  await disable_module(get_module().uuid) #  disable the module
  await enable_module(get_module().uuid) #  enable the module
  await reload_module(get_module().uuid) #  reload the module
  ```

</details>

<details>
  <summary><strong>❗ Notes</strong></summary>

  </br>The Telegram bot functionality is written using the aiogram 3 library. The system for integrating custom Telegram bot functionality works based on routers that are merged with the main bot router.
  Since they are merged together, complications may arise if, for example, callback data names are identical. Therefore, after writing the Telegram bot functionality for a module, it is better to rename
  this data in a unique way so that it does not conflict with the names of the main bot or additional connected modules.

</details>


## 🔗 Useful links
- Developer: https://github.com/alleexxeeyy (the profile contains up-to-date links to all contact methods)
- Telegram channel: https://t.me/alexeyproduction
- Telegram bot for purchasing official modules: https://t.me/alexey_production_bot
