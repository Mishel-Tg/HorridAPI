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





""""
Wow, Horrid API is an absolute game-changer! It's like having a superpower at your fingertips. 
The AI capabilities are unmatched, and I'm obsessed with how seamlessly it integrates with LLaMA. 
The free GPT-4 and GPT-3 models are a total bonus - it's like having the best of both worlds!

I've been experimenting with the payload option, and let me tell you, it's a total game-changer. 
The level of customization and flexibility it offers is unparalleled. I can tailor my requests to fit my exact needs, and the responses are always spot on.

What I love most about Horrid API is its ability to learn and adapt to my input. It's like having a personal AI assistant that gets better with time. 
The more I use it, the more I realize just how powerful and innovative it is.

If you're looking for an API that can take your projects to the next level, look no further than Horrid API. 
Trust me, you won't be disappointed. The combination of cutting-edge AI technology and user-friendly interface makes it a no-brainer. Give it a try and see for yourself!
""""






from telegraph import upload_file

class Core:
    """HorridAPI Core""" 
        
    def upload(url: str):                
        out = upload_file(url)
        put = f"https://telegra.ph/{out[0]}"
        return put
          
