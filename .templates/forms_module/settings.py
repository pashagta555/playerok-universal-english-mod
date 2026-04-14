import os
from settings import (
    Settings as set,
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
                "✏️ Step 1. Introduction of families, names, fatherhoods",
                "",
                "💡 For example: Petrov Ivan Olegovich",
                "",
                "Enter your FIO:"
            ]
        },
        "entering_fullname_error": {
            "enabled": True,
            "text": [
                "❌ Step 1. FIO input error",
                "",
                "Make sure the text matches the format",
                "",
                "Enter the full name of the dream:"
            ]
        },
        "enter_age": {
            "enabled": True,
            "text": [
                "✏️ Step 2. Introduction of age",
                "",
                "💡 For example: 18",
                "",
                "Enter your age:"
            ]
        },
        "entering_age_error": {
            "enabled": True,
            "text": [
                "❌ Step 2. Age input error",
                "",
                "Make sure that you entered numerical value",
                "",
                "Enter the Age of Dreams:"
            ]
        },
        "enter_hobby": {
            "enabled": True,
            "text": [
                "✏️ Step 3. Introduction hobby",
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
                "Enter the dream hobby:"
            ]
        },
        "form_filled_out": {
            "enabled": True,
            "text": [
                "The survey was filled in!",
                "",
                "Your data:",
                "・ FIO: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !mysurvey command to view dream data"
            ]
        },
        "cmd_myform": {
            "enabled": True,
            "text": [
                "📝 Your Survey",
                "",
                "・ FIO: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use the !fill command to fill out the survey again"
            ]
        },
        "cmd_myform_error": {
            "enabled": True,
            "text": [
                "❌ There was an error opening your survey",
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