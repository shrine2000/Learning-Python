import csv
from pathlib import Path


data = [
    {"id": 1, "name": "porsche"},
    {"id": 2, "name": "audi"},
    {"id": 3, "name": "bmw"},
]

with Path("example.csv").open("w", encoding="utf-8") as f:
    writter = csv.DictWriter(f, fieldnames=["id", "name"])
    writter.writeheader()
    writter.writerows(data)


with Path("example.csv").open("r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
