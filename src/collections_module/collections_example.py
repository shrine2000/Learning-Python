# collections — built-in specialized container types

from collections import defaultdict, Counter, deque, namedtuple


# 1. defaultdict — dict that never raises KeyError
word_groups = defaultdict(list)

words = ["apple", "ant", "banana", "avocado", "blueberry"]
for word in words:
    word_groups[word[0]].append(word)

print(dict(word_groups))
# {'a': ['apple', 'ant', 'avocado'], 'b': ['banana', 'blueberry']}


# 2. Counter — count occurrences
letters = Counter("banana")
print(letters)              # Counter({'a': 3, 'n': 2, 'b': 1})
print(letters.most_common(2))  # [('a', 3), ('n', 2)]
print(letters["z"])         # 0 — missing key returns 0, not KeyError


# 3. deque — fast append/pop from both ends
# list.insert(0, x) is O(n), deque.appendleft(x) is O(1)

d = deque([1, 2, 3])
d.append(4)       # add to right
d.appendleft(0)   # add to left
print(d)          # deque([0, 1, 2, 3, 4])

d.pop()           # remove from right
d.popleft()       # remove from left
print(d)          # deque([1, 2, 3])

# fixed-size sliding window
recent = deque(maxlen=3)
for i in range(6):
    recent.append(i)
print(recent)  # deque([3, 4, 5], maxlen=3) — oldest auto-dropped


# 4. namedtuple — tuple with named fields
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)

print(p.x, p.y)   # 3 4
print(p[0], p[1]) # 3 4 — still indexable
print(p)          # Point(x=3, y=4)
