import json
from pathlib import Path

data = {"fruits": ["apple", "banana", "orange"]}

with Path("data.json").open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

with Path("data.json").open("r", encoding="utf-8") as f:
    loaded = json.load(f)
    print(loaded)
