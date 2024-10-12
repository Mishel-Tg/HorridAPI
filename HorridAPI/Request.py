# (c) @Mrz_bots


import json
import urllib.request
import urllib.parse

class Requests:
    def __init__(self):
        pass

    @staticmethod
    def get(url, params=None, **kwargs):
        """
        Send a GET request to the specified URL.

        Args:
            url (str): The URL to send the request to.
            params (dict): A dictionary of URL parameters to send with the request.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            response (str): The response from the server.
        """
        if params:
            url += "?" + urllib.parse.urlencode(params)
        req = urllib.request.Request(url, **kwargs)
        with urllib.request.urlopen(req) as response:
            return response.read().decode()

    @staticmethod
    def post(url, json=None, **kwargs):
        """
        Send a POST request to the specified URL.

        Args:
            url (str): The URL to send the request to.
            json (dict): A dictionary to send as JSON payload.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            response (str): The response from the server.
        """
        if json:
            kwargs["data"] = json.dumps(json).encode()
            kwargs["Content-Type"] = "application/json"
        req = urllib.request.Request(url, **kwargs)
        with urllib.request.urlopen(req) as response:
            return response.read().decode()

    @staticmethod
    def api(url, method, json=None, **kwargs):
        """
        Send a request to the specified API URL.

        Args:
            url (str): The API URL to send the request to.
            method (str): The HTTP method to use (e.g. "GET", "POST", etc.).
            json (dict): A dictionary to send as JSON payload.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            response (str): The response from the server.
        """
        if method == "GET":
            return Requests.get(url, **kwargs)
        elif method == "POST":
            return Requests.post(url, json, **kwargs)
        else:
            raise ValueError("Unsupported method")
