import requests


class CloudflareDetectedException(Exception):
    """
    Error detection Cloudflare protection at sending request.

    :param response: Object answer.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error: CloudFlare noticed suspicious activity at sending request on website Playerok."
            f"\nCode errors: {self.status_code}"
            f"\nAnswer: {self.html_text}"
        )
        return msg


class RequestFailedError(Exception):
    """
    Exception, which gets excited, If code answer Not equals 200.

    :param response: Object answer.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error request To {self.response.url}"
            f"\nCode errors: {self.status_code}"
            f"\nAnswer: {self.html_text}"
        )
        return msg


class RequestPlayerokError(Exception):
    """
    Exception, which gets excited, If arose error request on side Playerok.

    :param response: Object answer.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.json = response.json()
        self.error_code = self.json["errors"][0]["extensions"]["code"]
        self.error_message = self.json["errors"][0]["message"]

    def __str__(self):
        msg = (
            f"Error request To {self.response.url}"
            f"\nCode errors: {self.error_code}"
            f"\nMessage: {self.error_message}"
        )
        return self.error_message or msg


class RequestSendingError(Exception):
    """
    Exception, which gets excited, If Not succeeded send request for some attempts.

    :param url: URL request.
    :type url: `str`

    :param error: Text errors.
    :type error: `str`
    """

    def __init__(self, url: str, error: str):
        self.url = url
        self.error = error

    def __str__(self):
        msg = (
            f"Error at attempt send request To {self.url}"
            f"\nText errors: {self.error}"
        )
        return msg


class UnauthorizedError(Exception):
    """Exception, which gets excited, If Not succeeded log in V account Playerok."""

    def __str__(self):
        return "Not succeeded connect To account Playerok. Maybe You indicated incorrect token?"
