# Playerok Universal
[![telegram](https://img.shields.io/badge/telegram-channel-blue?style=for-the-badge&logo=telegram)](https://t.me/alexeyproduction)
[![modules](https://img.shields.io/badge/%F0%9F%A7%A9%20bot-modules-green?style=for-the-badge)](https://t.me/alexey_production_bot)
[![python](https://img.shields.io/badge/python-3.12.x-yellow?style=for-the-badge&logo=python)](https://www.python.org/downloads/release/python-3119/)
[![stars](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.stargazers_count&style=for-the-badge&label=stars&color=43d433&logo=github)](https://github.com/alleexxeeyy/playerok-universal/stargazers)
[![forks](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fapi.github.com%2Frepos%2Falleexxeeyy%2Fplayerok-universal&query=%24.forks_count&style=for-the-badge&label=forks&color=%236c70e6&logo=github)](https://github.com/alleexxeeyy/playerok-universal/forks)

Modern bot-assistant For Playerok 🤖🟦

---

## 🗺️ Navigation
- [Functional bot](#-functional)
- [Installation bot](#%EF%B8%8F-installation)
- [Useful links](#-useful-links)
- [For developers](#-For-developers)

## 🔧 Functional
### 🤖💬 Telegram bot With complete management
- Configure any setting from the config in a few steps
- View bot statistics and account profile
- Bot event management

### ⚙️ Wide spectrum opportunities
- Module system (plugins connected to the bot)
- Always online on the website
- Auto-restore items
- Auto-bump items
- Auto-delivery goods
- Auto-withdrawal funds
- Automatic transaction confirmation
- Welcome message
- Custom commands
- Custom auto-delivery
- Team `!seller` For call seller V chat
- Editing And inclusion/shutdown everyone messages
- TG notifications for new messages, orders, reviews, etc.

### 🌐 More advanced
- Connection To proxy HTTPS IPv4
- Settings intervals requests

## ⬇️ Installation
1. Download [last Release version](https://github.com/alleexxeeyy/playerok-universal/releases/latest) And unpack V any comfortable For you place
2. Make sure, What at you installed **Python versions 3.12.x** (on others versions Job bot Not guaranteed). If Not installed, do This, passing By link https://www.python.org/downloads/release/python-31210/ (at installation click on paragraph `Add to PATH`)
3. Open `install_requirements.bat` And wait installations everyone necessary For work libraries, A after close window
4. To run bot, open launcher `start.bat`
5. After first launch you will ask tune bot For work

[Arose problems With installation? Click on me](https://telegra.ph/FunPay-Universal--chastye-oshibki-i-ih-resheniya-08-26)

## 📚 For developers

Modular system helps deploy V bot additional functional, made enthusiasts. By essentially, This same, What And plugins, But V more convenient format.
You you can create mine module, leaning on on [formulaic](.templates/forms_module).

<details>
  <summary><strong>📌 Basic events</strong></summary>

  ### Events bot (BOT_EVENT_HANDLERS)

  Events, which are being carried out at certain action bot.

  | Event | When called | Transmissible arguments |
  |-------|------------------|------------------------|
  | `ON_MODULE_ENABLED` | At inclusion module | `Module` |
  | `ON_MODULE_DISABLED` | At turning off module | `Module` |
  | `ON_INIT` | At initialization bot | `-` |
  | `ON_PLAYEROK_BOT_INIT` | At initialization (launch) Playerok bot | `PlayerokBot` |
  | `ON_TELEGRAM_BOT_INIT` | At initialization (launch) Telegram bot | `TelegramBot` |

  ### Events Playerok (PLAYEROK_EVENT_HANDLERS)

  Events, received V listener events V Playerok both.

  | Event | When called | Transmissible arguments |
  |-------|------------------|------------------------|
  | `EventTypes.CHAT_INITIALIZED` | Chat initialized | `PlayerokBot`, `ChatInitializedEvent` |
  | `EventTypes.NEW_MESSAGE` | New message V chat | `PlayerokBot`, `NewMessageEvent` |
  | `EventTypes.NEW_DEAL` | Created new deal (When buyer paid product) | `PlayerokBot`, `NewDealEvent` |
  | `EventTypes.NEW_REVIEW` | New review By deal | `PlayerokBot`, `NewReviewEvent` |
  | `EventTypes.DEAL_CONFIRMED` | Deal confirmed | `PlayerokBot`, `DealConfirmedEvent` |
  | `EventTypes.DEAL_ROLLED_BACK` | Salesman issued return deals | `PlayerokBot`, `DealRolledBackEvent` |
  | `EventTypes.DEAL_HAS_PROBLEM` | User reported O problem V deal | `PlayerokBot`, `DealHasProblemEvent` |
  | `EventTypes.DEAL_PROBLEM_RESOLVED` | Problem V deal resolved | `PlayerokBot`, `DealProblemResolvedEvent` |
  | `EventTypes.DEAL_STATUS_CHANGED` | Status deals changed | `PlayerokBot`, `DealStatusChangedEvent` |
  | `EventTypes.ITEM_PAID` | User paid item | `PlayerokBot`, `ItemPaidEvent` |
  | `EventTypes.ITEM_SENT` | Item sent (seller confirmed execution deals) | `PlayerokBot`, `ItemSentEvent` |

</details>

<details>
  <summary><strong>📁 Structure module</strong></summary>  
  
  </br>Module - This folder, inside which are important components. You you can study structure module, leaning on on [formulaic module](.templates/forms_module), But costs understand, What This only example, made us.

  Mandatory constants handlers:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `BOT_EVENT_HANDLERS` | `dict[str, list[Any]]` | IN this dictionary are given handlers events bot |
  | `PLAYEROK_EVENT_HANDLERS` | `dict[EventTypes, list[Any]` | IN this dictionary are given handlers events Playerok |
  | `TELEGRAM_BOT_ROUTERS` | `list[Router]` | IN this array are given routers modular Telegram bot  |

  Mandatory constants metadata:
  | Constant | Type | Description |
  |-----------|-----|----------|
  | `PREFIX` | `str` | Prefix |
  | `VERSION` | `str` | Version |
  | `NAME` | `str` | Name |
  | `DESCRIPTION` | `str` | Description |
  | `AUTHORS` | `str` | Authors |
  | `LINKS` | `str` | Links on authors |

  Also, If module requires additional dependencies, V him must be file dependencies **requirements.txt**, which will themselves download at loading everyone modules bot.

  #### 🔧 Example content:
  Please pay attention, What metadata were passed V separate file `meta.py`, But imported V `__init__.py`.
  This made For avoidance conflicts import V further parts code module.

  **`meta.py`**:
  ```python
  from colorama import Fore, Style

  PREFIX = f"{Fore.LIGHTCYAN_EX}[test module]{Fore.WHITE}"
  VERSION = "0.1"
  NAME = "test_module"
  DESCRIPTION = "Test module. /test_module V Telegram both For management"
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
          print(f"{PREFIX} Module connected And active")
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
  
  ### 📝 Customized wrappers files configurations And files data
  Instead of Togo, to extra once suffer With files configurations, writing code For departments them, We prepared For you ready solution.
  U bot There is already customized classes V files [`settings.py`](settings.py) And [`data.py`](data.py)

  #### How This works?
  Let's say, You want create file configurations V his module, For this to you need to will create file `settings.py` V root folders module.
  Content `settings.py` should be approximately next:
  ```python
  import os
  from settings import (
      Settings as sett,
      SettingsFile
  )


  CONFIG = SettingsFile(
      name="config", #  Name file configurations
      path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"), #  path To file configurations (V given case relatively folders module)
      need_restore=True, #  need to whether restore config
      default={
          "bool_param": True,
          "str_param": "qwerty",
          "int_param": 123
      } #  standard content file
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

  File configurations is given With with help dataclass `SettingsFile`, which V my queue, transmitted V array `DATA`.
  
  Next, get data from config or save data V config Can Here So:
  ```python
  from . import settings as sett

  config = sett.get("config") #  we get config
  print(config["bool_param"]) # -> True
  print(config["str_param"]) #  -> qwerty
  print(config["int_param"]) #  -> 123
  config["bool_param"] = False
  config["str_param"] = "uiop"
  config["int_param"] = 456
  sett.set("config", config) #  we ask config new meaning
  ```

  By asking config new meaning, it straightaway is recorded V his file. Also And at receiving, are taken current data from file.

  Description arguments dataclass `SettingsFile`:
  | Argument | Description |
  |----------|----------|
  | `name` | Name file configurations, which we will use at receiving And records |
  | `path` | Path To file configurations |
  | `need_restore` | Need to whether restore config? Let's say, V standard meaning config at you added new data, A V already created **previously** file configurations They none. If parameter included, script will check current data config with standard indicated, And If V current data Not will Togo or other key, which There is V standard meaning, He automatically will be added V config. So same, If type values key standard config Not corresponds existing (For example, V file **string** type, A V standard meaning **numerical**), Also this key V current config will replaced on standard meaning |
  | `default` | Standard meaning file configurations |


  </br>Exactly Also arranged And file data, But He needed For storage information, collected ourselves script, A Not specified users.
  For example, You want create file data V his module, For this to you need to will create file `data.py` V root folders module.
  
  Content `data.py` should be approximately next:
  ```python
  import os
  from data import (
      Data as data,
      DataFile
  )


  LATEST_EVENTS_TIMES = DataFile(
      name="new_forms", #  Name file data
      path=os.path.join(os.path.dirname(__file__), "module_data", "new_forms.json"), #  path To file data (V given case relatively folders module)
      default={} #  standard content file
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

  Here All similarly file configurations, only serves For another tasks.


  ### 🔌 Convenient control states module
  Using methods from `core/modules.py`, Can comfortable include/turn off/reboot current module.
  For Togo, to This do, need to before total get UUID current running module, which generated at his initialization.
  
  For example, V file `__init__.py` Can do So:
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

  A Then V any convenient place manage module:
  ```python
  from core.modules import enable_module, disable_module, reload_module

  from . import get_module


  await disable_module(get_module().uuid) #  turns off module
  await enable_module(get_module().uuid) #  includes module
  await reload_module(get_module().uuid) #  reboots module
  ```

</details>

<details>
  <summary><strong>❗ Notes</strong></summary>

  </br>Functional Telegram bot written on library aiogram 3, system implementation custom functionality Telegram bot works on basis routers, which merge With main, main router bot.
  AND So, How They merge together, can arise complications, If, For example Callback data have identical Name. That's why, after writing functionality Telegram bot For module, better rename
  these data unique way, to They Not coincided With names main bot or additional connected modules.

</details>


## 🔗 Useful links
- Developer: https://github.com/alleexxeeyy (V profile There is current links on All contacts For communications)
- Telegram channel: https://t.me/alexeyproduction
- Telegram bot For purchases official modules: https://t.me/alexey_production_bot
