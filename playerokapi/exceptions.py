import requests 


class BotCheckDetectedException (Exception ):
    'Error detecting bot verification when sending a request.\n\n    :param response: The response object.\n    :type response: `requests.Response`'

    def __str__ (self ):
        msg =(
        'The verification bot noticed suspicious activity when sending a request to the Playerok website.'
        'To continue working, you need to change the ddg5 parameter to the current one, or change the cookies to the current ones.'
        )
        return msg 


class RequestFailedError (Exception ):
    'The exception that is thrown if the response code is not 200.\n\n    :param response: The response object.\n    :type response: `requests.Response`'

    def __init__ (self ,response :requests .Response ):
        self .response =response 
        self .status_code =self .response .status_code 
        self .html_text =self .response .text 

    def __str__ (self ):
        msg =(
        f"Ошибка запроса к {self .response .url }"
        f"\nКод ошибки: {self .status_code }"
        f"\nОтвет: {self .html_text }"
        )
        return msg 


class RequestPlayerokError (Exception ):
    'An exception that is thrown if there is a request error on the Playerok side.\n\n    :param response: The response object.\n    :type response: `requests.Response`'

    def __init__ (self ,response :requests .Response ):
        self .response =response 
        self .json =response .json ()
        self .error_code =self .json ['errors'][0 ]['extensions']['code']
        self .error_message =self .json ['errors'][0 ]['message']

    def __str__ (self ):
        msg =(
        f"Ошибка запроса к {self .response .url }"
        f"\nКод ошибки: {self .error_code }"
        f"\nСообщение: {self .error_message }"
        )
        return self .error_message or msg 


class RequestSendingError (Exception ):
    'The exception that is thrown if the request fails to be sent after several attempts.\n\n    :param url: Request URL.\n    :type url: `str`\n\n    :param error: Error text.\n    :type error: `str`'

    def __init__ (self ,url :str ,error :str ):
        self .url =url 
        self .error =error 

    def __str__ (self ):
        msg =(
        f"Ошибка при попытке отправить запрос к {self .url }"
        f"\nТекст ошибки: {self .error }"
        )
        return msg 


class UnauthorizedError (Exception ):
    'An exception that is raised if logging into the Playerok account failed.'

    def __str__ (self ):
        return 'Failed to connect to Playerok account. Maybe you specified the wrong token?'


class NotInitiatedError (Exception ):
    'An exception that is thrown if the Playerok account has not been initialized (the `get()` method has not been called).'

    def __str__ (self ):
        return (
        'The Playerok account is not initialized to perform this action.'
        'Before you do this, call the Account(...).get() method.'
        )
