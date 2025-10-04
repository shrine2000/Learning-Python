from pathlib import Path


path = Path("example.txt")
with path.open("w", encoding="utf-8") as f:
    f.write("Hello, world!")

with path.open("r", encoding="utf-8") as f:
    context = f.read()
    print(context)
