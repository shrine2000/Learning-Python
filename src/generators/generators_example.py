# Generators — produce values one at a time using yield


# 1. Basic generator function
def count_up(start, end):
    while start <= end:
        yield start
        start += 1


for n in count_up(1, 5):
    print(n)  # 1 2 3 4 5


# 2. Generator expression (like list comprehension but lazy)
squares_list = [x ** 2 for x in range(5)]   # list — all in memory
squares_gen = (x ** 2 for x in range(5))    # generator — one at a time

for val in squares_gen:
    print(val)  # 0 1 4 9 16


# 3. next() — manually advance a generator
gen = count_up(1, 3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen)       # StopIteration — generator exhausted


# 4. Infinite generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for _ in range(8):
    print(next(fib), end=" ")  # 0 1 1 2 3 5 8 13
print()


# 5. yield from — delegate to another iterable
def flatten(nested):
    for sublist in nested:
        yield from sublist


result = list(flatten([[1, 2], [3, 4], [5]]))
print(result)  # [1, 2, 3, 4, 5]
