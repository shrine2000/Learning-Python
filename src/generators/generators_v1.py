"""
yield is a pause button.

When Python hits yield, the function freezes — it returns a value to the caller, but remembers exactly where it stopped. Next time you call next(), it resumes from that exact line.
"""


def demo():
    print("step 1")
    yield 10
    print("step 2")
    yield 20
    print("step 3")
    
    
g = demo()

print(next(g)) # step 1
print(g) # <generator object demo at 1b0>
print(type(g)) # <class 'generator'>

print(next(g)) # step 2 20

# print(next(g)) # step 3 -> StopIteration <- generator exhausted. 

print(next(g, None))  # returns None instead of raising