import requests
from .models import models
from .payload import create_payload

class Mseed:
    def __init__(self, mongo_url):
        """
        Initialize the class with the MongoDB URL.

        Args:
            mongo_url (str): The URL of the MongoDB
        """
        self.mongo_url = mongo_url      

    def generate(self, system, prompt, user_id, model):
        """
        Generate content using the specified AI model.

        Args:
            payload (dict): The payload to generate content for.
            user_id (int): The ID of the user.
            model (str): The AI model to use.

        Returns:
            dict or str: The generated content as a dictionary if the response is successful, otherwise the error message as a string.
        """
        api = "https://horridapi.onrender.com/mango_generate"
        json = {"mongo_url": self.mongo_url, "system": system, "user_id": user_id, "model": model, "prompt": prompt}
        k = requests.post(api, json=json)      
        data = k.json()
        result = data["result"]
        return {"result": result}

    def delete_user_messages(self, user_id):
        """
        Delete all messages for a user.

        Args:
            user_id (int): The ID of the user.
        """
        k = "https://horridapi.onrender.com/mango_delete_user_messages"        
        json = {"user_id": user_id, "mongo_url": self.mongo_url}
        data = requests.post(k, json=json)
