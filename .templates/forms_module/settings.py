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
                "✏️ Step 1. Enter surnames, name, middle names",
                "",
                "💡 For example: Petrov Ivan Olegovich",
                "",
                "Enter yours Full name:"
            ]
        },
        "entering_fullname_error": {
            "enabled": True,
            "text": [
                "❌ Step 1. Error input Full name",
                "",
                "Make sure, What text corresponds format",
                "",
                "Enter Full name again:"
            ]
        },
        "enter_age": {
            "enabled": True,
            "text": [
                "✏️ Step 2. Enter age",
                "",
                "💡 For example: 18",
                "",
                "Enter mine age:"
            ]
        },
        "entering_age_error": {
            "enabled": True,
            "text": [
                "❌ Step 2. Error input age",
                "",
                "Make sure, What You introduced numeric meaning",
                "",
                "Enter age again:"
            ]
        },
        "enter_hobby": {
            "enabled": True,
            "text": [
                "✏️ Step 3. Enter hobby",
                "",
                "💡 For example: Drawing",
                "",
                "Enter yours hobby:"
            ]
        },
        "entering_username_error": {
            "enabled": True,
            "text": [
                "❌ Step 3. Error input hobby",
                "",
                "Make sure, What text corresponds format",
                "",
                "Enter hobby again:"
            ]
        },
        "form_filled_out": {
            "enabled": True,
            "text": [
                "✅ Questionnaire was filled!",
                "",
                "Yours data:",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use team !my profile, to view data again"
            ]
        },
        "cmd_myform": {
            "enabled": True,
            "text": [
                "📝 Yours questionnaire",
                "",
                "・ Full name: {fullname}",
                "・ Age: {age}",
                "・ Hobby: {hobby}",
                "",
                "💡 Use team !fill out, to fill out questionnaire again"
            ]
        },
        "cmd_myform_error": {
            "enabled": True,
            "text": [
                "❌ At opening yours questionnaires happened error",
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