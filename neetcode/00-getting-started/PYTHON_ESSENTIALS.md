# 🐍 Python Essentials for DSA

**Everything you need to know about Python before solving DSA problems**

> This guide covers Python basics specifically for DSA interviews. If you're completely new to Python, spend 2-3 days here before starting DSA problems.

---

## 📚 Table of Contents

1. [Basic Syntax](#basic-syntax)
2. [Data Structures in Python](#data-structures-in-python)
3. [Essential Operations](#essential-operations)
4. [List Comprehensions](#list-comprehensions)
5. [Important Built-in Functions](#important-built-in-functions)
6. [Common DSA Patterns in Python](#common-dsa-patterns)
7. [Time Complexity Cheat Sheet](#time-complexity-cheat-sheet)
8. [Python Interview Tricks](#python-interview-tricks)
9. [Common Mistakes to Avoid](#common-mistakes-to-avoid)

---

## 🎯 Basic Syntax

### Variables and Types

```python
# Python is dynamically typed (no need to declare type)
x = 5              # int
y = 3.14           # float
name = "Alice"     # string
is_valid = True    # boolean

# Multiple assignment
a, b, c = 1, 2, 3

# Swap values (Python trick!)
a, b = b, a

# Type checking
type(x)           # <class 'int'>
isinstance(x, int)  # True
```

### Strings

```python
# String basics
s = "hello world"

# Indexing (0-based)
s[0]        # 'h'
s[-1]       # 'd' (last character)
s[-2]       # 'l' (second from last)

# Slicing [start:end:step]
s[0:5]      # 'hello'
s[:5]       # 'hello' (start defaults to 0)
s[6:]       # 'world' (end defaults to len)
s[::2]      # 'hlowrd' (every 2nd character)
s[::-1]     # 'dlrow olleh' (reverse!)

# Common methods
s.upper()              # 'HELLO WORLD'
s.lower()              # 'hello world'
s.split()              # ['hello', 'world']
s.split('o')           # ['hell', ' w', 'rld']
s.replace('world', 'python')  # 'hello python'
s.strip()              # Remove whitespace
s.startswith('hello')  # True
s.endswith('world')    # True
s.isdigit()           # False
s.isalpha()           # False (has space)

# String formatting
name = "Alice"
age = 25
f"My name is {name} and I'm {age}"  # f-strings (Python 3.6+)
"My name is {} and I'm {}".format(name, age)  # format()

# Character operations (important for DSA!)
ord('a')    # 97 (ASCII value)
chr(97)     # 'a' (character from ASCII)
ord('A')    # 65
ord('z') - ord('a')  # 25 (alphabet position)
```

### Numbers and Math

```python
# Arithmetic
10 + 3      # 13
10 - 3      # 7
10 * 3      # 30
10 / 3      # 3.333... (float division)
10 // 3     # 3 (integer division - IMPORTANT!)
10 % 3      # 1 (modulo - remainder)
2 ** 3      # 8 (exponentiation)

# Math operations
abs(-5)     # 5 (absolute value)
min(1, 2, 3)    # 1
max(1, 2, 3)    # 3
pow(2, 3)       # 8 (same as 2**3)
round(3.7)      # 4

# Math module
import math
math.ceil(3.2)   # 4 (round up)
math.floor(3.8)  # 3 (round down)
math.sqrt(16)    # 4.0
math.log(8, 2)   # 3.0 (log base 2)
math.inf         # Infinity (useful for DSA!)
-math.inf        # Negative infinity

# Infinity in comparisons
x = float('inf')
y = float('-inf')
x > 1000000     # True
```

---

## 📦 Data Structures in Python

### 1. Lists (Most Important!)

```python
# Creation
arr = [1, 2, 3, 4, 5]
empty = []
matrix = [[1, 2], [3, 4]]  # 2D list

# Accessing
arr[0]      # 1
arr[-1]     # 5
arr[1:3]    # [2, 3]

# Modifying
arr[0] = 10             # [10, 2, 3, 4, 5]
arr.append(6)           # [10, 2, 3, 4, 5, 6]
arr.insert(0, 0)        # [0, 10, 2, 3, 4, 5, 6]
arr.pop()               # Remove and return last: 6
arr.pop(0)              # Remove and return index 0: 0
arr.remove(10)          # Remove first occurrence of 10
del arr[0]              # Delete by index

# Useful operations
len(arr)                # Length
arr.count(3)            # Count occurrences
arr.index(3)            # Index of first occurrence
arr.reverse()           # Reverse in-place
arr.sort()              # Sort in-place
sorted(arr)             # Return sorted copy
arr.extend([7, 8])      # Add multiple elements

# List operations
arr1 + arr2             # Concatenate
arr * 3                 # Repeat
3 in arr                # Check membership
arr.clear()             # Remove all elements

# Common patterns for DSA
# Initialize with same value
zeros = [0] * 5         # [0, 0, 0, 0, 0]

# Initialize 2D array
matrix = [[0] * 3 for _ in range(4)]  # 4x3 matrix
# DON'T DO: [[0] * 3] * 4  (references same list!)

# Copy list
arr_copy = arr[:]       # Shallow copy
arr_copy = arr.copy()   # Shallow copy
import copy
arr_deep = copy.deepcopy(arr)  # Deep copy
```

**Time Complexity:**
```python
arr.append(x)       # O(1) amortized
arr.pop()           # O(1)
arr.pop(0)          # O(n) - avoid!
arr.insert(0, x)    # O(n) - avoid!
arr[i]              # O(1)
arr[i] = x          # O(1)
x in arr            # O(n)
arr.sort()          # O(n log n)
```

### 2. Dictionaries (Hash Maps)

```python
# Creation
d = {'a': 1, 'b': 2, 'c': 3}
empty = {}
d2 = dict(a=1, b=2, c=3)  # Alternative

# Accessing
d['a']              # 1
d.get('a')          # 1
d.get('z', 0)       # 0 (default if key doesn't exist)
d.get('z')          # None

# Modifying
d['d'] = 4          # Add/update
d.pop('a')          # Remove and return value
d.pop('z', None)    # Remove with default
del d['b']          # Delete key

# Checking
'a' in d            # True (check key)
'a' not in d        # False

# Iterating
for key in d:                   # Iterate keys
for key, value in d.items():    # Iterate key-value pairs
for value in d.values():        # Iterate values
for key in d.keys():            # Iterate keys (explicit)

# Useful methods
d.keys()            # dict_keys(['a', 'b', 'c'])
d.values()          # dict_values([1, 2, 3])
d.items()           # dict_items([('a', 1), ('b', 2), ('c', 3)])
d.clear()           # Remove all

# Default dict (useful for DSA!)
from collections import defaultdict

# Auto-initialize missing keys
count = defaultdict(int)        # Defaults to 0
count['a'] += 1                 # Works without initialization!

graph = defaultdict(list)       # Defaults to []
graph['a'].append('b')          # No KeyError!

# Counter (frequency counting)
from collections import Counter
arr = [1, 1, 2, 2, 2, 3]
freq = Counter(arr)             # Counter({2: 3, 1: 2, 3: 1})
freq.most_common(2)             # [(2, 3), (1, 2)]
```

**Time Complexity:**
```python
d[key] = value      # O(1) average
d[key]              # O(1) average
key in d            # O(1) average
d.pop(key)          # O(1) average
```

### 3. Sets (Hash Sets)

```python
# Creation
s = {1, 2, 3, 4, 5}
empty = set()       # NOT {} (that's empty dict!)
from_list = set([1, 2, 2, 3])  # {1, 2, 3}

# Operations
s.add(6)            # Add element
s.remove(6)         # Remove (raises error if not found)
s.discard(6)        # Remove (no error if not found)
s.pop()             # Remove and return arbitrary element

# Checking
3 in s              # True
len(s)              # Size

# Set operations (math!)
a = {1, 2, 3}
b = {3, 4, 5}

a | b               # {1, 2, 3, 4, 5} (union)
a & b               # {3} (intersection)
a - b               # {1, 2} (difference)
a ^ b               # {1, 2, 4, 5} (symmetric difference)

a.union(b)          # Same as a | b
a.intersection(b)   # Same as a & b
a.difference(b)     # Same as a - b

# Useful for DSA
# Remove duplicates
arr = [1, 2, 2, 3, 3, 3]
unique = list(set(arr))  # [1, 2, 3]

# Check if all unique
len(arr) == len(set(arr))  # False (has duplicates)
```

**Time Complexity:**
```python
s.add(x)            # O(1) average
s.remove(x)         # O(1) average
x in s              # O(1) average
```

### 4. Tuples (Immutable Lists)

```python
# Creation
t = (1, 2, 3)
t = 1, 2, 3         # Parentheses optional
single = (1,)       # Single element tuple (note comma!)

# Accessing (same as list)
t[0]                # 1
t[-1]               # 3
t[1:3]              # (2, 3)

# Useful for:
# 1. Multiple return values
def get_min_max(arr):
    return min(arr), max(arr)

minimum, maximum = get_min_max([1, 2, 3])

# 2. Dictionary keys (tuples are hashable!)
graph = {}
graph[(0, 1)] = 5   # Edge from 0 to 1 with weight 5

# 3. Tuple unpacking
a, b, c = (1, 2, 3)
```

### 5. Deque (Double-Ended Queue)

```python
from collections import deque

# Creation
q = deque([1, 2, 3])
q = deque()

# Operations (FAST on both ends!)
q.append(4)         # Add to right: [1, 2, 3, 4]
q.appendleft(0)     # Add to left: [0, 1, 2, 3, 4]
q.pop()             # Remove from right: 4
q.popleft()         # Remove from left: 0

# Access
q[0]                # First element
q[-1]               # Last element

# Why use deque?
# - O(1) operations on both ends
# - Use for queue (BFS) or stack
# - list.pop(0) is O(n), deque.popleft() is O(1)!

# Queue usage (BFS)
queue = deque([root])
while queue:
    node = queue.popleft()  # O(1)
    # process node...
    queue.append(node.left)
    queue.append(node.right)

# Stack usage (DFS)
stack = deque([root])
while stack:
    node = stack.pop()  # O(1)
    # process node...
```

### 6. Heap (Priority Queue)

```python
import heapq

# Python's heapq is a MIN heap by default
heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)

heapq.heappop(heap)     # Returns 1 (minimum)
heap[0]                 # Peek at minimum (don't pop)

# Create heap from list
arr = [3, 1, 4, 1, 5]
heapq.heapify(arr)      # O(n) - converts to heap

# Get k smallest/largest
heapq.nsmallest(2, arr)     # [1, 1]
heapq.nlargest(2, arr)      # [5, 4]

# Max heap trick (negate values!)
max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
heapq.heappush(max_heap, -2)
max_val = -heapq.heappop(max_heap)  # 3

# Heap with tuples (first element is priority)
heap = []
heapq.heappush(heap, (1, 'task1'))
heapq.heappush(heap, (3, 'task3'))
heapq.heappush(heap, (2, 'task2'))
priority, task = heapq.heappop(heap)  # (1, 'task1')
```

**Time Complexity:**
```python
heapq.heappush(heap, x)     # O(log n)
heapq.heappop(heap)         # O(log n)
heapq.heapify(arr)          # O(n)
heap[0]                     # O(1) peek
```

---

## ⚡ Essential Operations

### Sorting

```python
arr = [3, 1, 4, 1, 5]

# Sort in-place (modifies original)
arr.sort()              # [1, 1, 3, 4, 5]
arr.sort(reverse=True)  # [5, 4, 3, 1, 1]

# Return sorted copy
sorted_arr = sorted(arr)

# Custom sorting
# Sort by absolute value
arr = [-3, -1, 2, -4, 5]
arr.sort(key=abs)       # [-1, 2, -3, -4, 5]

# Sort by length (strings)
words = ['apple', 'pie', 'a', 'cherry']
words.sort(key=len)     # ['a', 'pie', 'apple', 'cherry']

# Sort tuples by second element
pairs = [(1, 3), (2, 1), (3, 2)]
pairs.sort(key=lambda x: x[1])  # [(2, 1), (3, 2), (1, 3)]

# Multiple criteria (sort by x, then by y)
points = [(1, 3), (1, 1), (2, 2)]
points.sort(key=lambda p: (p[0], p[1]))

# Reverse sort
arr.sort(reverse=True)
arr.sort(key=lambda x: -x)  # Same for numbers
```

### Iteration

```python
# Basic
for i in range(5):          # 0, 1, 2, 3, 4
for i in range(2, 5):       # 2, 3, 4
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8

# Reverse
for i in range(5, 0, -1):   # 5, 4, 3, 2, 1
for i in reversed(range(5)): # 4, 3, 2, 1, 0

# Enumerate (get index and value)
arr = ['a', 'b', 'c']
for i, val in enumerate(arr):
    print(f"{i}: {val}")    # 0: a, 1: b, 2: c

# Start enumeration from different number
for i, val in enumerate(arr, start=1):
    print(f"{i}: {val}")    # 1: a, 2: b, 3: c

# Zip (iterate multiple lists)
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Zip with indices
for i, (name, age) in enumerate(zip(names, ages)):
    print(f"{i}: {name} is {age}")
```

### Slicing (Very Important!)

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# arr[start:end:step]
arr[2:5]        # [2, 3, 4] (indices 2, 3, 4)
arr[:5]         # [0, 1, 2, 3, 4] (first 5)
arr[5:]         # [5, 6, 7, 8, 9] (from 5 to end)
arr[:]          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Step
arr[::2]        # [0, 2, 4, 6, 8] (every 2nd)
arr[1::2]       # [1, 3, 5, 7, 9] (every 2nd starting from 1)

# Reverse
arr[::-1]       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
arr[::-2]       # [9, 7, 5, 3, 1] (reverse every 2nd)

# Negative indices
arr[-3:]        # [7, 8, 9] (last 3)
arr[:-3]        # [0, 1, 2, 3, 4, 5, 6] (all except last 3)
arr[-5:-2]      # [5, 6, 7] (from -5 to -2)

# Modify with slicing
arr[2:5] = [10, 11, 12]  # Replace middle elements
arr[:3] = []             # Delete first 3 elements
```

---

## 🎨 List Comprehensions

```python
# Basic syntax: [expression for item in iterable if condition]

# Create list
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# If-else in expression
signs = [1 if x > 0 else -1 for x in [-2, -1, 0, 1, 2]]
# [-1, -1, -1, 1, 1]

# Nested loops
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# 2D matrix
matrix = [[i+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]  # [1, 2, 3, 4, 5, 6]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_lengths = {len(word) for word in ['hi', 'hello', 'hey']}
# {2, 3, 5}

# With enumerate
indexed = {i: val for i, val in enumerate(['a', 'b', 'c'])}
# {0: 'a', 1: 'b', 2: 'c'}
```

---

## 🔧 Important Built-in Functions

```python
# all() - check if all elements are True
all([True, True, True])     # True
all([True, False, True])    # False
all([1, 2, 3])              # True (non-zero is truthy)
all([])                     # True (vacuously true)

# any() - check if any element is True
any([False, False, True])   # True
any([False, False, False])  # False
any([])                     # False

# map() - apply function to all elements
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))  # [1, 4, 9, 16]

# Multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))  # [5, 7, 9]

# filter() - keep elements that satisfy condition
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4, 6]

# reduce() - reduce to single value
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)  # 24

# zip() - combine iterables
names = ['Alice', 'Bob']
ages = [25, 30]
list(zip(names, ages))  # [('Alice', 25), ('Bob', 30)]

# unzip
pairs = [('Alice', 25), ('Bob', 30)]
names, ages = zip(*pairs)  # ('Alice', 'Bob'), (25, 30)

# sum(), min(), max()
sum([1, 2, 3])          # 6
min([3, 1, 2])          # 1
max([3, 1, 2])          # 3

# With key function
words = ['apple', 'pie', 'cherry']
min(words, key=len)     # 'pie'
max(words, key=len)     # 'cherry'

# ord() and chr() - character/ASCII conversion
ord('a')                # 97
chr(97)                 # 'a'
```

---

## 💡 Common DSA Patterns in Python

### 1. Two Pointers

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process
        if condition:
            left += 1
        else:
            right -= 1
```

### 2. Sliding Window

```python
def sliding_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        # Slide window
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 3. Fast & Slow Pointers

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 4. DFS (Recursion)

```python
def dfs(node, visited):
    if not node or node in visited:
        return

    visited.add(node)

    for neighbor in node.neighbors:
        dfs(neighbor, visited)
```

### 5. BFS (Queue)

```python
from collections import deque

def bfs(root):
    queue = deque([root])
    visited = {root}

    while queue:
        node = queue.popleft()

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### 6. Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

### 7. Dynamic Programming

```python
# Top-down (memoization)
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Bottom-up (tabulation)
def fib_iterative(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

### 8. Backtracking

```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])  # Copy!
        return

    for choice in choices:
        # Choose
        path.append(choice)

        # Explore
        backtrack(path, remaining_choices)

        # Unchoose
        path.pop()
```

---

## ⏱️ Time Complexity Cheat Sheet

```python
# List operations
arr[i]                  # O(1)
arr.append(x)           # O(1) amortized
arr.insert(0, x)        # O(n) - SLOW!
arr.pop()               # O(1)
arr.pop(0)              # O(n) - SLOW!
x in arr                # O(n)
arr.sort()              # O(n log n)
arr.reverse()           # O(n)

# Dictionary operations
d[key]                  # O(1) average
d[key] = val            # O(1) average
key in d                # O(1) average
del d[key]              # O(1) average

# Set operations
s.add(x)                # O(1) average
s.remove(x)             # O(1) average
x in s                  # O(1) average
s1 & s2                 # O(min(len(s1), len(s2)))
s1 | s2                 # O(len(s1) + len(s2))

# Deque operations
q.append(x)             # O(1)
q.appendleft(x)         # O(1)
q.pop()                 # O(1)
q.popleft()             # O(1)

# Heap operations
heapq.heappush(h, x)    # O(log n)
heapq.heappop(h)        # O(log n)
heapq.heapify(arr)      # O(n)

# String operations
s[i]                    # O(1)
s + t                   # O(len(s) + len(t))
s * n                   # O(n * len(s))
s.split()               # O(n)
s.join(arr)             # O(sum of lengths)
```

---

## 🎯 Python Interview Tricks

### 1. Infinity

```python
# Use for initial values
min_val = float('inf')
max_val = float('-inf')

# Better than
min_val = 999999999  # What if input is larger?
```

### 2. Multiple Conditions

```python
# Check if x is between a and b
if a < x < b:  # Pythonic!

# Instead of
if x > a and x < b:
```

### 3. Swap Without Temp

```python
a, b = b, a  # Python magic!
```

### 4. Boolean as Integer

```python
True == 1   # True
False == 0  # True

# Count True values
count = sum([True, False, True, True])  # 3
```

### 5. Default Dict Patterns

```python
from collections import defaultdict

# Frequency count
freq = defaultdict(int)
for char in "hello":
    freq[char] += 1

# Graph adjacency list
graph = defaultdict(list)
graph[1].append(2)
graph[1].append(3)

# Group by key
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    groups[item.category].append(item)
```

### 6. Set for O(1) Lookup

```python
# Instead of
if x in [1, 2, 3, 4, 5]:  # O(n)

# Use
if x in {1, 2, 3, 4, 5}:  # O(1)
```

### 7. Reverse String/List

```python
s = "hello"
s[::-1]  # 'olleh'

arr = [1, 2, 3]
arr[::-1]  # [3, 2, 1]
```

### 8. Check if Power of 2

```python
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0
```

### 9. Count Set Bits

```python
def count_bits(n):
    return bin(n).count('1')
```

### 10. Generator for Memory Efficiency

```python
# Instead of creating entire list
squares = [x**2 for x in range(1000000)]  # Uses memory

# Use generator
squares = (x**2 for x in range(1000000))  # Lazy evaluation
```

---

## ❌ Common Mistakes to Avoid

### 1. Mutable Default Arguments

```python
# ❌ WRONG
def append_to(element, lst=[]):
    lst.append(element)
    return lst

append_to(1)  # [1]
append_to(2)  # [1, 2] - UNEXPECTED!

# ✅ CORRECT
def append_to(element, lst=None):
    if lst is None:
        lst = []
    lst.append(element)
    return lst
```

### 2. Shallow vs Deep Copy

```python
# ❌ WRONG
matrix = [[0] * 3] * 3  # All rows reference same list!
matrix[0][0] = 1
# [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - OOPS!

# ✅ CORRECT
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
# [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

### 3. Modifying List While Iterating

```python
# ❌ WRONG
arr = [1, 2, 3, 4, 5]
for x in arr:
    if x % 2 == 0:
        arr.remove(x)  # Skips elements!

# ✅ CORRECT
arr = [x for x in arr if x % 2 != 0]
# Or
arr[:] = [x for x in arr if x % 2 != 0]  # Modify in-place
```

### 4. Integer Division in Python 2 vs 3

```python
# Python 3
5 / 2   # 2.5 (float division)
5 // 2  # 2 (integer division)

# Always use // for integer division in interviews!
```

### 5. == vs is

```python
a = [1, 2, 3]
b = [1, 2, 3]

a == b  # True (same value)
a is b  # False (different objects)

# Use == for value comparison
# Use is for None, True, False
if x is None:  # ✅
if x == None:  # Works but not Pythonic
```

### 6. Not Copying When Needed

```python
# ❌ WRONG
original = [1, 2, 3]
copy = original
copy[0] = 99
print(original)  # [99, 2, 3] - OOPS!

# ✅ CORRECT
copy = original[:]  # or list(original) or original.copy()
copy[0] = 99
print(original)  # [1, 2, 3]
```

---

## 🎓 Practice Exercises

Test your Python knowledge with these:

```python
# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Find duplicates in list
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for x in arr:
        if x in seen:
            duplicates.add(x)
        seen.add(x)
    return list(duplicates)

# 4. Merge two dictionaries
def merge_dicts(d1, d2):
    result = d1.copy()
    result.update(d2)
    return result
    # Or in Python 3.9+: d1 | d2

# 5. Flatten nested list
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# 6. Group anagrams
def group_anagrams(words):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())
```

---

## 🚀 Next Steps

Once you're comfortable with these Python basics:

1. **Practice on easy problems** - Apply these concepts
2. **Read PATTERN_RECOGNITION.md** - Learn DSA patterns
3. **Start solving** - 01-arrays-hashing/easy problems
4. **Reference this guide** - Keep coming back!

**Important:** Don't spend more than 2-3 days on Python basics. Learn by doing DSA problems!

---

## 📚 Quick Reference

**Most Used in Interviews:**
- Lists, dicts, sets (90% of solutions)
- List comprehensions (clean code)
- defaultdict, Counter (frequency counting)
- deque (BFS/DFS)
- heapq (priority queue)

**Must Know:**
- Slicing `arr[start:end:step]`
- Sorting `sorted(arr, key=lambda x: x[1])`
- enumerate, zip
- `//` for integer division
- `**` for exponentiation
- `float('inf')` for infinity

**Practice Until Automatic:**
- Two pointers pattern
- Sliding window pattern
- Hash map for O(1) lookup
- Set for duplicates
- Binary search template

---

**Ready to start DSA?** Go to `QUICK_START.md` next! 🚀
