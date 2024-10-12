# made by @Mrz_bots

import requests
import os

class Requests:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_video(self, prompt):
        url = f"https://horridapi.onrender.com/txt2vid?prompt={prompt}&api_key={self.api_key}"
        response = requests.get(url)
        return response.content
