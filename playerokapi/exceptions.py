import requests

class BotCheckDetectedException(Exception):
    """
    Ошибка обнаружения проверки on бота при отправке запроса.

    :param response: Объект ответа.
    :type response: `requests.Response`
    """

    def __str__(self):
        msg = 'Bot-проверка заметила подозрительную активность при отправке запроса on сайт Playerok. Чтобы продолжить работу, вам нужно поменять параметр ddg5 on актуальный, или поменять cookies on актуальные.'
        return msg

class RequestFailedError(Exception):
    """
    Исключение, которое возбуждается, если код ответа не равен 200.

    :param response: Объект ответа.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = f'Request error {self.response.url}\nError code: {self.status_code}\nResponse: {self.html_text}'
        return msg

class RequestPlayerokError(Exception):
    """
    Исключение, которое возбуждается, если возникла ошибка запроса on стороне Playerok.

    :param response: Объект ответа.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.json = response.json()
        self.error_code = self.json['errors'][0]['extensions']['code']
        self.error_message = self.json['errors'][0]['message']

    def __str__(self):
        msg = f'Request error {self.response.url}\nError code: {self.error_code}\nMessage: {self.error_message}'
        return self.error_message or msg

class RequestSendingError(Exception):
    """
    Исключение, которое возбуждается, если не удалось отправить запрос за несколько попыток.

    :param url: URL запроса.
    :type url: `str`

    :param error: Error text.
    :type error: `str`
    """

    def __init__(self, url: str, error: str):
        self.url = url
        self.error = error

    def __str__(self):
        msg = f'Error when trying to send a request to {self.url}\nError text: {self.error}'
        return msg

class UnauthorizedError(Exception):
    """Исключение, которое возбуждается, если не удалось авторизоваться в аккаунте Playerok."""

    def __str__(self):
        return 'Не удалось подключиться к аккаунту Playerok. Может вы указали неверный token?'

class NotInitiatedError(Exception):
    """Исключение, которое возбуждается, если аккаунт Playerok не был инициализирован (не был вызван метод `get()`)."""

    def __str__(self):
        return 'Аккаунт Playerok не инициализирован для выполнения этого действия. Прежде чем сделать это, вызовите метод Account(...).get().'