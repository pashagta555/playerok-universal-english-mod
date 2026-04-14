# Playerok Universal
[![telegram](https://img.shields.io/badge/telegram-%D0%BA%D0%B0%D0%BD%D0%B0%D0%BB-blue?style=for-the-badge&logo=telegram)](https://t.me/alexeyproduction)
[![modules](https://img.shields.io/badge/%F0%9F%A7%A9%20%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D0%B8-%D0%B1%D0%BE%D1%82%D0%B0-green?style=for-the-badge)](https://t.me/alexey_production_bot)
[![python](https://img.shields.io/badge/python-3.12.x-yellow?style=for-the-badge&logo=python&link=https%3A%2F%2Fimg.shields.io%2Fbadge%2Ftelegram-%25D0%25BA%25D0%25B0%25D0%25BD%25D0%25B0%25D0%25BB-blue%3Fstyle%3Dfor-the-badge%26logo%3Dtelegram)](https://www.python.org/downloads/release/python-3119/)
[![stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.stargazers_count&style=for-the-badge&label=stars&color=43d433&logo=github)](https://github.com/alleexxeeyy/playerok-universal/stargazers)
[![forks](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.forks_count&style=for-the-badge&label=forks&color=%236c70e6&logo=github)](https://github.com/alleexxeeyy/playerok-universal/forks)

Modern bot assistant for Playerok 🤖🟦

---

## 🗺️ Navigation
- [Bot functionality](#-functionality)
- [Bot installation](#%EF%B8%8F-installation)
- [Useful links](#-useful-links)
- [For developers](#-for-developers)

## 🔧 Functionality
### 🤖💬 Telegram bot with full control
- Setting any parameter from the config in a couple of steps
- View bot statistics and account profile
- Bot event management

### ⚙️ Wide range of possibilities
- System of modules (plugins connected to the bot)
- Eternal online on the site
- Auto-recovery of items
- Auto-lifting objects
- Automatic delivery of goods
- Auto-withdrawal
- Auto-confirmation of transactions
- Welcome message
- Custom commands
- Custom auto-issue
- Command `!seller` to call the seller in chat
- Editing and enabling/disabling each message
- Notifications in TG about new messages, orders, reviews, etc.

### 🌐 More advanced
- Connect to proxy HTTPS IPv4
- Configuring request intervals

## ⬇️ Installation
1. Download [latest Release version](https://github.com/alleexxeeyy/playerok-universal/releases/latest) and unpack it to any place convenient for you
2. Make sure you have ** installedPython version 3.12.x** (on other versions the bot is not guaranteed to work). If not installed, do so by following the link https://www.python.org/downloads/release/python-31210/ (When installing, click on `Add to PATH`)
3. Open `install_requirements.bat` and wait until all the libraries necessary for operation are installed, and then close the window
4. To launch the bot, open the launcher `start.bat`
5. After the first launch, you will be asked to configure the bot to work

[Having problems installing? Click on me](https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26)

## 📚 For developers

The modular system helps to implement additional functionality into the bot, made by enthusiasts. Essentially, this is the same as plugins, but in a more convenient format.
You can create your own module based on [template](.templates/forms_module).

<details>
  <summary><strong>📌 Main events</strong></summary>

  ### Bot events (BOT_EVENT_HANDLERS)

  Events that are executed when a certain bot action occurs.

  | Event | When | is called Passed Arguments |
  |-------|------------------|------------------------|
  | `ON_MODULE_ENABLED` | When you turn on the module | `Module` |
  | `ON_MODULE_DISABLED` | When the module is turned off | `Module` |
  | `ON_INIT` | When initializing the bot | `-` |
  | `ON_PLAYEROK_BOT_INIT` | During initialization (startup) Playerok bot | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | During initialization (startup) Telegram bot | `TelegramBot` |

  ### Events Playerok (PLAYEROK_EVENT_HANDLERS)

  Events received in the event listener in Playerok both.

  | Event | When | is called Passed Arguments |
  |-------|------------------|------------------------|
  | `EventTypes.CHAT_INITIALIZED` | Chat initialized | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | New chat message | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | A new transaction was created (when the buyer paid for the item) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.NEW_REVIEW` | New review of the deal | `PlayerokBot`, `NewReviewEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Deal confirmed | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | The seller issued a refund of the transaction | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | The user reported a problem with the transaction | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | The problem in the deal has been resolved | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Transaction status changed | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | The user paid for the item | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Item shipped (seller confirmed transaction completed) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Module structure</strong></summary>  
  
  </br>A module is a folder that contains important components. You can study the structure of a module based on the [template module](.templates/forms_module), but you should understand that this is just an example made by us.

  Mandatory handler constants:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | This dictionary defines bot event handlers |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | This dictionary defines event handlers Playerok |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | This array specifies modular routers Telegram bot |

  Required metadata constants:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `PREFIX` | `str` | Prefix |
  | `VERSION` | `str` | Version |
  | `NAME` | `str` | Title |
  | `DESCRIPTION` | `str` | Description |
  | `AUTHORS` | `str` | Author |
  | `LINKS` | `str` | Author links |

  Also, if a module requires additional dependencies, it must have a dependency file**requirements.txt**, which will be downloaded themselves when all bot modules are loaded.

  #### 🔧 Sample content:
  Please note that the metadata was placed in a separate file `meta.py`, but are imported into `__init__.py`.
  This is done to avoid import conflicts in the further part of the module code.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Test module. /test_module V Telegram bot for management"
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
          print(f"{PREFIX} The module is connected and active")
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
  
  ### 📝 Customized configuration file and data file wrappers
  Instead of once again struggling with configuration files and writing code to manage them, we have prepared a ready-made solution for you.
  The bot has already configured classes in the files [`settings.py`](settings.py) and [`data.py`](data.py)

  #### How does this work?
  Let's say you want to create a configuration file in your module, for this you will need to create a file `settings.py` in the root of the module folder.
  Contents`settings.py` should be something like this:
  ```python
  import os
  from settings import (
      Settings as sett,
      SettingsFile
  )


  CONFIG = SettingsFile(
      name="config", #  configuration file name
      path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"), #  path to the configuration file (in this case relative to the module folder)
      need_restore=True, #  do I need to restore the config?
      default={
          "bool_param": True,
          "str_param": "qwerty",
          "int_param": 123
      } #  standard file content
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

  The configuration file is specified using the ` dataclassSettingsFile`, which in turn is transferred to the array `DATA`.
  
  Next, you can get data from the config or save data to the config like this:
  ```python
  from . import settings as sett

  config = sett.get("config") #  we get the config
  print(config["bool_param"]) # -> True
  print(config["str_param"]) #  -> qwerty
  print(config["int_param"]) #  -> 123
  config["bool_param"] = False
  config["str_param"] = "uiop"
  config["int_param"] = 456
  sett.set("config", config) #  set the config to a new value
  ```

  By assigning a new value to the config, it is immediately written to its file. Also, upon receipt, the current data is taken from the file.

  Description of dataclass arguments `SettingsFile`:
  | Argument | Description |
  |----------|----------|
  | `name` | The name of the configuration file that we will use when receiving and writing |
  | `path` | Path to configuration file |
  | `need_restore` | Do I need to restore the config? Let's say you have added new data to the standard config value, but it is missing from the previously created **previously** configuration file. If the parameter is enabled, the script will check the current config data with the standard ones specified, and if the current data does not contain one or another key that is in the standard value, it will be automatically added to the config. Also, if the value type of a standard config key does not match the existing one (for example, the type in the file is **string**, and the standard value is **numeric**), this key in the current config will also be replaced with the standard value |
  | `default` | Default configuration file value |


  </br>The data file is structured in exactly the same way, but it is needed to store information collected by the script itself, and not specified by users.
  For example, you want to create a data file in your module, for this you will need to create a file `data.py` in the root of the module folder.
  
  Contents`data.py` should be something like this:
  ```python
  import os
  from data import (
      Data as data,
      DataFile
  )


  LATEST_EVENTS_TIMES = DataFile(
      name="new_forms", #  data file name
      path=os.path.join(os.path.dirname(__file__), "module_data", "new_forms.json"), #  path to the data file (in this case relative to the module folder)
      default={} #  standard file content
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

  Everything here is similar to the configuration file, only it serves a different task.


  ### 🔌 Convenient management of module states
  Using methods from `core/modules.py`, You can conveniently turn on/off/reboot the current module.
  In order to do this, you must first obtain UUID the currently running module, which is generated when it is initialized.
  
  For example, in the file `__init__.py` you can do this:
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

  And then manage the module in any convenient place:
  ```python
  from core.modules import enable_module, disable_module, reload_module

  from . import get_module


  await disable_module(get_module().uuid) #  turns off the module
  await enable_module(get_module().uuid) #  includes module
  await reload_module(get_module().uuid) #  reloads the module
  ```

</details>

<details>
  <summary><strong>❗ Notes</strong></summary>

  </br>Functional Telegram bot is written in the library aiogram 3, user functionality implementation system Telegram The bot works on the basis of routers, which merge with the main, main router of the bot.
  And the way they merge together, complications can arise if e.g. Callback the data has the same name. Therefore, after writing the functionality Telegram bot for the module, better rename it
  this data in a unique way so that it does not match the names of the main bot or additional plug-ins.

</details>


## 🔗 Useful links
- Developer: https://github.com/alleexxeeyy (The profile contains current links to all contacts for communication)
- Telegram channel: https://t.me/alexeyproduction
- Telegram bot for purchasing official modules: https://t.me/alexey_production_bot
