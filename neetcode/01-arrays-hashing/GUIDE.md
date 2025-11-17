# Arrays & Hashing - Complete Guide

## 🎯 What is this pattern?

Arrays & Hashing is the **foundation** of data structures. This pattern teaches you how to:
- Store and access data efficiently
- Use hash tables (dictionaries in Python) for O(1) lookups
- Count frequencies
- Detect duplicates
- Group related elements

## 🧠 Core Concepts

### 1. Arrays
An array is a collection of elements stored in contiguous memory.

**Visual:**
```
Index:  0   1   2   3   4
Array: [5, 2, 8, 1, 9]
```

**Key Operations:**
- Access by index: O(1)
- Search for value: O(n)
- Insert/Delete at end: O(1)
- Insert/Delete at beginning/middle: O(n)

### 2. Hash Tables (Dictionaries)
A hash table stores key-value pairs for super-fast lookups.

**Visual:**
```
Key → Hash Function → Index in Array
"apple" → hash() → 5
"banana" → hash() → 12
```

**Python Implementation:**
```python
# Dictionary (Hash Map)
hash_map = {}
hash_map["key"] = "value"  # O(1) insert
value = hash_map["key"]     # O(1) lookup

# Set (Hash Set) - only stores keys
hash_set = set()
hash_set.add(5)             # O(1) insert
if 5 in hash_set:           # O(1) lookup
    print("Found!")
```

**Key Operations:**
- Insert: O(1) average
- Lookup: O(1) average
- Delete: O(1) average

## 🎨 Common Techniques

### Technique 1: Frequency Counting
Count how many times each element appears.

**Example:** Count character frequencies in "hello"
```python
freq = {}
for char in "hello":
    freq[char] = freq.get(char, 0) + 1
# Result: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

**Visualization:**
```
String: "hello"
h → 1
e → 1
l → 2  (appears twice!)
o → 1
```

### Technique 2: Duplicate Detection
Find if any element appears more than once.

**Approach 1: Using Set**
```python
def has_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Visualization:**
```
Array: [1, 2, 3, 1]
       ↓
Step 1: seen = {1}
Step 2: seen = {1, 2}
Step 3: seen = {1, 2, 3}
Step 4: 1 already in seen! → Return True
```

### Technique 3: Two-Pass Solution
First pass: collect information. Second pass: use that information.

**Example:** Find elements that appear twice
```python
# Pass 1: Count frequencies
freq = {}
for num in nums:
    freq[num] = freq.get(num, 0) + 1

# Pass 2: Find those with count = 2
result = []
for num, count in freq.items():
    if count == 2:
        result.append(num)
```

### Technique 4: Grouping/Categorizing
Group elements that share a property.

**Example:** Group anagrams
```python
from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        # Sort as key: "eat" → "aet"
        key = ''.join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

# ["eat", "tea", "tan", "ate", "nat", "bat"]
# → [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
```

**Visualization:**
```
"eat" → sorted → "aet" → group 1
"tea" → sorted → "aet" → group 1 (same key!)
"tan" → sorted → "ant" → group 2
"ate" → sorted → "aet" → group 1
```

### Technique 5: Complement Search
Find two elements that satisfy a relationship.

**Example:** Two Sum - find indices where nums[i] + nums[j] = target
```python
def two_sum(nums, target):
    seen = {}  # value → index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

**Visualization:**
```
nums = [2, 7, 11, 15], target = 9

i=0, num=2, complement=7, seen={} → seen={2:0}
i=1, num=7, complement=2, seen={2:0} → Found! Return [0,1]
```

## 🔑 When to Use This Pattern

Use Arrays & Hashing when you need to:
- ✅ Check if an element exists (use Set)
- ✅ Count frequencies (use Dictionary)
- ✅ Find duplicates
- ✅ Group elements by a property
- ✅ Fast lookups - "Have I seen this before?"
- ✅ Map one value to another

## ⚡ Complexity Analysis

| Operation | Array | Hash Table |
|-----------|-------|------------|
| Access by index | O(1) | N/A |
| Search for value | O(n) | O(1) avg |
| Insert | O(1) end, O(n) middle | O(1) avg |
| Delete | O(1) end, O(n) middle | O(1) avg |
| Space | O(n) | O(n) |

## 🎯 Problem-Solving Framework

### Step 1: Recognize the Pattern
Ask yourself:
- Do I need to check if something exists?
- Do I need to count occurrences?
- Do I need to group similar items?
- Can I trade space for time?

### Step 2: Choose Your Data Structure
- **Set**: For existence checks, duplicates
- **Dictionary**: For counting, mapping, grouping
- **Array**: For ordered data, index-based access

### Step 3: Write the Algorithm
```python
# Template for hash-based solutions
def solve(data):
    # Step 1: Initialize hash structure
    hash_map = {}  # or set()

    # Step 2: First pass - collect info
    for item in data:
        # Process and store in hash
        pass

    # Step 3: Second pass or return result
    # Use the collected information
    return result
```

## 📝 Common Problems in This Category

### Easy
1. Contains Duplicate - Use set to detect duplicates
2. Valid Anagram - Count character frequencies
3. Two Sum - Use hash map for complement search
4. Replace Elements with Greatest Element on Right Side

### Medium
5. Group Anagrams - Group by sorted string as key
6. Top K Frequent Elements - Frequency counting + sorting
7. Product of Array Except Self - Creative array manipulation
8. Valid Sudoku - Multiple hash sets
9. Longest Consecutive Sequence

### Hard
10. Minimum Window Substring - Sliding window + hash map

## 💡 Pro Tips

1. **Hash Map vs Hash Set**:
   - Use Set when you only care about existence
   - Use Dictionary when you need to store associated data

2. **Default Values**:
   ```python
   # Method 1: dict.get()
   count = freq.get(key, 0)

   # Method 2: collections.defaultdict
   from collections import defaultdict
   freq = defaultdict(int)
   ```

3. **Tuple as Key**:
   - Lists can't be dictionary keys (unhashable)
   - Use tuples instead: `key = tuple(sorted_list))`

4. **Order Matters?**:
   - Regular dict: Preserves insertion order (Python 3.7+)
   - Set: No ordering

## 🚀 Next Steps

1. Study the `template.py` file
2. Open `visualization.html` in your browser
3. Start with **Contains Duplicate** (easiest problem)
4. Progress through Easy → Medium → Hard

---

**Remember:** Hash tables are your best friend for interview problems. Master them! 🎯
