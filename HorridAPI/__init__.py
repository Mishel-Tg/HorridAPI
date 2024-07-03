
import requests
from urllib.parse import quote

__version__ = "0.6"

__all__ = ["api"]


class HorridAPI:
    """Horrid API Wrapper Class"""

    @staticmethod
    def joke():
        """Fetches a joke from the Horrid API."""
        api = f'https://horrid-api.onrender.com/joke'
        res = requests.get(api).json()
        return res['joke']

    @staticmethod
    def truth():
        """Fetches a truth statement from the Horrid API."""
        api = f'https://horrid-api.onrender.com/truth'
        res = requests.get(api).json()
        return res['truth']

    @staticmethod
    def dare():
        """Fetches a dare from the Horrid API."""
        api = f'https://horrid-api.onrender.com/dare'
        res = requests.get(api).json()
        return res['dare']

    @staticmethod
    def llama(query: str):
        """Fetches a response from the Horrid API's llama endpoint."""
        prompt = quote(query)
        api = f'https://horrid-api.onrender.com/llama?query={prompt}'
        res = requests.get(api).json()
        return res['response']

# Instead of creating an instance and shadowing the built-in function
# Use the class methods directly
api = HorridAPI()
