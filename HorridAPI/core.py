from telegraph import upload_file

class Core:
    """HorridAPI Core""" 
        
    def upload(url: str):                
        out = upload_file(url)
        put = f"https://telegra.ph/{out[0]}"
        return put
          
