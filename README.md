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


# Usage
```
from HorridAPI import api
ai = api.llama("who are you")
print(ai)
```

# Mango Ai
```
from HorridAPI import Mango

mango = Mango()

response = mango.chat.completions.create(
    model="gpt-3.5",
    messages=[{"role": "user", "content": "Hello"}]
)

print(response.text)
```

# MangoSeed 

Introducing MangoSeed AI

MangoSeed is a super cool AI that offers the following features:

* User Data Storage: You can save user data to the AI, allowing for personalized experiences and tailored interactions.
* Upgradability: The AI can be upgraded to make it even more cool and advanced, ensuring it stays cutting-edge and efficient.

# MangoSeed sample code

```
from MangoSeed import Mseed
from MangoSeed.payload import create_payload

ai = Mseed("") # add here your mongo db

response = ai.generate(
            system="You are a Help full assistant, You act like a good human",
            prompt=query,
            user_id=message.from_user.id,
            model="gpt-3.5"
        )
print(response["result"])
```

# MangoSeed user message delete

how to delete that user message from db 🤔

here the code of delete user data 

```
from MangoSeed import Mseed

delete = Mseed("") # add here your mongo db url


delete.delete_user_messages(12345) # add here which user data you want delete that user id
```
