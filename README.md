# HorridAPI

<p align="center">
    <a href="https://github.com/Mishel-07/HorridAPI">
        <img src="https://img.shields.io/github/repo-size/Mishel-tg/HorridAPI?color=red&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-07/HorridAPI/commits/main">
        <img src="https://img.shields.io/github/last-commit/Mishel-tg/HorridAPI?color=brown&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-07/HorridAPI/issues">
        <img src="https://img.shields.io/github/issues/Mishel-tg/HorridAPI?color=blueviolet&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-07/HorridAPI/fork">
        <img src="https://img.shields.io/github/forks/Mishel-tg/HorridAPI?color=orange&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-07/HorridAPI/stargazers">
        <img src="https://img.shields.io/github/stars/Mishel-tg/HorridAPI?color=yellow&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://pypi.org/project/HorridAPI/">
        <img src="https://img.shields.io/pypi/v/HorridAPI?color=yellow&label=HorridAPI&logo=python&logoColor=blue&style=flat" />
    </a>
</p>

# Pip Install

``` 
pip install HorridAPI
```



# Mango 


### Mango Text Generation

```
from HorridAPI import Mango

mango = Mango()

response = mango.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.text)
```

### Mango Image Generation

```
from HorridAPI import Mango

mango = Mango()

response = mango.images.generate(
    model="flux-1.1-pro",
    prompt="a boy looking in the river"
)

print(response.url)
```


# Text to video 

This is a Python script that uses the HorridAPI to generate a video from a given text prompt. The script uses the LLVA API to create a realistic video from the text input.


### Obtaining an API Key

To get an API key, follow these steps:

1. Go to https://t.me/XBOTSUPPORTS
2. Follow the instructions to obtain an API key

### Example Code

```
from HorridAPI import LLVA

api_key = ""  # replace with your API key
prompt = "a girl and boy kissing"

k = LLVA(prompt=prompt, api_key=api_key)
video_path = k.generate_video()
print(video_path)
```


### Parameters

* prompt: the text input to generate a video from
* api_key: your HorridAPI key

# Hey there!

Welcome to my project! I'm excited to show you my powerful features. Here are some of the amazing things I can do:

AI Capabilities: I'm powered by artificial intelligence, which enables me to perform tasks with precision and speed.

Logo Maker: Need a logo for your business or project? I've got you covered! I can generate professional-looking logos in no time.

**Wiki:** Get instant access to a vast knowledge base with my built-in wiki feature. Search and learn from a vast repository of information.

**Image Search:** Find the perfect image for your project with my advanced image search feature. I can search through millions of images to find the one that fits your needs.



# song download

```
from HorridAPI import Songmrz

api_key = "horridapi_Db9RVKwf6zaBM8iatiQ4-Q_free_key"
s = Songmrz(api_key)

k = s.download("thallumaala")

title = k.title
url = k.url
print(url)
```




# Bard

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
ai = horrid.bard("hi")
print(ai)
```

# Upscale 

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
huhu = horrid.upscale(url="https://www.example.jpg", api_key="", scale=8) # you can get api key here https://t.me/XBOTSUPPORTS
print(huhu)
```


# Wiki

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
wiki = horrid.wiki("what is ai?")
print(wiki)
```

# Gemini image vision 

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
ne = horrid.search("today news", "https://www.example.jpg")
print(ne)
```

# Proxy scrapper 

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
proxy = horrid.proxy("https://www.google.com/")
print(proxy)
```

# news

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
news = horrid.news("today news")
print(news)
```

# lyrics

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
lyrics = horrid.lyrics("thallumaala") 
print(lyrics)
```

# Logo

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
logo = horrid.logo("mrz bots") 
print(logo)
```

# instadl

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
instadl = horrid.instadl("") # Your Instagram reel or photo story any url link
print(instadl)
```


# imagine

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
huhu = horrid.imagine(prompt="a cute cat", api_key="") # you can get api key here https://t.me/XBOTSUPPORTS
print(huhu)
```

# execute

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
execute = horrid.execute(code="print('hi')", language="python", version="*")
print(execute)
```

# Waifu image 

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
qr = horrid.waifu()
print(qr)
```

# Gpt

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
gpt = horrid.gpt("hi")
print(gpt)
```

# Qr

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
qr = horrid.qr("hi")
print(qr)
```

# Dare

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
dare = horrid.dare()
print(dare)
```

# Truth

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
truth = horrid.truth()
print(truth)

```
# Pinterest

```
from HorridAPI import HorridAPI

horrid = HorridAPI()
pinterest = horrid.pinterest("anime male character")
print(pinterest)
```

# Joke
```
from HorridAPI import HorridAPI

joke = HorridAPI()
he = joke.joke()
print(he)
```

# Llama
```
from HorridAPI import HorridAPI

api = HorridAPI()
ai = api.llama("who are you")
print(ai)
```

# Llama async 
```
from HorridAPI import Async

api = Async()
ai = await api.llama("who are you")
print(ai)
```

# image search async also using base url

```
from HorridAPI import Async

image = await Async().images(
        base_url="https://horrid-api.vercel.app/",
        query="gojo",
        page=7
   )

print(image)
```


# image search

```
from HorridAPI import HorridAPI 
image = await HorridAPI().images(
        base_url="https://horrid-api.vercel.app/",
        query="gojo",
        page=7
    )

print(image)

```


