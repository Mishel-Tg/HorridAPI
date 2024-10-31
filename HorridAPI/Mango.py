import requests
from models import hehmango  

class Mangoo:
    """
    A class to generate content using AI models.
    """

    def __init__(self, base_url="https://horridapi.onrender.com/mango"):
        """
        Initialize the class with the base URL of the API.

        Args:
            base_url (str, optional): The base URL of the API. Defaults to "https://horridapi.onrender.com/mango".
        """
        self.base_url = base_url
        self.models = hehmango      
        self.chat = Chat(self)

class Chat:
    def __init__(self, mango):
        self.mango = mango
        self.completions = Completions(self)

class Completions:
    def __init__(self, chat):
        self.chat = chat

    def create(self, model=None, messages=None):
        if not model:
            raise ValueError("i can't find any model, You can see model here https://horridapi.onrender.com/mango")
        if not messages:
            raise ValueError("An error Report @XBOTSUPPORTS or https://github.com/Mishel-Tg/HorridAPI/issues")
        api = f"{self.chat.mango.base_url}?model={model}"  
        response = requests.post(api, json=messages)

        if response.status_code == 200:         
            return Choices(response.json())
        else:
            raise Exception(f"API request failed with status code: {response.status_code}")

class Choices:
    def __init__(self, response):      
        self.choices = response.get("response", "Api was Error")

Mango = Mangoo()  
