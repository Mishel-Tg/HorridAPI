import requests

class Mango:
    """
    A class to generate content using AI models.
    """

    def __init__(self, base_url="https://horrid-api.vercel.app/mango", **kwargs):
        """
        Initialize the class with the base URL of the API.

        Args:
            base_url (str, optional): The base URL of the API. Defaults to "https://horridapi.onrender.com/mango".
        """
        self.base_url = base_url              
        self.chat = Chat(self)
        self.images = images(self)


class images:
    def __init__(self, mango, **kwargs):
        self.mango = mango
        
    def generate(self, model=None, prompt=None, **kwargs):
         if not model:
             raise ValueError("i can't find any model, You can see model here https://horrid-api.vercel.app/mango/imagine/models")
         if not prompt:
             raise ValueError("i can't find any prompt")  
         response = requests.get(f"{self.mango.base_url}/imagine?model={model}&prompt={prompt}")
         k = response.json()
         if "error" in k and "invalid model" in k["error"]:
             raise ValueError("Invalid model")
         if response.status_code == 200:         
             return URL(response.json())
         else:
             raise Exception(f"Error: Report  @XBOTSUPPORTS or https://github.com/Mishel-07/HorridAPI/issues")


class URL:
    def __init__(self, response, **kwargs):          
        self.url = response["image"]
        
class Chat:
    def __init__(self, mango, **kwargs):
        self.mango = mango
        self.completions = Completions(self)

class Completions:
    def __init__(self, chat, **kwargs):
        self.chat = chat

    def create(self, model=None, messages=None, **kwargs):                          
        if not model:
            raise ValueError("i can't find any model, You can see model here https://horrid-api.vercel.app/mango")
        if not messages:
            raise ValueError("An error Report @XBOTSUPPORTS or https://github.com/Mishel-07/HorridAPI/issues")
        ms = {'messages': messages}        
        api = f"{self.chat.mango.base_url}?model={model}"  
        response = requests.post(api, json=ms)
        k = response.json()
        if "messages" in k and "invalid model" in k["messages"]:
            raise ValueError("Invalid model")
        if response.status_code == 200:         
            return Choices(response.json())
        else:
            raise Exception(f"Error: Report  @XBOTSUPPORTS or https://github.com/Mishel-07/HorridAPI/issues")

class Choices:
    def __init__(self, response, **kwargs):          
        self.text = response["response"]


