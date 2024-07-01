import requests
from urllib.parse import quote

__version__ = "0.5"

__all__ = ["api"]


class HorridAPI:
    
    def __init__(self)->None:
        """     
        @Mrz_bots 
        """
        pass

    

    @staticmethod
    def joke():                
        api = f'https://horrid-api.onrender.com/joke'
        res = requests.get(api).json()
        k = res['joke']
        return k

    @staticmethod
    def truth():                
        api = f'https://horrid-api.onrender.com/truth'
        res = requests.get(api).json()
        k = res['truth']
        return k

    @staticmethod
    def dare():                
        api = f'https://horrid-api.onrender.com/dare'
        res = requests.get(api).json()
        k = res['dare']
        return k
        
    @staticmethod
    def llama(query: str):        
        prompt = quote(query)
        api = f'https://horrid-api.onrender.com/llama?query={prompt}'
        res = requests.get(api).json()
        k = res['response']
        return k


api=HorridAPI()
      
