The provided code is a part of an AIogram bot, a Python framework for building chatbots. It seems to be handling some custom command functionality. Here's the translation:

**Handler 1: Waiting for Custom Command Page**

This handler handles messages when the bot is waiting for a custom command page.

- If the message text contains only digits, it updates the state and sends a float message with settings-related text and a reply markup.
- If the message text does not contain digits or an error occurs, it sets the state to None, gets the current data, and sends a float message with an error text and a back button.

**Handler 2: Waiting for New Custom Command**

This handler handles messages when the bot is waiting for a new custom command.

- If the message text is empty or too long (less than 1 character or more than 32 characters), it raises an exception.
- It updates the state, saves the new custom command, sets the state to waiting for an answer, and sends a float message with settings-related text and a reply markup.

**Handler 3: Waiting for New Custom Command Answer**

This handler handles messages when the bot is waiting for an answer to a new custom command.

- If the message text is empty, it raises an exception.
- It updates the state, saves the answer, sets the state to None, and sends a float message with settings-related text and a reply markup containing a confirmation button.

**Handler 4: Waiting for Custom Command Answer**

This handler handles messages when the bot is waiting for an answer to a custom command.

- If the message text is empty, it raises an exception.
- It updates the state, saves the new custom commands, sets the state to None, and sends a float message with settings-related text and a reply markup containing a back button.

