import requests


class CloudflareDetectedException(Exception):
    """
    Error detecting Cloudflare protection while sending a request.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error: CloudFlare detected suspicious activity while sending a request to Playerok."
            f"\nStatus code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestFailedError(Exception):
    """
    Error raised when the HTTP status code is not 200.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Request error to {self.response.url}"
            f"\nStatus code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestError(Exception):
    """
    Error raised when an error occurs while sending a request.

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
            f"Request error to {self.response.url}"
            f"\nError code: {self.error_code}"
            f"\nMessage: {self.error_message}"
        )
        return self.error_message or msg


class UnauthorizedError(Exception):
    """Error raised when authorization to the Playerok account fails."""

    def __str__(self):
        return "Failed to connect to the Playerok account. You may have provided an invalid token."
