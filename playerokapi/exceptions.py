import requests


class CloudflareDetectedException(Exception):
    """
    Raised when Cloudflare protection is detected on a request.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error: Cloudflare flagged suspicious activity on a request to Playerok."
            f"\nError code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestFailedError(Exception):
    """
    Raised when the response status code is not 200.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Request error for {self.response.url}"
            f"\nError code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestPlayerokError(Exception):
    """
    Raised when Playerok returns a GraphQL error.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.json = response.json()
        self.error_code = self.json["errors"][0]["extensions"]["code"]
        self.error_message = self.json["errors"][0]["message"]

    def __str__(self):
        msg = (
            f"Request error for {self.response.url}"
            f"\nError code: {self.error_code}"
            f"\nMessage: {self.error_message}"
        )
        return self.error_message or msg


class RequestSendingError(Exception):
    """
    Raised when the request could not be sent after several attempts.

    :param url: Request URL.
    :type url: `str`

    :param error: Error text.
    :type error: `str`
    """

    def __init__(self, url: str, error: str):
        self.url = url
        self.error = error

    def __str__(self):
        msg = (
            f"Error while sending request to {self.url}"
            f"\nError text: {self.error}"
        )
        return msg


class UnauthorizedError(Exception):
    """Raised when login to the Playerok account fails."""

    def __str__(self):
        return "Could not connect to the Playerok account. Did you enter a wrong token?"
