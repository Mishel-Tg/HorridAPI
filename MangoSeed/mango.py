from .models import models
from .payload import create_payload

class Mseed:
    def __init__(self, mongo_url):
        return None
    
    def model(self, model):
        """
        Get the model number from the model name.

        Args:
            model (str): The name of the model.

        Returns:
            int: The model number.
        """
        if model not in self.models:
            return "Invalid model. You Can Get model here https://horrid-api-yihb.onrender.com/ai."
        return self.models[model]

    def generate(self, system, prompt, user_id, model):        
        return {"result": "removed temporary"}

    def delete_user_messages(self, user_id):
        return None
