import requests

def AiGenerativeContent(query, model):
    url = "https://horrid-api.onrender.com/ai"
    out = f"{url}?query={query}&model={model}"
    response = requests.post(out)
    if response.status_code == 200:
        return response.json()
    else:
        put = f"{url}?model={model}"
        res = requests.post(put, json=query)
        return res.json()
