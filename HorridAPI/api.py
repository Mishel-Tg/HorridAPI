from io import BytesIO
import requests

class HorridAPI:
    """Horrid API Wrapper Class"""

    def __init__(self, url='https://horridapi.onrender.com/'):
        self.url = url

    def joke(self):
        """Fetches a joke from the Horrid API."""
        api = f'{self.url}joke'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json().get('joke', 'No joke found.')
        else:
            return f"Error fetching joke: {res.status_code}"

    def truth(self):
        """Fetches a truth statement from the Horrid API."""
        api = f'{self.url}truth'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json().get('truth', 'No truth found.')
        else:
            return f"Error fetching truth: {res.status_code}"
      
    def dare(self):
        """Fetches a dare from the Horrid API."""
        api = f'{self.url}dare'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json().get('dare', 'No dare found.')
        else:
            return f"Error fetching dare: {res.status_code}"

    def qr(self, query):                
        url = f'{self.url}qr?text={query}'
        response = requests.get(url)
        if response.status_code == 200:
            img = BytesIO(response.content)
            return img
        else:
            return f"Error generating QR code: {response.status_code}"

    def song(self, query):               
        api = f'{self.url}song?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching song: {res.status_code}"
        
    def gpt(self, query):        
        api = f'{self.url}gpt?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching GPT response: {res.status_code}"

    def waifu(self):
        api = f'{self.url}anime/waifu'
        res = requests.get(api)
        if res.status_code == 200:
            img = BytesIO(res.content)
            return img
        else:
            return f"Error fetching waifu image: {res.status_code}"

    def bard(self, query):        
        api = f'{self.url}bard?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching bard response: {res.status_code}"

    def aipro(self, botname, query, owner):       
        api = f'{self.url}aipro'
        res = requests.post(api, json={'botname': botname, 'owner': owner, 'query': query)        
        return res.json()
        
    def llama(self, query):
        """Fetches a response from the Horrid API's llama endpoint."""
        api = f'{self.url}llama?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json().get('response', 'No response found.')
        else:
            return f"Error fetching llama response: {res.status_code}"

api = HorridAPI()
