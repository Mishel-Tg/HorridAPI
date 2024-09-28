import requests
from pymongo import MongoClient
from .models import models
from .payload import create_payload

class Mseed:
    def __init__(self, mongo_url, base_url="https://horridapi2-0.onrender.com/ai"):
        """
        Initialize the class with the base URL of the API and MongoDB URL.

        Args:
            mongo_url (str): The URL of the MongoDB.
            base_url (str, optional): The base URL of the API. Defaults to "https://horrid-api-yihb.onrender.com/ai".
        """
        self.base_url = base_url
        self.mongo_url = mongo_url
        self.client = MongoClient(self.mongo_url)
        self.db = self.client["mydatabase"]
        self.collection = self.db["users_messages"]
        self.models = models

    def mongo(self, mongo_url):
        """
        Update the MongoDB URL.

        Args:
            mongo_url (str): The new URL of the MongoDB.
        """
        self.mongo_url = mongo_url
        self.client = MongoClient(self.mongo_url)
        self.db = self.client["mydatabase"]
        self.collection = self.db["users_messages"]

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
        """
        Generate content using the specified AI model.

        Args:
            payload (dict): The payload to generate content for.
            user_id (int): The ID of the user.
            model (str): The AI model to use.

        Returns:
            dict or str: The generated content as a dictionary if the response is successful, otherwise the error message as a string.
        """
        model_number = self.model(model)
        if isinstance(model_number, str):
            return model_number

        api = f"{self.base_url}?model={model_number}"
        system = system
        prompt = prompt 
        resp = ""
        
        user_data = self.collection.find_one({"user_id": user_id})
        if user_data is None:
            user_data = {"user_id": user_id, "messages": [{"role": "system", "content": system}]}
        else:
            user_data = user_data

        user_data["messages"].append({"role": "user", "content": prompt})
        
        payload = {"messages": user_data["messages"]}
        response = requests.post(api, json=payload)
        resp = response.json()["response"]

        user_data["messages"].append({"role": "assistant", "content": resp})

        self.collection.update_one({"user_id": user_id}, {"$set": user_data}, upsert=True)

        return {"result": resp}

    def delete_user_messages(self, user_id):
        """
        Delete all messages for a user.

        Args:
            user_id (int): The ID of the user.
        """
        self.collection.delete_one({"user_id": user_id})
