# Understanding Time & Space Complexity

## 🎯 The Problem: "I Don't Understand Big O"

**This guide makes complexity intuitive with visuals!**

---

## 🧠 What is Time Complexity?

**Simple definition:** How does runtime grow as input size grows?

**Think of it as:** "If I double the input, does my code take double the time? Four times? A million times?"

---

## 📊 Visual Guide to All Complexities

### O(1) - Constant Time

**What it means:** Time doesn't change with input size

**Visual:**
```
Input size:  1     10    100   1000
Time:        ●     ●     ●     ●
             Same time always!
```

**Examples:**
```python
# Access array by index
arr[5]  # O(1)

# Add to dictionary
dict[key] = value  # O(1)

# Math operation
result = a + b  # O(1)
```

**Mental model:** "Just one step, no matter what!"

---

### O(log n) - Logarithmic Time

**What it means:** Halve the problem each step

**Visual:**
```
Input size: 1000 elements

Step 1: Check middle (500 left)
Step 2: Check middle (250 left)
Step 3: Check middle (125 left)
...
Step 10: Found! (only 10 steps for 1000 elements!)

1000 → 500 → 250 → 125 → 63 → 32 → 16 → 8 → 4 → 2 → 1
```

**Growth:**
```
n = 10        → ~3 steps
n = 100       → ~7 steps
n = 1,000     → ~10 steps
n = 1,000,000 → ~20 steps (Amazing!)
```

**Examples:**
```python
# Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # Each iteration cuts half!
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Mental model:** "Cut problem in half repeatedly"

**Visual comparison:**
```
n = 1,000,000

O(n) algorithm:     1,000,000 operations
O(log n) algorithm:        20 operations

That's 50,000x faster! 🚀
```

---

### O(n) - Linear Time

**What it means:** Time grows directly with input

**Visual:**
```
Input size:  1     10    100   1000
Time:        ●     ●●●●● ●●●●● ●●●●●
            1x     10x   100x  1000x
            Direct proportion!
```

**Examples:**
```python
# Loop through array once
for num in arr:  # O(n)
    print(num)

# Find max in array
max_val = arr[0]
for num in arr:  # O(n)
    if num > max_val:
        max_val = num

# Hash map operations in loop
for num in arr:  # O(n)
    if num in hash_map:  # O(1) inside loop
        return True
    hash_map[num] = True
```

**Mental model:** "Touch each element once"

---

### O(n log n) - Linearithmic Time

**What it means:** Doing log(n) work for each of n items

**Visual:**
```
Merge Sort visualization:

Original:   [5, 2, 8, 1, 9, 3]  (6 elements)

Divide:     [5, 2, 8]  [1, 9, 3]  → log(n) levels
            [5,2] [8]  [1,9] [3]
            [5][2][8]  [1][9][3]

Merge:      [2,5] [8]  [1,9] [3]  → n work per level
            [2,5,8]    [1,3,9]
            [1,2,3,5,8,9]

Total: n × log(n)
```

**Growth:**
```
n = 10    → ~33 operations
n = 100   → ~664 operations
n = 1000  → ~9,966 operations
```

**Examples:**
```python
# Efficient sorting
arr.sort()  # O(n log n)

# Merge sort, quick sort, heap sort
```

**Mental model:** "Divide problem (log n) and solve each part (n)"

---

### O(n²) - Quadratic Time

**What it means:** Nested loops over input

**Visual:**
```
For n=4:
     0  1  2  3
   ┌──────────┐
0  │ ✓  ✓  ✓  ✓│
1  │    ✓  ✓  ✓│
2  │       ✓  ✓│
3  │          ✓│
   └──────────┘
   = 10 comparisons (roughly n²/2)

For n=10:  ~100 comparisons
For n=100: ~10,000 comparisons  😰
```

**Examples:**
```python
# Nested loop - check all pairs
for i in range(len(arr)):      # n times
    for j in range(i+1, len(arr)):  # n times
        if arr[i] + arr[j] == target:
            return [i, j]
# Total: O(n²)

# Bubble sort
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
```

**Mental model:** "Check every pair"

**Why it's slow:**
```
n = 1,000
O(n) = 1,000 operations
O(n²) = 1,000,000 operations (1000x slower!)
```

---

### O(2^n) - Exponential Time

**What it means:** Doubles with each additional input

**Visual:**
```
Fibonacci tree (naive recursion):

                fib(5)
               /      \
          fib(4)      fib(3)
          /    \      /     \
     fib(3) fib(2) fib(2) fib(1)
     /   \
 fib(2) fib(1)

Calls double at each level!
fib(5) → 15 calls
fib(10) → 177 calls
fib(20) → 21,891 calls
fib(30) → 2,692,537 calls 😱
```

**Growth:**
```
n = 10  → 1,024 operations
n = 20  → 1,048,576 operations
n = 30  → 1,073,741,824 operations (over 1 billion!)
```

**Examples:**
```python
# Naive Fibonacci
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)  # Two recursive calls!

# Generate all subsets
def subsets(nums):
    result = []
    def backtrack(start, path):
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i+1, path)
            path.pop()
    backtrack(0, [])
    return result
```

**Mental model:** "Try all possible combinations"

---

## 📈 Complexity Comparison Chart

```
Operations for different n:

n      O(1)  O(log n) O(n)   O(n log n) O(n²)     O(2^n)
────────────────────────────────────────────────────────
10     1     3        10     33         100       1,024
100    1     7        100    664        10,000    1.27×10³⁰
1,000  1     10       1,000  9,966      1,000,000 huge!

Visual scale (1ms per operation):
────────────────────────────────────────────────────────
10     instant  instant  instant  instant   instant   instant
100    instant  instant  instant  instant   instant   forever
1,000  instant  instant  0.001s   0.01s     1s        forever
```

**Rule of thumb:**
```
✅ Good:    O(1), O(log n), O(n), O(n log n)
⚠️  Okay:   O(n²) for small n (< 1000)
❌ Avoid:  O(2^n), O(n!) for large n
```

---

## 🎨 How to Calculate Complexity

### Rule 1: Single Loop = O(n)
```python
for i in range(n):  # O(n)
    print(i)
```

### Rule 2: Nested Loops = Multiply
```python
for i in range(n):           # O(n)
    for j in range(m):       # O(m)
        print(i, j)
# Total: O(n × m)

for i in range(n):           # O(n)
    for j in range(n):       # O(n)
        print(i, j)
# Total: O(n × n) = O(n²)
```

### Rule 3: Sequential = Add
```python
for i in range(n):   # O(n)
    print(i)

for j in range(m):   # O(m)
    print(j)

# Total: O(n + m)
# If n and m are same size: O(n)
```

### Rule 4: Halving = O(log n)
```python
while n > 0:
    print(n)
    n = n // 2  # Halving!
# O(log n)
```

### Rule 5: Drop Constants
```python
for i in range(n):       # O(n)
    print(i)

for j in range(n):       # O(n)
    print(j)

for k in range(n):       # O(n)
    print(k)

# Total: O(3n) = O(n)  (drop the 3)
```

### Rule 6: Drop Non-Dominant Terms
```python
for i in range(n):           # O(n)
    print(i)

for i in range(n):           # O(n)
    for j in range(n):       # O(n)
        print(i, j)

# Total: O(n + n²) = O(n²)  (drop the n)
```

---

## 🎯 Space Complexity

**What it means:** How much extra memory do we use?

### O(1) Space - Constant
```python
def sum_array(arr):
    total = 0  # One variable
    for num in arr:
        total += num
    return total
# Space: O(1) - just one variable!
```

### O(n) Space - Linear
```python
def double_array(arr):
    result = []  # New array
    for num in arr:
        result.append(num * 2)
    return result
# Space: O(n) - array of size n!

def frequency_count(arr):
    freq = {}  # Hash map
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    return freq
# Space: O(n) - hash map with n elements worst case
```

### O(log n) Space - Logarithmic
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid+1, right)
    else:
        return binary_search_recursive(arr, target, left, mid-1)

# Space: O(log n) - recursion stack depth is log(n)
```

---

## 💡 Practical Examples

### Example 1: Two Sum

```python
# Brute Force
def twoSum_brute(nums, target):
    for i in range(len(nums)):         # O(n)
        for j in range(i+1, len(nums)): # O(n)
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Time: O(n²) - nested loops
# Space: O(1) - no extra space

# Optimized
def twoSum_optimized(nums, target):
    seen = {}  # O(n) space
    for i, num in enumerate(nums):  # O(n) time
        if target - num in seen:    # O(1) lookup
            return [seen[target-num], i]
        seen[num] = i
    return []

# Time: O(n) - single loop
# Space: O(n) - hash map

Trade-off: Use O(n) space to get O(n) time! ✓
```

### Example 2: Find Maximum

```python
def find_max(arr):
    max_val = arr[0]
    for num in arr:  # O(n)
        if num > max_val:
            max_val = num
    return max_val

# Time: O(n) - must check every element
# Space: O(1) - one variable

Can we do better than O(n)?
NO! Must look at every element at least once.
```

### Example 3: Binary Search

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:  # O(log n)
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Time: O(log n) - halve each step
# Space: O(1) - few variables

Why O(log n)?
1000 → 500 → 250 → 125 → ... → 1
Only ~10 steps!
```

---

## 🎯 Quick Reference Table

| Pattern | Time | Space | Example |
|---------|------|-------|---------|
| Hash Map (lookup) | O(n) | O(n) | Two Sum |
| Two Pointers | O(n) | O(1) | Valid Palindrome |
| Sliding Window | O(n) | O(k) | Longest Substring |
| Binary Search | O(log n) | O(1) | Search in Sorted |
| DFS/BFS | O(V+E) | O(V) | Graph traversal |
| Sorting | O(n log n) | O(1) or O(n) | Sort array |
| Backtracking | O(2^n) | O(n) | All subsets |
| DP | O(n) or O(n²) | O(n) | Fibonacci |

---

## 💡 Tips for Interviews

### When They Ask "What's the Complexity?"

```
1. Count the loops
   - One loop = O(n)
   - Nested loops = O(n²)
   - Halving = O(log n)

2. Think about worst case
   - What's the maximum work?

3. Be clear
   - "Time complexity is O(n) because..."
   - "Space complexity is O(1) because..."

4. Mention trade-offs
   - "I'm using O(n) space to achieve O(n) time"
```

---

## 🚀 Practice

### Calculate complexity for these:

```python
# 1.
for i in range(n):
    print(i)
# Answer: O(n) time, O(1) space

# 2.
for i in range(n):
    for j in range(n):
        print(i, j)
# Answer: O(n²) time, O(1) space

# 3.
arr = []
for i in range(n):
    arr.append(i)
# Answer: O(n) time, O(n) space

# 4.
while n > 0:
    n = n // 2
# Answer: O(log n) time, O(1) space
```

---

## 🎓 Remember

**Big O is about GROWTH RATE, not exact operations!**

- O(2n) = O(n) - same growth rate
- O(n² + n) = O(n²) - n² dominates
- O(5) = O(1) - constant is constant

**Always think: "How does this scale with larger input?"**

---

## 📖 Next Steps

1. ✅ Understand each complexity intuitively
2. ✅ Practice calculating for code snippets
3. ✅ Use this guide during problem solving
4. ✅ Soon it becomes automatic!
