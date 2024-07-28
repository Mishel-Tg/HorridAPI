import requests
from telegraph import upload_file


class models:
    """HorridAPI Core""" 
        
    def gemni():                        
        return "1"


class Core:
    """HorridAPI Core""" 
        
    def upload(url: str):                
        out = upload_file(url)
        return out
          
