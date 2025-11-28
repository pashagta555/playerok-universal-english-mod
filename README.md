# Playerok Universal
[![telegram](https://img.shields.io/badge/telegram-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-blue?style=for-the-badge&logo=telegram)](https://t.me/alexeyproduction)
[![modules](https://img.shields.io/badge/%F0%9F%A7%A9%20%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D0%B8-%D0%B1%D0%BE%D1%82%D0%B0-green?style=for-the-badge)](https://t.me/alexey_production_bot)
[![python](https://img.shields.io/badge/python-3.11.x-yellow?style=for-the-badge&logo=python&link=https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftelegram-%25D0%25BA%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB-blue%3Fstyle%3Dfor-the-badge%26logo%3Dtelegram)](https://www.python.org/downloads/release/python-3119/)
[![stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.stargazers_count&style=for-the-badge&label=stars&color=43d433&logo=github)](https://github.com/alleexxeeyy/funpay-universal/stargazers)
[![forks](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.forks_count&style=for-the-badge&label=forks&color=%236c70e6&logo=github)](https://github.com/alleexxeeyy/funpay-universal/stargazers)

Modern bot assistant for Playerok 🤖🟦

---

## 🗺️ Navigation
- [Bot Features](#-features)
- [Bot Installation](#%EF%B8%8F-installation)
- [Useful Links](#-useful-links)
- [For Developers](#-for-developers)

## 🔧 Features
### 🤖💬 Telegram bot with full control
- Configure any parameter from config in a few actions
- View bot statistics and account profile
- Manage bot events

### ⚙️ Wide range of capabilities
- Module system (plugins that can be connected to the bot)
- Always online on the site
- Auto-restore items
- Welcome message
- Custom commands
- Custom auto-delivery
- `!seller` command to call the seller to chat
- Edit and enable/disable each message
- Notifications in TG about new messages, orders, reviews, etc.

### 🌐 More advanced
- HTTPS IPv4 proxy connection
- Request interval configuration

## ⬇️ Installation
1. Download the [latest Release version](https://github.com/alleexxeeyy/playerok-universal/releases/latest) and extract it to any convenient location
2. Make sure you have **Python version 3.11.x** installed (bot operation is not guaranteed on other versions). If not installed, do so by following the link https://www.python.org/downloads/release/python-31210/ (during installation, click on `Add to PATH`)
3. Open `install_requirements.bat` and wait for all necessary libraries to be installed, then close the window
4. To start the bot, open the launcher `start.bat`
5. After the first launch, you will be asked to configure the bot for operation

## 📚 For Developers

The modular system helps integrate additional functionality into the bot, made by enthusiasts. Essentially, it's the same as plugins, but in a more convenient format.
You can create your own module based on the [template](.templates/forms_module).

<details>
  <summary><strong>📌 Main Events</strong></summary>

  ### Bot Events (BOT_EVENT_HANDLERS)

  Events that are executed on a certain bot action.

  | Event | When triggered | Arguments passed |
  |-------|----------------|------------------|
  | `ON_MODULE_ENABLED` | When module is enabled | `Module` |
  | `ON_MODULE_DISABLED` | When module is disabled | `Module` |
  | `ON_INIT` | On bot initialization | `-` |
  | `ON_PLAYEROK_BOT_INIT` | On Playerok bot initialization (startup) | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | On Telegram bot initialization (startup) | `TelegramBot` |

  ### Playerok Events (PLAYEROK_EVENT_HANDLERS)

  Events received in the event listener in the Playerok bot.

  | Event | When triggered | Arguments passed |
  |-------|----------------|------------------|
  | `EventTypes.CHAT_INITIALIZED` | Chat initialized | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | New message in chat | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | New deal created (when buyer paid for item) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.NEW_REVIEW` | New review on deal | `PlayerokBot`, `NewReviewEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Deal confirmed | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | Seller issued deal refund | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | User reported a problem in deal | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | Deal problem resolved | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Deal status changed | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | User paid for item | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Item sent (seller confirmed deal completion) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Module Structure</strong></summary>  
  
  </br>A module is a folder containing important components. You can study the module structure based on the [template module](.templates/forms_module), but keep in mind that this is just an example we created.

  Required handler constants:
  | Constant | Type | Description |
  |----------|------|-------------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | This dictionary defines bot event handlers |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | This dictionary defines Playerok event handlers |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | This array defines modular Telegram bot routers  |

  Required metadata constants:
  | Constant | Type | Description |
  |----------|------|-------------|
  | `PREFIX` | `str` | Prefix |
  | `VERSION` | `str` | Version |
  | `NAME` | `str` | Name |
  | `DESCRIPTION` | `str` | Description |
  | `AUTHORS` | `str` | Authors |
  | `LINKS` | `str` | Links to authors |

  Also, if the module requires additional dependencies, it must have a **requirements.txt** dependency file, which will be automatically downloaded when loading all bot modules.

  #### 🔧 Example content:
  Note that metadata has been moved to a separate `meta.py` file, but is imported in `__init__.py`.
  This is done to avoid import conflicts in the further part of the module code.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Test module. /test_module in Telegram bot for management"
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
          print(f"{PREFIX} Module connected and active")
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
  <summary><strong>🛠️ Useful Tools</strong></summary>  
  
  ### 📝 Pre-configured configuration and data file wrappers
  Instead of struggling with configuration files and writing code to manage them, we've prepared a ready-made solution for you.
  The bot has pre-configured classes in files [`settings.py`](settings.py) and [`data.py`](data.py)

  #### How does it work?
  Let's say you want to create a configuration file in your module, for this you'll need to create a `settings.py` file in the root of the module folder.
  The content of `settings.py` should be approximately as follows:
  ```python
  import os
  from settings import (
      Settings as sett,
      SettingsFile
  )


  CONFIG = SettingsFile(
      name="config", #  configuration file name
      path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"), #  path to configuration file (in this case relative to module folder)
      need_restore=True, #  whether to restore config
      default={
          "bool_param": True,
          "str_param": "qwerty",
          "int_param": 123
      } #  default file content
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
  
  Next, you can get data from the config or save data to the config like this:
  ```python
  from . import settings as sett

  config = sett.get("config") #  get config
  print(config["bool_param"]) # -> True
  print(config["str_param"]) #  -> qwerty
  print(config["int_param"]) #  -> 123
  config["bool_param"] = False
  config["str_param"] = "uiop"
  config["int_param"] = 456
  sett.set("config", config) #  set new value to config
  ```

  When setting a new value to the config, it is immediately written to its file. Also, when getting, the current data from the file is taken.

  Description of `SettingsFile` dataclass arguments:
  | Argument | Description |
  |----------|-------------|
  | `name` | Configuration file name that will be used when getting and writing |
  | `path` | Path to configuration file |
  | `need_restore` | Whether to restore the config? Let's say new data was added to the default config value, but it's missing in the **previously** created configuration file. If the parameter is enabled, the script will compare the current config data with the specified default, and if the current data doesn't have a key that exists in the default value, it will be automatically added to the config. Also, if the type of a key's value in the default config doesn't match the existing one (for example, **string** type in the file, but **numeric** in the default value), this key in the current config will also be replaced with the default value |
  | `default` | Default configuration file value |


  </br>The data file is structured the same way, but it's needed to store information collected by the script itself, not specified by users.
  For example, you want to create a data file in your module, for this you'll need to create a `data.py` file in the root of the module folder.
  
  The content of `data.py` should be approximately as follows:
  ```python
  import os
  from data import (
      Data as data,
      DataFile
  )


  LATEST_EVENTS_TIMES = DataFile(
      name="new_forms", #  data file name
      path=os.path.join(os.path.dirname(__file__), "module_data", "new_forms.json"), #  path to data file (in this case relative to module folder)
      default={} #  default file content
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

  Everything here is similar to the configuration file, just serves a different purpose.


  ### 🔌 Convenient module state management
  Using methods from `core/modules.py`, you can conveniently enable/disable/reload the current module.
  To do this, you first need to get the UUID of the current running module, which is generated during its initialization.
  
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

  And then manage the module from any convenient place:
  ```python
  from core.modules import enable_module, disable_module, reload_module

  from . import get_module


  await disable_module(get_module().uuid) #  disables module
  await enable_module(get_module().uuid) #  enables module
  await reload_module(get_module().uuid) #  reloads module
  ```

</details>

<details>
  <summary><strong>❗ Notes</strong></summary>

  </br>The Telegram bot functionality is written on the aiogram 3 library, the system for integrating custom Telegram bot functionality works based on routers that merge with the main, primary bot router.
  And since they merge together, complications may arise if, for example, Callback data has identical names. Therefore, after writing Telegram bot functionality for a module, it's better to rename
  this data in a unique way so that it doesn't match the names of the main bot or additional connected modules.

</details>


## 🔗 Useful Links
- Developer: https://github.com/alleexxeeyy (profile has current links to all contacts for communication)
- Telegram channel: https://t.me/alexeyproduction
- Telegram bot for purchasing official modules: https://t.me/alexey_production_bot
