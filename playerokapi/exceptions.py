import requests


class CloudflareDetectedException(Exception):
    """
    Cloudflare protection detection error when sending request.

    :param response: The response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error: CloudFlare detected suspicious activity when sending a request to the Playerok website."
            f"\nError code:{self.status_code}"
            f"\nAnswer:{self.html_text}"
        )
        return msg


class RequestFailedError(Exception):
    """
    The exception that is thrown if the response code is not 200.

    :param response: The response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Request error{self.response.url}"
            f"\nError code:{self.status_code}"
            f"\nAnswer:{self.html_text}"
        )
        return msg


class RequestPlayerokError(Exception):
    """
    An exception that is thrown if there is a request error on the Playerok side.

    :param response: The response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.json = response.json()
        self.error_code = self.json["errors"][0]["extensions"]["code"]
        self.error_message = self.json["errors"][0]["message"]

    def __str__(self):
        msg = (
            f"Request error{self.response.url}"
            f"\nError code:{self.error_code}"
            f"\nMessage:{self.error_message}"
        )
        return self.error_message or msg


class RequestSendingError(Exception):
    """
    The exception that is thrown if the request fails to be sent after several attempts.

    :param url: URL request.
    :type url: `str`

    :param error: Error text.
    :type error: `str`
    """

    def __init__(self, url: str, error: str):
        self.url = url
        self.error = error

    def __str__(self):
        msg = (
            f"Error when trying to send a request to{self.url}"
            f"\nError text:{self.error}"
        )
        return msg


class UnauthorizedError(Exception):
    """An exception that is raised if logging into the Playerok account failed."""

    def __str__(self):
        return "Failed to connect to Playerok account. Maybe you specified the wrong token?"
