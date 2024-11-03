import requests
from .models import hehmango  

class Mango:
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
        if model not in hehmango:
            raise ValueError("Invalid model")        
        if not model:
            raise ValueError("i can't find any model, You can see model here https://horridapi.onrender.com/mango")
        if not messages:
            raise ValueError("An error Report @XBOTSUPPORTS or https://github.com/Mishel-Tg/HorridAPI/issues")
        ms = {'messages': messages}        
        api = f"{self.chat.mango.base_url}?model={hehmango[model]}"  
        response = requests.post(api, json=ms)

        if response.status_code == 200:         
            return Choices(response.json())
        else:
            raise Exception(f"Error: Report  @XBOTSUPPORTS or https://github.com/Mishel-Tg/HorridAPI/issues")

class Choices:
    def __init__(self, response):          
        self.text = response["response"]


