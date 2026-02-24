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
                "✏️ Step 1. Enter full name (first, middle, last)",
                "",
                "💡 Example: John Michael Doe",
                "",
                "Enter your full name:"
            ]
        },
        "entering_fullname_error": {
            "enabled": True,
            "text": [
                "❌ Step 1. Full name input error",
                "",
                "Make sure the text matches the format",
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
                "Make sure you entered a number",
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
                "Make sure the text matches the format",
                "",
                "Enter your hobby again:"
            ]
        },
        "form_filled_out": {
            "enabled": True,
            "text": [
                "✅ Form has been filled out!",
                "",
                "Your data:",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !myform command to view your data again"
            ]
        },
        "cmd_myform": {
            "enabled": True,
            "text": [
                "📝 Your form",
                "",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !fill command to fill in the form again"
            ]
        },
        "cmd_myform_error": {
            "enabled": True,
            "text": [
                "❌ An error occurred while opening your form",
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