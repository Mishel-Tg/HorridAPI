import requests

class AiGenerativeContent:

    def HorridAPI(query, model):
        url = "https://horrid-api.onrender.com/ai"
        out = f"{url}?model={model}"
        response = requests.post(out, json=query)
        return response.text
        
    def Content(query, model):
        url = "https://horrid-api.onrender.com/ai"
        out = f"{url}?query={query}&model={model}"
        response = requests.post(out)
        return response.text
