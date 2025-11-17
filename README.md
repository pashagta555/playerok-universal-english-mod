# Playerok Universal

Modern assistant bot for Playerok 🤖🟦

## 🧭 Navigation:

-   [Bot features](#-features)
-   [Bot installation](#%EF%B8%8F-installation)
-   [Useful links](#-useful-links)
-   [For developers](#-for-developers)

## ⚡ Features

-   Modular system\
-   Convenient Telegram bot for configuring the bot (uses aiogram
    3.10.0)\
-   Basic functionality:
    -   Permanent online status on the site
    -   Automatic restoration of items after purchase with their
        previous priority status
    -   Welcome message
    -   Ability to add custom commands
    -   Ability to add custom auto-delivery for items
    -   `!seller` command to call the seller (notifies you in the
        Telegram bot that the buyer needs assistance)
-   Other minor features:
    -   Add/remove/edit watermark under bot messages
    -   Option to read/not read the chat before sending a message

and more.

## ⬇️ Installation

1.  Download the [latest Release
    version](https://github.com/alleexxeeyy/playerok-universal/releases/latest)
    and extract it anywhere you like.
2.  Make sure you have **Python version 3.x.x - 3.12** installed. If
    not, install it from
    https://www.python.org/downloads/release/python-31210 (during
    installation, enable `Add to PATH`).
3.  Open `install_requirements.bat` and wait for all required libraries
    to be installed, then close the window.
4.  To launch the bot, open `start.bat`.
5.  After the first launch, you will be prompted to configure the bot.

## 📚 For developers

The modular system helps implement additional functionality created by
enthusiasts. Essentially, it's similar to plugins, but in a more
convenient format.\
You can create your own module based on the
[template](.templates/forms_module).

```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}📌 Main events`</strong>`{=html}
```{=html}
</summary>
```
### Bot events (BOT_EVENT_HANDLERS)

Events triggered when certain bot actions occur.

  ------------------------------------------------------------------------------------
  Event                    When triggered              Passed arguments
  ------------------------ --------------------------- -------------------------------
  `ON_MODULE_ENABLED`      When a module is enabled    `Module`

  `ON_MODULE_DISABLED`     When a module is disabled   `Module`

  `ON_INIT`                When the bot initializes    `-`

  `ON_PLAYEROK_BOT_INIT`   When the Playerok bot       `PlayerokBot`
                           initializes                 

  `ON_TELEGRAM_BOT_INIT`   When the Telegram bot       `TelegramBot`
                           initializes                 
  ------------------------------------------------------------------------------------

### Playerok events (PLAYEROK_EVENT_HANDLERS)

Events received in the Playerok bot event listener.

  ------------------------------------------------------------------------------------------------
  Event                                When triggered              Passed arguments
  ------------------------------------ --------------------------- -------------------------------
  `EventTypes.CHAT_INITIALIZED`        Chat initialized            `PlayerokBot`,
                                                                   `ChatInitializedEvent`

  `EventTypes.NEW_MESSAGE`             New message in chat         `PlayerokBot`,
                                                                   `NewMessageEvent`

  `EventTypes.NEW_DEAL`                New deal created (when      `PlayerokBot`, `NewDealEvent`
                                       buyer pays for the item)    

  `EventTypes.NEW_REVIEW`              New review for a deal       `PlayerokBot`, `NewReviewEvent`

  `EventTypes.DEAL_CONFIRMED`          Deal confirmed              `PlayerokBot`,
                                                                   `DealConfirmedEvent`

  `EventTypes.DEAL_ROLLED_BACK`        Seller issued a refund      `PlayerokBot`,
                                                                   `DealRolledBackEvent`

  `EventTypes.DEAL_HAS_PROBLEM`        User reported a deal        `PlayerokBot`,
                                       problem                     `DealHasProblemEvent`

  `EventTypes.DEAL_PROBLEM_RESOLVED`   Deal problem resolved       `PlayerokBot`,
                                                                   `DealProblemResolvedEvent`

  `EventTypes.DEAL_STATUS_CHANGED`     Deal status changed         `PlayerokBot`,
                                                                   `DealStatusChangedEvent`

  `EventTypes.ITEM_PAID`               User paid for the item      `PlayerokBot`, `ItemPaidEvent`

  `EventTypes.ITEM_SENT`               Item sent (seller confirmed `PlayerokBot`, `ItemSentEvent`
                                       delivery)                   
  ------------------------------------------------------------------------------------------------

```{=html}
</details>
```
```{=html}
<details>
```
```{=html}
<summary>
```
`<strong>`{=html}📁 Module structure`</strong>`{=html}
```{=html}
</summary>
```
A module is a folder containing important components. You can study the
structure based on the [template module](.templates/forms_module), but
note that it is only an example.

Required handler constants: \| Constant \| Type \| Description \|
\|----------\|------\|-------------\| \| `BOT_EVENT_HANDLERS` \|
`dict[str, list[Any]]` \| Contains bot event handlers \| \|
`PLAYEROK_EVENT_HANDLERS` \| `dict[EventTypes, list[Any]]` \| Contains
Playerok event handlers \| \| `TELEGRAM_BOT_ROUTERS` \| `list[Router]`
\| Contains Telegram bot routers \|

Required metadata constants: \| Constant \| Type \| Description \|
\|----------\|------\|-------------\| \| `PREFIX` \| `str` \| Prefix \|
\| `VERSION` \| `str` \| Version \| \| `NAME` \| `str` \| Name \| \|
`DESCRIPTION` \| `str` \| Description \| \| `AUTHORS` \| `str` \|
Authors \| \| `LINKS` \| `str` \| Links to authors \|

If the module requires additional dependencies, include a
**requirements.txt** file. Dependencies will be installed automatically.

```{=html}
</details>
```
