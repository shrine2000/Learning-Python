import requests
from pydantic import BaseModel

class Joke(BaseModel):
    id: int
    type: str
    setup: str
    punchline: str


response = requests.get("https://official-joke-api.appspot.com/jokes/1", timeout=5)
data = response.json() 
joke = Joke(**data)
print(joke)
