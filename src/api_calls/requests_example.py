import requests
from dataclasses import dataclass


@dataclass
class Joke:
    id: int
    type: str
    setup: str
    punchline: str


data = requests.get("https://official-joke-api.appspot.com/jokes/1", timeout=5).json()
joke = Joke(**data)
print(joke)
