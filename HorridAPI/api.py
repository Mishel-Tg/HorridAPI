from io import BytesIO
import requests
from urllib.parse import quote

class HorridAPI:
    """Horrid API Wrapper Class"""

    def __init__(self, url='https://horrid-api-yihb.onrender.com/'):
        self.url = url

    def joke(self):
        """Fetches a joke from the Horrid API."""
        api = f'{self.url}joke'
        res = requests.get(api).json()
        return res['joke']

    def truth(self):
        """Fetches a truth statement from the Horrid API."""
        api = f'{self.url}truth'
        res = requests.get(api).json()
        return res['truth']
      
    def dare(self):
        """Fetches a dare from the Horrid API."""
        api = f'{self.url}dare'
        res = requests.get(api).json()
        return res['dare']

    def ai(self, query: str, prompt: str):
        """Fetches a response from the Horrid API's Ai endpoint."""
        query = quote(query)
        api = f'{self.url}ai'
        headers = {"Content-Type": "application/json"}
        data = {"query": query, "prompt": prompt}        
        res = requests.post(api, headers=headers, json=data).json()
        return res['response']

    def qr(self, query: str):                
        url = f'{self.url}qr?text={query}'
        response = requests.get(url)
        img = BytesIO(response.content)
        return img

    def song(self, query: str):               
        api = f'{self.url}song?query={query}'
        res = requests.get(api).json()
        return res    
        
    def gpt(self, query: str):        
        prompt = quote(query)
        api = f'{self.url}gpt?query={prompt}'
        res = requests.get(api).json()
        return res    
        
    def llama(self, query: str):
        """Fetches a response from the Horrid API's llama endpoint."""
        prompt = quote(query)
        api = f'{self.url}llama?query={prompt}'
        res = requests.get(api).json()
        return res['response']        

api = HorridAPI()
