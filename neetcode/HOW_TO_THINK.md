# How to Think: Mental Framework for Problem Solving

## 🧠 The Problem: "My Mind Goes Blank When I See a Problem"

**This guide trains your mind to think systematically!**

---

## 🎯 The 7-Step Thinking Process

Use this EVERY TIME you see a problem. Make it a habit!

### Step 1: UNDERSTAND (2 minutes)

**What to do:**
```
□ Read the problem TWICE
□ Rephrase in your own words
□ Identify input and output
□ Check constraints
```

**Example:**
```
Problem: "Find two numbers in an array that sum to target"

Rephrase: "I have a list of numbers. I need to find which two add up to a specific value."

Input: Array of numbers + target number
Output: Two numbers (or their indices)
Constraints: Array unsorted, can have duplicates
```

**Visual Thinking:**
```
Input:  [2, 7, 11, 15], target = 9
Output: [2, 7]  (because 2 + 7 = 9)

Draw it:
2  7  11  15
↑  ↑
These sum to 9!
```

---

### Step 2: EXAMPLES (3 minutes)

**What to do:**
```
□ Create 2-3 small examples BY HAND
□ Include edge cases
□ Trace through what YOU would do
```

**Example:**
```
Problem: Find longest substring without repeating characters

Example 1: "abcabcbb"
Think:
- Start: "a" (length 1)
- Add "b": "ab" (length 2)
- Add "c": "abc" (length 3) ✓
- Add "a": Wait! "a" repeats!
  → Remove from left until no repeat
  → "bca"

So answer: 3 ("abc")

Example 2: "bbbbb"
All same! Answer: 1 ("b")

Example 3: "pwwkew"
Answer: 3 ("wke")
```

**Why this matters:**
- You discover the pattern BY DOING
- Your brain learns the logic before coding
- You catch edge cases early

---

### Step 3: BRUTE FORCE (1 minute)

**What to do:**
```
□ Think: "What's the SIMPLEST way?"
□ Don't worry about efficiency
□ Just get A solution
```

**Example:**
```
Problem: Two Sum

Brute force thinking:
"For each number, check EVERY OTHER number to see if they sum to target"

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]

Complexity: O(n²) - Too slow!
But at least I have A solution!
```

**Visual:**
```
[2, 7, 11, 15], target = 9

Check all pairs:
2+7=9 ✓ Found!
2+11=13
2+15=17
7+11=18
...

This works but checking n² pairs is slow
```

---

### Step 4: OPTIMIZE (5 minutes)

**What to do:**
```
□ Identify bottleneck in brute force
□ Ask: "What am I repeating?"
□ Think: "Can I trade space for time?"
□ Consider: Hash Map, Sorting, Two Pointers
```

**Optimization Checklist:**
```
Brute force is O(n²)?
  └→ Can hash map make it O(n)?  [YES often!]
  └→ Would sorting help? O(n log n)
  └→ Can two pointers work? O(n)

Need to find something quickly?
  └→ Hash map: O(1) lookup!

Need all combinations?
  └→ Might have to stay O(2^n)
```

**Example:**
```
Two Sum brute force: O(n²)

Bottleneck: "For each number, I search ALL others"

Optimize:
"What if I REMEMBER what I've seen?"
  ↓
HASH MAP!
  ↓
for each num:
    complement = target - num
    if complement in hash_map:
        Found!
    hash_map[num] = index

Complexity: O(n) ✓
```

**Visual Optimization:**
```
Instead of:
[2, 7, 11, 15]
 ↓   check all →

Do this:
Hash map: {2: 0}
See 7 → need 2 → CHECK MAP → Found!

One pass! O(n)
```

---

### Step 5: WALK THROUGH (3 minutes)

**What to do:**
```
□ Trace your optimized approach on paper
□ Use your Example 1
□ Step by step, like a computer
□ Check if it works
```

**Example:**
```
Two Sum with hash map
Input: [2, 7, 11, 15], target = 9

Step-by-step:
seen = {}

i=0, num=2
  complement = 9-2 = 7
  7 in seen? No
  seen = {2: 0}

i=1, num=7
  complement = 9-7 = 2
  2 in seen? YES! ✓
  return [seen[2], 1] = [0, 1]

✓ Works!
```

**Draw it:**
```
[2, 7, 11, 15]
 ↑
seen = {2:0}
    ↑
  Check for 7? Not yet

[2, 7, 11, 15]
    ↑
seen = {2:0}
    ↑
  Check for 2? YES! Found at index 0
```

---

### Step 6: CODE (5 minutes)

**What to do:**
```
□ Start with template (if you know the pattern)
□ Write step by step
□ Add comments for YOUR understanding
□ Handle edge cases
```

**Thinking while coding:**
```python
def twoSum(nums, target):
    # I need to remember what I've seen
    seen = {}  # value -> index

    # Check each number
    for i, num in enumerate(nums):
        # What number would make this work?
        complement = target - num

        # Have I seen that number before?
        if complement in seen:
            # Yes! Return both indices
            return [seen[complement], i]

        # No? Remember this number for later
        seen[num] = i

    # Didn't find anything
    return []
```

**Mental checklist while coding:**
```
□ Does this handle empty array?
□ What if no solution exists?
□ What if duplicate values?
□ Did I initialize variables?
□ Off-by-one errors?
```

---

### Step 7: TEST (2 minutes)

**What to do:**
```
□ Test with your Example 1
□ Test with edge cases
□ Trace through code line by line
□ Fix bugs
```

**Test cases to always check:**
```
□ Empty input: []
□ Single element: [1]
□ Two elements: [1, 2]
□ All same: [5, 5, 5]
□ No solution: [1, 2], target = 10
□ Duplicates: [3, 3], target = 6
```

**Example:**
```python
# Test 1: Normal case
twoSum([2, 7, 11, 15], 9)
# Trace: seen={2:0}, check 7, complement=2, found! ✓

# Test 2: Edge case
twoSum([3, 3], 6)
# Trace: seen={3:0}, check 3, complement=3, found! ✓

# Test 3: No solution
twoSum([1, 2], 10)
# Trace: Loop ends, return [] ✓
```

---

## 🎨 Visual Thinking Techniques

### Technique 1: Draw the Data Structure

**For Arrays:**
```
Draw boxes:
[1, 2, 3, 4, 5]
 ↑     ↑     ↑
 i     j     k
```

**For Trees:**
```
Draw the tree:
    1
   / \
  2   3
 / \
4   5
```

**For Graphs:**
```
Draw nodes and edges:
1 -- 2
|    |
3 -- 4
```

### Technique 2: Trace with Colors

**Use mental colors:**
```
[2, 7, 11, 15]
 🔴 (checking)

[2, 7, 11, 15]
 ✅  🔴 (found!)
```

### Technique 3: Think Step-by-Step

**Narrate to yourself:**
```
"I'm at index 0, value is 2"
"I need 7 to make 9"
"Is 7 in my hash map? No"
"Store 2 in map"
"Now I'm at index 1, value is 7"
"I need 2 to make 9"
"Is 2 in my map? YES!"
"Found the answer!"
```

### Technique 4: Use Real-World Analogies

**Hash Map = Phone Book**
```
"I'm looking for someone who can give me 7"
"Let me check my phone book (hash map)"
"Oh! I have 2's number, and 2 + 7 = 9!"
```

**Two Pointers = Two People Walking**
```
"Person A starts from left"
"Person B starts from right"
"They walk towards each other"
"They meet when sum = target"
```

---

## 🚀 Common Mental Blocks and How to Overcome Them

### Block 1: "I don't know where to start"

**Solution:**
```
Always start with:
1. Small example (3-4 elements)
2. Draw it
3. Solve BY HAND
4. What did YOU just do? That's the algorithm!
```

### Block 2: "I can't think of the optimal solution"

**Solution:**
```
1. Start with brute force
2. Identify what's slow
3. Ask: "What am I checking multiple times?"
4. Use hash map to remember things
5. Use sorting if order helps
```

### Block 3: "I don't know which pattern to use"

**Solution:**
```
Look for keywords:
- "pair/triplet" → Hash Map or Two Pointers
- "substring" → Sliding Window
- "sorted" → Binary Search or Two Pointers
- "all combinations" → Backtracking
- "maximum/minimum ways" → DP

When in doubt: Hash Map solves 40% of problems!
```

### Block 4: "I know the pattern but can't implement"

**Solution:**
```
1. Use the template from pattern guides
2. Modify template for your problem
3. Start with comments:
   # Step 1: Initialize hash map
   # Step 2: Loop through array
   # Step 3: Check if complement exists

4. Then fill in code for each comment
```

---

## 💡 Training Your Mind: Daily Practice

### Week 1-2: Pattern Recognition
```
Day 1-7: Do 2 hash map problems
Day 8-14: Do 2 two pointer problems

Goal: Recognize "Oh, this is a hash map problem!"
```

### Week 3-4: Template Mastery
```
Memorize templates for:
- Hash Map
- Two Pointers
- Sliding Window
- Binary Search

Goal: Code template from memory in 2 minutes
```

### Week 5-6: Speed
```
Solve same problems again
Time yourself
Goal: Recognize + code in 15 minutes
```

---

## 🎯 Thinking Checklist (Print This!)

```
When I see a problem:

□ Read twice and understand
□ Draw small example (3-4 elements)
□ Solve by hand - what did I do?
□ Identify the pattern (use PATTERN_RECOGNITION.md)
□ Think brute force first
□ Optimize (hash map? sorting? two pointers?)
□ Walk through on paper
□ Code with comments
□ Test with edge cases

Total time: 20 minutes
```

---

## 🎓 Remember

**Your brain is a pattern matching machine!**

The more problems you solve, the faster you'll recognize:
- "Oh, this is just like Two Sum!" → Hash Map
- "Oh, this is just like Valid Palindrome!" → Two Pointers
- "Oh, this is just like Longest Substring!" → Sliding Window

**It's not about memorizing solutions. It's about recognizing patterns!**

---

## 🚀 Next Steps

1. ✅ Read PATTERN_RECOGNITION.md
2. ✅ Read this guide (HOW_TO_THINK.md)
3. ✅ Use DECISION_TREE.md when solving
4. ✅ Practice 1 problem using this framework
5. ✅ Repeat until it becomes automatic!

**You got this!** 💪
