import requests
from .models import hehmango

class AiGenerative:
    """
    A class to generate content using AI models.
    """

    def __init__(self, base_url="https://horridapi.onrender.com/mango"):
        """
        Initialize the class with the base URL of the API.

        Args:
            base_url (str, optional): The base URL of the API. Defaults to "https://horrid-api-yihb.onrender.com/ai".
        """
        self.base_url = base_url
        self.models = hehmango            
        
    def Content(self, query, model):
        """
        Generate content using the specified AI model.

        Args:
            query (str): The query to generate content for.
            model (str): The AI model to use (either "bard" or "gpt").

        Returns:
            dict or str: The generated content as a dictionary if the response is successful, otherwise the error message as a string.
        """
        if model not in self.models:
            return "Invalid model. You Can Get model here https://horridapi.onrender.com/mango."

        url = f"{self.base_url}?model={self.models[model]}&query={query}"
        response = requests.post(url)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text   


AiGenerativeContent = AiGenerative()
