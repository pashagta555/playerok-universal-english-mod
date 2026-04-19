The code you provided is a Python script, and it appears to be a bot that handles orders and calculates statistics. The script includes several functions:

1. `configure_config()`: This function prompts the user to input their Playerok account token, user agent, and proxy settings for both Playerok and Telegram. It also checks if the Playerok account is banned or the Telegram bot is not working.
2. `get_stats()`: This function calculates various statistics about orders, such as the number of active, completed, and refunded orders, as well as the total profit.

Here's a rough translation of the code:

```python
import pytz
import re
from datetime import datetime, timedelta

# Importing necessary libraries
import pytz
import re
from datetime import datetime, timedelta

# Getting configuration settings
config = get_config()

while not config["playerok"]["api"]["token"]:
    # Asking for Playerok account token and settings
    print("Please enter your Playerok account token:")
    playerok_token = input()
    if not is_pl_account_working(playerok_token):
        print("Invalid token. Please try again.")
        continue
    else:
        config["playerok"]["api"]["token"] = playerok_token

while not config["telegram"]["api"]["token"]:
    # Asking for Telegram bot settings
    print("Please enter your Telegram bot token:")
    telegram_token = input()
    if not is_tg_bot_exists(telegram_token):
        print("Invalid token. Please try again.")
        continue
    else:
        config["telegram"]["api"]["token"] = telegram_token

# Getting statistics about orders
stats = get_stats(config)

print("Statistics:")
print(f"Day: {stats['day']['orders']} orders, {stats['day']['active']} active, {stats['day']['completed']} completed, {stats['day']['refunded']} refunded, profit: ${stats['day']['profit']}, best item: {stats['day']['best']}")
print(f"Week: {stats['week']['orders']} orders, {stats['week']['active']} active, {stats['week']['completed']} completed, {stats['week']['refunded']} refunded, profit: ${stats['week']['profit']}, best item: {stats['week']['best']}")
print(f"Month: {stats['month']['orders']} orders, {stats['month']['active']} active, {stats['month']['completed']} completed, {stats['month']['refunded']} refunded, profit: ${stats['month']['profit']}, best item: {stats['month']['best']}")
print(f"All time: {stats['all']['orders']} orders, {stats['all']['active']} active, {stats['all']['completed']} completed, {stats['all']['refunded']} refunded, profit: ${stats['all']['profit']}, best item: {stats['all']['best']}")
```

Note that this translation is not exact and may contain errors. The original code likely contains more details and specific formatting for the output statistics.

