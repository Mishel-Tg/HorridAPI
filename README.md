# HorridAPI

<p align="center">
    <a href="https://github.com/Mishel-tg/HorridAPI">
        <img src="https://img.shields.io/github/repo-size/Mishel-tg/HorridAPI?color=red&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-tg/HorridAPI/commits/main">
        <img src="https://img.shields.io/github/last-commit/Mishel-tg/HorridAPI?color=brown&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-tg/HorridAPI/issues">
        <img src="https://img.shields.io/github/issues/Mishel-tg/HorridAPI?color=blueviolet&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-tg/HorridAPI/fork">
        <img src="https://img.shields.io/github/forks/Mishel-tg/HorridAPI?color=orange&logo=github&logoColor=green&style=flat" />
    </a>
    <a href="https://github.com/Mishel-tg/HorridAPI/stargazers">
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
```
from HorridAPI import Mango

mango = Mango()

response = mango.chat.completions.create(
    model="gpt-3.5",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.text)
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
ai = api.llama("who are you")
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


# image search

```
from HorridAPI import HorridAPI 
image = await HorridAPI().images(
        base_url="https://horrid-api.vercel.app/",
        query="gojo",
        page=7
    )

print(image)


