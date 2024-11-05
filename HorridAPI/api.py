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

    def qr(self, query=None): 
        if not query:
            raise ValueError("Please Give Any query")
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
        
    def gpt(self, query=None): 
        if not query:
            raise ValueError("Please Give any query add query=hi like that")
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

    def enhance(self, image=None):
        if not image:
            raise ValueError("Where the image If you don't know how to use this you can use Mangandi pip install mangandi")
        api = requests.post(f"{self.url}enhance", files={"image": image})
        bio = BytesIO(api.content)
        return bio

    def execute(self, code=None, language=None, version=None):  
        if not code:
            raise ValueError("where the code?")
        if not language:
            raise ValueError("where the language?")
        if not version:
            raise ValueError("Where the version?")
        api = requests.post(f"{self.url}execute", json={"code": code, "language": language, "version": version})
        return api.json()

    def imagine(self, prompt=None, api_key=None):
        if not prompt:
            raise ValueError("Where the prompt?")
        api = requests.get(f"{self.url}imagine?api_key={api_key}&prompt={prompt}")
        k = api.json()
        if not api_key:
            raise ValueError("Unauthorized You can get api key here https://t.me/XBOTSUPPORTS")
        if 'error' in k and 'Unauthorized' in k["error"]:
            raise ValueError("Unauthorized You can get api key here https://t.me/XBOTSUPPORTS")

        return api.content           

    def image_search(self, query=None):  
        if not query:
            raise ValueError("Where the query?")
        api = f'{self.url}image_search?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching image search response"   

    def images(self, query=None, page=6):  
        if not query:
            raise ValueError("Where the query?")
        api = f'{self.url}images?query={query}&page={page}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching image search response"   

    def instadl(self, url=None):  
        if not url:
            raise ValueError("Where the instgram url?")
        api = f'{self.url}instadl?url={url}'
        hehe = requests.get(api).json()
        if not hehe["STATUS"] == OK:
            raise ValueError("Its not a Instagram url")
        return hehe

    def logo(self, text=None):  
        if not text:
            raise ValueError("Give any name for the logo")
        api = f'{self.url}logo?text={text}'
        hehe = requests.post(api).json()
        return hehe

    def lyrics(self, song=None):  
        if not song:
            raise ValueError("Give any song name")
        api = f'{self.url}lyrics?song={song}'
        hehe = requests.get(api).json()
        return hehe

    def news(self, query=None):  
        if not query:
            raise ValueError("Give any query")
        api = f'{self.url}news?query={query}'
        hehe = requests.get(api).json()
        return hehe

    def proxy(self, url=None):  
        if not url:
            raise ValueError("Give an url")
        api = f'{self.url}proxy?url={url}'
        hehe = requests.get(api).json()
        return hehe

    def search(self, query=None, link=None):  
        if not query:
            raise ValueError("Give any query")
        if not link:
            raise ValueError("Give any image link")
        api = f'{self.url}search?query={query}&img={link}'
        hehe = requests.get(api).json()
        return hehe

    def wiki(self, query=None):  
        if not query:
            raise ValueError("Give any query")
        api = f'{self.url}wiki?query={query}'
        hehe = requests.get(api).json()
        return hehe

    def upscale(self, url=None, api_key=None, scale=8):
        if not url:
            raise ValueError("Give the image url")
        api = requests.get(f"{self.url}upscale?api_key={api_key}&url={url}&scale={scale}")
        k = api.json()
        if not api_key:
            raise ValueError("Unauthorized You can get api key here https://t.me/XBOTSUPPORTS")
        if 'error' in k and 'Unauthorized' in k["error"]:
            raise ValueError("Unauthorized You can get api key here https://t.me/XBOTSUPPORTS")

        return api.content
 
    def bard(self, query=None):    
        if not query:
            raise ValueError("Where the query?")
        api = f'{self.url}bard?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json()
        else:
            return f"Error fetching bard response: {res.status_code}"

    def aipro(self, botname, query, owner):       
        api = f'{self.url}aipro'        
        res = requests.post(api, json={'botname': botname, 'owner': owner, 'query': query})      
        return res.json()
        
    def llama(self, query=None):
        if not query:
            raise ValueError("Where the query?")
        """Fetches a response from the Horrid API's llama endpoint."""
        api = f'{self.url}llama?query={query}'
        res = requests.get(api)
        if res.status_code == 200:
            return res.json().get('response', 'No response found.')
        else:
            return f"Error fetching llama response: {res.status_code}"

api = HorridAPI()
