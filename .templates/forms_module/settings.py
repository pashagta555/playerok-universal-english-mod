import os
from settings import Settings as sett, SettingsFile
CONFIG = SettingsFile(name='config', path=os.path.join(os.path.dirname(__file__), 'module_settings', 'config.json'), need_restore=True, default={'playerok': {'bot': {'log_states': True}}})
MESSAGES = SettingsFile(name='messages', path=os.path.join(os.path.dirname(__file__), 'module_settings', 'messages.json'), need_restore=True, default={'cmd_writein': {'enabled': True, 'text': ['✏️ Шаг 1. Ввод фамилии, имени, отчества', '', '💡 Например: Петров Иван Олегович', '', 'Enter your full name:']}, 'entering_fullname_error': {'enabled': True, 'text': ['❌ Шаг 1. Ошибка ввода ФИО', '', 'Убедитесь, что текст соответствует формату', '', 'Enter your full name again:']}, 'enter_age': {'enabled': True, 'text': ['✏️ Шаг 2. Ввод возраста', '', '💡 Например: 18', '', 'Enter your age:']}, 'entering_age_error': {'enabled': True, 'text': ['❌ Шаг 2. Ошибка ввода возраста', '', 'Убедитесь, что вы ввели числовое значение', '', 'Enter your age again:']}, 'enter_hobby': {'enabled': True, 'text': ['✏️ Шаг 3. Ввод хобби', '', '💡 Например: Рисование', '', 'Enter your hobby:']}, 'entering_username_error': {'enabled': True, 'text': ['❌ Шаг 3. Ошибка ввода хобби', '', 'Убедитесь, что текст соответствует формату', '', 'Enter hobby again:']}, 'form_filled_out': {'enabled': True, 'text': ['✅ The form has been completed!', '', 'Your details:', '・ ФИО: {fullname}', '・ Возраст: {age}', '・ Хобби: {hobby}', '', '💡 Используйте команду !mysurvey, чтобы просмотреть данные снова']}, 'cmd_myform': {'enabled': True, 'text': ['📝 Your questionnaire', '', '・ ФИО: {fullname}', '・ Возраст: {age}', '・ Хобби: {hobby}', '', '💡 Используйте команду !fill out, чтобы fill out анкету заново']}, 'cmd_myform_error': {'enabled': True, 'text': ['❌ There was an error opening your profile', '', '{reason}']}})
DATA = [CONFIG, MESSAGES]

class Settings:

    @staticmethod
    def get(name: str) -> dict:
        return sett.get(name, DATA)

    @staticmethod
    def set(name: str, new: list | dict) -> dict:
        return sett.set(name, new, DATA)