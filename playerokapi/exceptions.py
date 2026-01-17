import requests


class CloudflareDetectedException(Exception):
    """
    Error detected by Cloudflare protection when sending a request.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.status_code = self.response.status_code
        self.html_text = self.response.text

    def __str__(self):
        msg = (
            f"Error: CloudFlare detected suspicious activity when sending a request to Playerok site."
            f"\nError code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestFailedError(Exception):
    """
    Error that is raised if the response status code is not 200.

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
            f"\nError code: {self.status_code}"
            f"\nResponse: {self.html_text}"
        )
        return msg


class RequestError(Exception):
    """
    Error that is raised if an error occurred when sending a request.

    :param response: Response object.
    :type response: `requests.Response`
    """

    def __init__(self, response: requests.Response):
        self.response = response
        self.json = response.json() or None
        self.error_code = self.json["errors"][0]["extensions"]["code"]
        self.error_message = self.json["errors"][0]["message"]

    def __str__(self):
        msg = (
            f"Request error to {self.response.url}"
            f"\nError code: {self.error_code}"
            f"\nMessage: {self.error_message}"
        )
        return msg


class UnauthorizedError(Exception):
    """Error that is raised if it failed to authorize in the Playerok account."""

    def __str__(self):
        return "Failed to connect to Playerok account. Maybe you specified an incorrect token?"
