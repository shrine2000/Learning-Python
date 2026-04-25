from pathlib import Path


# pathlib approach
path = Path("example.txt")
with path.open("w", encoding="utf-8") as f:
    f.write("Hello, world!")

with path.open("r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# without path — plain string filename
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, world!")

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
