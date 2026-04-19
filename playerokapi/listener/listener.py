Here is the translation of the given Python code to English:

The code appears to be a part of a web scraping or monitoring application that tracks chat messages and deals on a website. The translations are provided below:

1. `listen_new_messages()` function:
	* Waits for new chats to appear and checks if there are any new messages.
	* If there are, it processes the messages by calling `_proccess_new_chat_message()`.
	* It also waits for new deals to appear and processes them by calling `_process_chats_last_messages()`.
2. `listen_new_reviews()` function:
	* Waits for reviews on new deals to appear and checks if there are any.
	* If there are, it processes the reviews by calling `_proccess_new_chat_message()`.
3. `listen_deal_statuses()` function:
	* Monitors the status of all active deals and waits for changes.
	* When a change is detected, it calls `_parse_message_events()` to process the event.

The overall functionality of this code appears to be monitoring chat messages and deal reviews on a website, possibly with the goal of detecting new deals or processing user reviews.

