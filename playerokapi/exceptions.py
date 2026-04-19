import requests 


class CloudflareDetectedException (Exception ):
    "Error detection of Cloudflare protection when sending a request.

:param response: Response object.
:type response: requests.Response"

    def __init__ (self ,response :requests .Response ):
        self .response =response 
        self .status_code =self .response .status_code 
        self .html_text =self .response .text 

    def __str__ (self ):
        msg =(
        f"Ошибка: CloudFlare заметил подозрительную активность при отправке запроса на сайт Playerok."
        f"\nКод ошибки: {self .status_code }"
        f"\nОтвет: {self .html_text }"
        )
        return msg 


class RequestFailedError (Exception ):
    "Exception that is raised if the response code is not equal to 200.

    :param response: Object of response.
    :type response: requests.Response"

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
    "Exception that is raised if an error query occurred on the side of Playerok.

:param response: Object of answer.
:type response: requests.Response"

    def __init__ (self ,response :requests .Response ):
        self .response =response 
        self .json =response .json ()
        self .error_code =self .json ["errors"][0 ]["extensions"]["code"]
        self .error_message =self .json ["errors"][0 ]["message"]

    def __str__ (self ):
        msg =(
        f"Ошибка запроса к {self .response .url }"
        f"\nКод ошибки: {self .error_code }"
        f"\nСообщение: {self .error_message }"
        )
        return self .error_message or msg 


class RequestSendingError (Exception ):
    "Exception that is raised if it's impossible to send a request after several attempts.

:param url: URL of the request.
:type url: str

:param error: Error text.
:type error: str"

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
    "Exception that is triggered if it's impossible to authenticate in a Playerok account."

    def __str__ (self ):
        return "Couldn't connect to the Playerok account. Did you specify an incorrect token?"
