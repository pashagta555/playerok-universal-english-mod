# Playerok Universal
[![telegram](https://img.shields.io/badge/telegram-channel-blue?style=for-the-badge&logo=telegram)](https://t.me/alexeyproduction)
[![modules](https://img.shields.io/badge/%F0%9F%A7%A9%20bot%20modules-green?style=for-the-badge)](https://t.me/alexey_production_bot)
[![python](https://img.shields.io/badge/python-3.12.x-yellow?style=for-the-badge&logo=python&link=https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftelegram-%25D0%25BA%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB-blue%3Fstyle%3Dfor-the-badge%26logo%3Dtelegram)](https://www.python.org/downloads/release/python-3119/)
[![stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.stargazers_count&style=for-the-badge&label=stars&color=43d433&logo=github)](https://github.com/alleexxeeyy/playerok-universal/stargazers)
[![forks](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.forks_count&style=for-the-badge&label=forks&color=%236c70e6&logo=github)](https://github.com/alleexxeeyy/playerok-universal/forks)

A modern bot assistant for Playerok 🤖🟦

---

## 🗺️ Navigation
- [Bot features](#-features)
- [Installation](#%EF%B8%8F-installation)
- [Useful links](#-useful-links)
- [For developers](#-for-developers)

## 🔧 Features
### 🤖💬 Telegram bot with full control
- Configure any parameter from the config in a few steps
- View bot statistics and account profile
- Manage bot events

### ⚙️ Broad capabilities
- Module system (plugins that can be attached to the bot)
- Permanent online on the site
- Auto-restore items
- Auto-bump items
- Auto-delivery of goods
- Auto-withdrawal of funds
- Welcome message
- Custom commands
- Custom auto-delivery
- `!seller` command to call the seller to the chat
- Edit and enable/disable each message
- TG notifications for new messages, orders, reviews, etc.

### 🌐 Advanced
- HTTPS IPv4 proxy connection
- Request interval configuration

## ⬇️ Installation
1. Download the [latest Release](https://github.com/alleexxeeyy/playerok-universal/releases/latest) and extract it to any folder
2. Make sure **Python 3.12.x** is installed (other versions are not guaranteed to work). If not, install it from https://www.python.org/downloads/release/python-31210/ (during installation, check `Add to PATH`)
3. Run `install_requirements.bat` and wait for all required libraries to install, then close the window
4. To start the bot, run `start.bat`
5. On first run you will be asked to configure the bot

[Installation issues? Click here](https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26)

## 📚 For developers

The module system makes it easy to add extra functionality to the bot, written by the community. In practice it is like plugins, but in a more convenient format.
You can create your own module using the [template](.templates/forms_module).

<details>
  <summary><strong>📌 Main events</strong></summary>

  ### Bot events (BOT_EVENT_HANDLERS)

  Events that run when the bot performs a certain action.

  | Event | When it is triggered | Arguments |
  |-------|----------------------|------------|
  | `ON_MODULE_ENABLED` | When the module is enabled | `Module` |
  | `ON_MODULE_DISABLED` | When the module is disabled | `Module` |
  | `ON_INIT` | On bot initialization | `-` |
  | `ON_PLAYEROK_BOT_INIT` | On Playerok bot initialization (start) | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | On Telegram bot initialization (start) | `TelegramBot` |

  ### Playerok events (PLAYEROK_EVENT_HANDLERS)

  Events received by the event listener in the Playerok bot.

  | Event | When it is triggered | Arguments |
  |-------|----------------------|------------|
  | `EventTypes.CHAT_INITIALIZED` | Chat initialized | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | New message in chat | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | New deal created (buyer paid for item) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.NEW_REVIEW` | New review for a deal | `PlayerokBot`, `NewReviewEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Deal confirmed | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | Seller issued a refund | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | User reported a problem with the deal | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | Deal problem resolved | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Deal status changed | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | User paid for item | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Item sent (seller confirmed completion) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Module structure</strong></summary>  
  
  </br>A module is a folder containing the main components. You can study the structure using the [template module](.templates/forms_module); note that it is only an example.

  Required handler constants:
  | Constant | Type | Description |
  |----------|------|-------------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | Handlers for bot events |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | Handlers for Playerok events |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | Routers for the module’s Telegram bot |

  Required metadata constants:
  | Constant | Type | Description |
  |----------|------|-------------|
  | `PREFIX` | `str` | Prefix |
  | `VERSION` | `str` | Version |
  | `NAME` | `str` | Name |
  | `DESCRIPTION` | `str` | Description |
  | `AUTHORS` | `str` | Authors |
  | `LINKS` | `str` | Links to authors |

  If the module needs extra dependencies, it must include a **requirements.txt** file; dependencies are installed when all modules are loaded.

  #### 🔧 Example content:
  Metadata is in a separate file `meta.py` and imported in `__init__.py` to avoid import conflicts.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Test module. Use /test_module in the Telegram bot to manage"
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
  <summary><strong>🛠️ Useful tools</strong></summary>  
  
  ### 📝 Preconfigured config and data file wrappers
  Instead of dealing with config files and writing your own management code, the bot provides ready-made classes in [`settings.py`](settings.py) and [`data.py`](data.py).

  #### How it works
  To add a config file in your module, create a `settings.py` in the module root. It can look like this:
  ```python
  import os
  from settings import (
      Settings as sett,
      SettingsFile
  )


  CONFIG = SettingsFile(
      name="config", # config file name
      path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"), # path to config (here, relative to module folder)
      need_restore=True, # whether to restore config
      default={
          "bool_param": True,
          "str_param": "qwerty",
          "int_param": 123
      } # default contents
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

  The config is defined with the `SettingsFile` dataclass, which is passed in the `DATA` list.
  
  Usage:
  ```python
  from . import settings as sett

  config = sett.get("config") # get config
  print(config["bool_param"]) # -> True
  print(config["str_param"]) #  -> qwerty
  print(config["int_param"]) #  -> 123
  config["bool_param"] = False
  config["str_param"] = "uiop"
  config["int_param"] = 456
  sett.set("config", config) # save new config
  ```

  When you set a new value, it is written to the file. When you get, the current data is read from the file.

  `SettingsFile` arguments:
  | Argument | Description |
  |----------|-------------|
  | `name` | Config name used for get/set |
  | `path` | Path to the config file |
  | `need_restore` | Restore config? If the default gains new keys that are missing in an existing file, they are added. If a key’s type in the file does not match the default (e.g. string vs number), it is replaced with the default value. |
  | `default` | Default config contents |


  </br>Data files work the same way but are used for script-collected data, not user input. To add a data file in your module, create `data.py` in the module root.
  
  Example `data.py`:
  ```python
  import os
  from data import (
      Data as data,
      DataFile
  )


  LATEST_EVENTS_TIMES = DataFile(
      name="new_forms", # data file name
      path=os.path.join(os.path.dirname(__file__), "module_data", "new_forms.json"), # path (here, relative to module folder)
      default={} # default contents
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

  Same idea as config, different purpose.


  ### 🔌 Module state control
  Using `core/modules.py` you can enable/disable/reload the current module. You need the module’s UUID, which is set when the module is loaded.
  
  Example in `__init__.py`:
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

  Then anywhere in the module:
  ```python
  from core.modules import enable_module, disable_module, reload_module

  from . import get_module


  await disable_module(get_module().uuid) # disable module
  await enable_module(get_module().uuid) # enable module
  await reload_module(get_module().uuid) # reload module
  ```

</details>

<details>
  <summary><strong>❗ Notes</strong></summary>

  </br>The Telegram bot is built with aiogram 3. Custom Telegram functionality is added via routers that are merged with the main bot router. Because they are merged, conflicts can occur if callback data names match. After implementing your module’s Telegram bot part, give callback data unique names so they do not clash with the main bot or other modules.

</details>


## 🔗 Useful links
- Developer: https://github.com/alleexxeeyy (profile has up-to-date contact links)
- Telegram channel: https://t.me/alexeyproduction
- Telegram bot for official modules: https://t.me/alexey_production_bot
