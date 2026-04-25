# Type Hints — annotate variables and function signatures

from typing import Optional


# 1. Basic function annotations
def add(a: int, b: int) -> int:
    return a + b


def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}"


print(add(2, 3))        # 5
print(greet("Alice"))   # Hello, Alice


# 2. Optional — value can be None
def find_user(user_id: int) -> Optional[dict]:
    users = {1: {"name": "Alice"}}
    return users.get(user_id)  # returns dict or None


print(find_user(1))   # {'name': 'Alice'}
print(find_user(99))  # None


# 3. Union — one of several types (Python 3.10+ syntax: X | Y)
def parse_id(value: str | int) -> int:
    return int(value)


print(parse_id("42"))  # 42
print(parse_id(42))    # 42


# 4. List, dict, tuple with types
def sum_all(numbers: list[int]) -> int:
    return sum(numbers)


def get_scores() -> dict[str, int]:
    return {"Alice": 95, "Bob": 87}


def get_point() -> tuple[int, int]:
    return (3, 4)


# 5. Callable — annotate functions passed as arguments
from collections.abc import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)


print(apply(lambda x, y: x + y, 3, 4))  # 7


# 6. TypedDict — typed structure for dicts
from typing import TypedDict

class User(TypedDict):
    name: str
    age: int

def print_user(user: User) -> None:
    print(user["name"], user["age"])


print_user({"name": "Alice", "age": 30})
