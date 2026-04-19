The provided code is in Python, specifically for the AIogram framework, which is a popular Telegram bot platform. It appears to be a set of handlers for different states in a conversation flow.

Here's the translation:

1. `waiting_for_token`: 
   - Handles token input and validates it.
   - Sets the config with the provided token.
   - Sends a success message with the updated token.

2. `waiting_for_user_agent`:
   - Handles user agent input and validates it.
   - Sets the config with the provided user agent.
   - Sends a success message with the updated user agent.

3. `waiting_for_pl_proxy`:
   - Handles proxy input and validates it.
   - Sets the config with the provided proxy.
   - Sends a success message with the updated proxy.

4. `waiting_for_tg_proxy`:
   - Handles Telegram proxy input and validates it.
   - Sets the config with the provided Telegram proxy.
   - Sends a success message with the updated Telegram proxy.

5. `waiting_for_requests_timeout`:
   - Handles timeout input and validates it.
   - Sets the config with the provided timeout.
   - Sends a success message with the updated timeout.

6. `waiting_for_listener_requests_delay`:
   - Handles delay input and validates it.
   - Sets the config with the provided delay.
   - Sends a success message with the updated delay.

7. `waiting_for_tg_logging_chat_id`:
   - Handles Telegram logging chat ID input and validates it.
   - Sets the config with the provided chat ID.
   - Sends a success message with the updated chat ID.

8. `waiting_for_auto_withdrawal_interval`:
   - Handles auto withdrawal interval input and validates it.
   - Sets the config with the provided interval.
   - Sends a success message with the updated interval.

9. `waiting_for_sbp_bank_phone_number`:
   - Handles SBP bank phone number input and validates it.
   - Sets the config with the provided phone number.
   - Sends a success message with the updated phone number.

10. `waiting_for_usdt_address`:
    - Handles USDT TRC20 address input and validates it.
    - Sets the config with the provided address.
    - Sends a success message with the updated address.

11. `waiting_for_watermark_value`:
   - Handles watermark value input and validates it.
   - Sets the config with the provided watermark.
   - Sends a success message with the updated watermark.

12. `waiting_for_logs_max_file_size`:
   - Handles logs max file size input and validates it.
   - Sets the config with the provided maximum file size.
   - Sends a success message with the updated maximum file size.

Each handler checks if the provided input is valid, sets the corresponding config value, and sends a success message.

