import os
from settings import (
    Settings as sett,
    SettingsFile
)


CONFIG = SettingsFile(
    name="config",
    path=os.path.join(os.path.dirname(__file__), "module_settings", "config.json"),
    need_restore=True,
    default={
        "playerok": {
            "bot": {
                "log_states": True
            }
        }
    }
)

MESSAGES = SettingsFile(
    name="messages",
    path=os.path.join(os.path.dirname(__file__), "module_settings", "messages.json"),
    need_restore=True,
    default={
        "cmd_writein": {
            "enabled": True,
            "text": [
                "✏️ Step 1. Enter last name, first name, and patronymic",
                "",
                "💡 Example: Smith John Robert",
                "",
                "Enter your full name:"
            ]
        },
        "entering_fullname_error": {
            "enabled": True,
            "text": [
                "❌ Step 1. Full name input error",
                "",
                "Make sure the text matches the expected format",
                "",
                "Enter your full name again:"
            ]
        },
        "enter_age": {
            "enabled": True,
            "text": [
                "✏️ Step 2. Enter age",
                "",
                "💡 Example: 18",
                "",
                "Enter your age:"
            ]
        },
        "entering_age_error": {
            "enabled": True,
            "text": [
                "❌ Step 2. Age input error",
                "",
                "Make sure you entered a numeric value",
                "",
                "Enter your age again:"
            ]
        },
        "enter_hobby": {
            "enabled": True,
            "text": [
                "✏️ Step 3. Enter hobby",
                "",
                "💡 Example: Drawing",
                "",
                "Enter your hobby:"
            ]
        },
        "entering_username_error": {
            "enabled": True,
            "text": [
                "❌ Step 3. Hobby input error",
                "",
                "Make sure the text matches the expected format",
                "",
                "Enter your hobby again:"
            ]
        },
        "form_filled_out": {
            "enabled": True,
            "text": [
                "✅ The form has been completed!",
                "",
                "Your details:",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !my profile command to view your details again"
            ]
        },
        "cmd_myform": {
            "enabled": True,
            "text": [
                "📝 Your profile",
                "",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !fill in command to fill out the form again"
            ]
        },
        "cmd_myform_error": {
            "enabled": True,
            "text": [
                "❌ An error occurred while opening your profile",
                "",
                "{reason}"
            ]
        }
    }
)

DATA = [CONFIG, MESSAGES]


class Settings:
    
    @staticmethod
    def get(name: str) -> dict:
        return sett.get(name, DATA)

    @staticmethod
    def set(name: str, new: list | dict) -> dict:
        return sett.set(name, new, DATA)