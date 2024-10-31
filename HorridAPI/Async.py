from io import BytesIO
import requests
from urllib.parse import quote

class AsyncDd:
    """Horrid API Wrapper Class"""

    async def __init__(self, url='https://horridapi.onrender.com/'):
        self.url = url

    async def joke(self):
        """Fetches a joke from the Horrid API."""
        api = f'{self.url}joke'
        res = requests.get(api).json()
        return res['joke']

    async def truth(self):
        """Fetches a truth statement from the Horrid API."""
        api = f'{self.url}truth'
        res = requests.get(api).json()
        return res['truth']
      
    async def dare(self):
        """Fetches a dare from the Horrid API."""
        api = f'{self.url}dare'
        res = requests.get(api).json()
        return res['dare']

    async def qr(self, query: str):                
        url = f'{self.url}qr?text={query}'
        response = requests.get(url)
        img = BytesIO(response.content)
        return img

    async def song(self, query: str):               
        api = f'{self.url}song?query={query}'
        res = requests.get(api).json()
        return res    
        
    async def gpt(self, query: str):        
        prompt = quote(query)
        api = f'{self.url}gpt?query={prompt}'
        res = requests.get(api).json()
        return res    
        
    async def llama(self, query: str):
        """Fetches a response from the Horrid API's llama endpoint."""
        prompt = quote(query)
        api = f'{self.url}llama?query={prompt}'
        res = requests.get(api).json()
        return res['response']        

Async = AsyncDd()
