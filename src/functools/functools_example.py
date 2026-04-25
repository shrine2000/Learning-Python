# functools — tools for working with functions

from functools import lru_cache, partial, reduce, wraps


# 1. lru_cache — cache return values of a function
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))           # 55
print(fibonacci.cache_info())  # hits, misses, maxsize, currsize


# 2. partial — fix some arguments of a function
def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(4))  # 16
print(cube(3))    # 27


# 3. reduce — fold a list into a single value
numbers = [1, 2, 3, 4, 5]

total = reduce(lambda acc, x: acc + x, numbers)
print(total)  # 15

product = reduce(lambda acc, x: acc * x, numbers)
print(product)  # 120


# 4. wraps — keep original function name inside a decorator
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@log_call
def greet(name):
    """Say hello."""
    return f"Hello, {name}"


print(greet("Alice"))
print(greet.__name__)  # greet  (without @wraps this would be "wrapper")
print(greet.__doc__)   # Say hello.
