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
                "✏️ Step 1. Enter last name, first name, patronymic",
                "",
                "💡 For example: Petrov Ivan Olegovich",
                "",
                "Enter your full name:"
            ]
        },
        "entering_fullname_error": {
            "enabled": True,
            "text": [
                "❌ Step 1. Error entering full name",
                "",
                "Make sure the text matches the format",
                "",
                "Please enter your full name again:"
            ]
        },
        "enter_age": {
            "enabled": True,
            "text": [
                "✏️ Step 2. Enter your age",
                "",
                "💡 For example: 18",
                "",
                "Enter your age:"
            ]
        },
        "entering_age_error": {
            "enabled": True,
            "text": [
                "❌ Step 2. Error entering age",
                "",
                "Make sure you entered a numeric value",
                "",
                "Enter your age again:"
            ]
        },
        "enter_hobby": {
            "enabled": True,
            "text": [
                "✏️ Step 3. Enter a hobby",
                "",
                "💡 For example: Drawing",
                "",
                "Enter your hobby:"
            ]
        },
        "entering_username_error": {
            "enabled": True,
            "text": [
                "❌ Step 3: Hobby entry error",
                "",
                "Make sure the text matches the format",
                "",
                "Enter hobby again:"
            ]
        },
        "form_filled_out": {
            "enabled": True,
            "text": [
                "✅ The form has been filled out!",
                "",
                "Your details:",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the command !myprofile to view the data again"
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
                "💡 Use the !fill command to fill out the form again."
            ]
        },
        "cmd_myform_error": {
            "enabled": True,
            "text": [
                "❌ There was an error opening your profile",
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