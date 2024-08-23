gemini = "1"
gemma = "2"
gemini_pro = 3
gemmaa = 4
gpt = 5


class models:
    """HorridAPI Model""" 

    def gemma():                
        out = "2"
        return out

    def gemma_2():                
        out = "4"
        return out

    def gemini_pro():                
        out = "3"
        return out
    
    def gpt():                
        out = "5"
        return out
        
    def gemini():                
        out = "1"
        return out

from telegraph import upload_file

class Core:
    """HorridAPI Core""" 
        
    def upload(url: str):                
        out = upload_file(url)
        put = f"https://telegra.ph/{out[0]}"
        return put
          
