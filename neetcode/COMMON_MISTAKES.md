# Common Mistakes & How to Avoid Them

**Learn from others' mistakes! This guide will save you weeks of frustration.**

---

## 🚫 Mistake #1: Jumping to Code Too Quickly

### The Mistake:
```
See problem → Start coding immediately → Get stuck → Give up
```

### Why It Happens:
- Feels productive to type code
- Impatient to "get it done"
- Skipping the thinking phase

### The Fix:
```
✅ READ problem twice
✅ DRAW small example (3-4 elements)
✅ SOLVE by hand first
✅ IDENTIFY pattern
✅ OUTLINE approach in comments
✅ THEN code

Spend 5 min thinking = Save 30 min debugging!
```

### Real Example:
```python
# ❌ WRONG: Jump to coding
def twoSum(nums, target):
    for i in range(len(nums)):  # Wait, how do I...
        # Gets stuck...

# ✅ RIGHT: Think first
def twoSum(nums, target):
    # Approach: Use hash map for O(1) lookup
    # For each num, check if (target - num) exists
    # Store num → index mapping

    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

---

## 🚫 Mistake #2: Not Reading Problem Carefully

### The Mistake:
```
Skim problem → Miss constraints → Wrong solution
```

### Common Missed Details:
- "Sorted array" → Should use Two Pointers or Binary Search!
- "In-place" → Can't use extra space!
- "Return indices" → Not values!
- "Distinct elements" → No duplicates!
- "At most K" → Not exactly K!

### The Fix:
```
✅ Read TWICE
✅ Underline key words
✅ Check constraints
✅ Verify examples
✅ Ask yourself: What's the catch?

Key words to watch:
- SORTED → Pattern hint!
- IN-PLACE → Space constraint!
- RETURN indices/values → What exactly?
- AT LEAST/AT MOST → Boundary!
```

### Real Example:
```
Problem: "Find two numbers in a SORTED array that sum to target"

❌ Wrong approach: Hash map (works but not optimal!)
✅ Right approach: Two Pointers (O(1) space, uses sorted property!)

The word "SORTED" is a huge hint!
```

---

## 🚫 Mistake #3: Ignoring Edge Cases

### The Mistake:
```
Solution works for main example → Submit → Fails on edge cases
```

### Common Edge Cases Missed:
```
Arrays:
- Empty array []
- Single element [1]
- Two elements [1, 2]
- All same [5, 5, 5, 5]
- Negative numbers [-1, -5, -10]

Strings:
- Empty string ""
- Single character "a"
- All spaces "   "
- Special characters "!@#"

Numbers:
- Zero
- Negative
- Max int (overflow!)
- Min int

Trees:
- None/null
- Single node
- All left/all right
- Unbalanced

Graphs:
- Disconnected
- Self-loop
- No edges
```

### The Fix:
```
✅ Always test:
   - Empty input
   - Single element
   - Two elements
   - Duplicates
   - Negatives/Zero
   - Max/Min values

✅ Before submitting, ask:
   "What could break this?"
```

### Testing Checklist:
```
For each solution:
□ Empty input
□ Single element
□ Normal case
□ Duplicates
□ Extreme values
□ Opposite signs
```

---

## 🚫 Mistake #4: Not Understanding Time Complexity

### The Mistake:
```
"My code works!" → Timeout on large inputs → Confused
```

### Common Complexity Errors:
```
❌ O(n²) when O(n) is needed
   - Nested loops for pair finding
   - Fix: Use hash map!

❌ O(n) when O(log n) is needed
   - Linear search in sorted array
   - Fix: Use binary search!

❌ O(2^n) without memoization
   - Naive recursion (Fibonacci)
   - Fix: Use DP!
```

### The Fix:
```
✅ Always calculate complexity BEFORE coding
✅ Check constraints:
   - n ≤ 100 → O(n²) OK
   - n ≤ 10,000 → O(n log n) needed
   - n ≤ 1,000,000 → O(n) or O(log n) needed

✅ If timeout:
   - Nested loops? → Use hash map
   - Searching unsorted? → Sort first or hash map
   - Repeated work? → Use DP
```

### Quick Reference:
```
Input Size    Max Complexity
n ≤ 10        O(n!)
n ≤ 20        O(2^n)
n ≤ 500       O(n³)
n ≤ 5,000     O(n²)
n ≤ 100,000   O(n log n)
n ≤ 1,000,000 O(n)
n > 1,000,000 O(log n) or O(1)
```

---

## 🚫 Mistake #5: Memorizing Code Instead of Patterns

### The Mistake:
```
Memorize Two Sum code → See 3Sum → Stuck!
```

### Why It Fails:
- Code is specific, patterns are general
- Can't apply to variations
- Forget code quickly

### The Fix:
```
❌ Don't memorize: "Two Sum uses this code..."
✅ Do understand: "Two Sum uses complement search pattern"

Pattern understanding:
1. WHAT: Find pairs that sum to X
2. WHY: Hash map gives O(1) lookup
3. WHEN: Unsorted array, need pairs
4. HOW: Store (target - num), check if exists

Now you can apply to:
- Two Sum II (sorted → use two pointers!)
- 3Sum (sort + two pointers)
- 4Sum (similar extension)
```

### Study Method:
```
For each problem:
□ What pattern is this?
□ Why does this pattern work?
□ When would I use this pattern again?
□ How can this pattern vary?

NOT just "What's the code?"
```

---

## 🚫 Mistake #6: Skipping Reviews (No Spaced Repetition)

### The Mistake:
```
Solve problem → Feel good → Never review → Forget everything
```

### What Happens:
```
Day 1: Solve Two Sum → "I got this!"
Day 30: See Two Sum again → "Wait, how did I...?"

Without reviews, you forget 90% in 30 days!
```

### The Fix:
```
✅ Use spaced repetition system (See REVISION_SYSTEM.md)
✅ Review at: 2-3 days, 7 days, 14 days, 30 days
✅ Mark every problem for review
✅ Don't skip reviews!

Review schedule:
Day 1: Solve problem
Day 3: Review (10 min)
Day 8: Review (8 min)
Day 15: Review (6 min)
Day 30: Review (5 min) → Long-term memory! ✅
```

---

## 🚫 Mistake #7: Giving Up Too Easily

### The Mistake:
```
Try for 10 minutes → Get stuck → Look at solution immediately
```

### Why It's Bad:
- No struggle = No learning
- Brain doesn't form strong connections
- Pattern recognition doesn't develop

### The Fix:
```
✅ Struggle time targets:
   - Easy: 15-20 min before hints
   - Medium: 25-30 min before hints
   - Hard: 35-40 min before hints

✅ When stuck:
   1. Re-read problem
   2. Draw more examples
   3. Check DECISION_TREE.md
   4. Review pattern guide
   5. Look at similar problem
   6. THEN check hints (not full solution)

✅ Partial hints progression:
   - "What pattern is this?" (not "How to solve")
   - "What data structure?" (not the code)
   - "How to optimize?" (not the answer)
```

### The Struggle is Learning:
```
Easy solve = Weak memory
Hard solve = Strong memory

Struggling for 20 min then solving >
Looking at solution immediately
```

---

## 🚫 Mistake #8: Not Drawing/Visualizing

### The Mistake:
```
Try to hold everything in head → Get confused → Make errors
```

### The Fix:
```
✅ ALWAYS draw:

Arrays:
[1, 2, 3, 4, 5]
 ↑     ↑     ↑
 i     j     k

Trees:
    1
   / \
  2   3
 / \
4   5

Graphs:
1 -- 2
|    |
3 -- 4

Hash Maps:
key → value
2 → 0
7 → 1

Windows:
[a, b, c, d, e]
 ↑     ↑
left  right
```

### Before Any Coding:
```
□ Draw the data structure
□ Show with 3-4 elements
□ Trace through step by step
□ Mark what changes
□ Only then code!
```

---

## 🚫 Mistake #9: Poor Variable Names

### The Mistake:
```python
# ❌ Bad naming
def f(a, t):
    x = {}
    for i, n in enumerate(a):
        y = t - n
        if y in x:
            return [x[y], i]
        x[n] = i
```

### The Fix:
```python
# ✅ Clear naming
def twoSum(nums, target):
    seen = {}  # value → index mapping

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
```

### Naming Guidelines:
```
✅ Use descriptive names:
   - seen, visited, memo (for hash maps)
   - left, right (for pointers)
   - slow, fast (for linked list)
   - count, freq (for frequency)

❌ Avoid:
   - Single letters (except i, j for loops)
   - Abbreviations (maxCnt → max_count)
   - Generic names (temp, data, val)
```

---

## 🚫 Mistake #10: Not Testing Your Code

### The Mistake:
```
Write code → Looks good → Submit → Fails
```

### The Fix:
```
✅ ALWAYS test before submitting:

1. Test with given examples
2. Test edge cases
3. Test with your own examples
4. Trace through step-by-step

Testing checklist:
□ Example 1 from problem
□ Example 2 from problem
□ Empty input
□ Single element
□ Two elements
□ Large input (mentally)
□ Negative numbers
□ Duplicates
```

### Manual Trace:
```
Code: Two Sum with [2, 7, 11, 15], target = 9

Step 1: i=0, num=2
  complement = 9-2 = 7
  7 in seen? No
  seen = {2: 0}

Step 2: i=1, num=7
  complement = 9-7 = 2
  2 in seen? YES! ✓
  return [0, 1]

Works! ✅
```

---

## 🚫 Mistake #11: Ignoring Space Complexity

### The Mistake:
```
"My solution is O(n) time! Done!"
*Uses O(n²) space* → Memory Limit Exceeded
```

### Common Issues:
```
❌ Creating unnecessary arrays
❌ Deep copying when shallow copy works
❌ Not reusing data structures
❌ Recursion too deep (stack overflow)
```

### The Fix:
```
✅ Always mention BOTH complexities:
   "Time: O(n), Space: O(n)"

✅ Check if in-place possible:
   Can I reuse the input array?
   Can I use pointers instead of new array?

✅ Optimize space:
   - Rolling variables instead of arrays
   - Iterative instead of recursive
   - One pass instead of multiple passes
```

### Example:
```python
# ❌ O(n) space
def reversedArray(arr):
    result = []
    for i in range(len(arr)-1, -1, -1):
        result.append(arr[i])
    return result

# ✅ O(1) space
def reverseInPlace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
```

---

## 🚫 Mistake #12: Not Using Available Templates

### The Mistake:
```
Start from scratch every time → Waste time → Make errors
```

### The Fix:
```
✅ Use template.py files in each topic!
✅ Keep CHEAT_SHEET.md open
✅ Reference similar solved problems

Templates available:
- Hash Map pattern
- Two Pointers pattern
- Sliding Window pattern
- Binary Search pattern
- DFS/BFS patterns
- DP patterns
- Backtracking pattern
```

### How to Use Templates:
```
1. Identify pattern
2. Open topic's template.py
3. Find relevant template
4. Understand the template
5. Adapt to your problem
6. Code confidently!
```

---

## 🚫 Mistake #13: Comparing to Others

### The Mistake:
```
"Person X solved 50 problems in 2 weeks, I'm only at 15..."
→ Feel bad → Lose motivation
```

### The Truth:
- Everyone learns at different pace
- Quality > Quantity
- Person X might have prior experience
- Your progress is YOUR progress

### The Fix:
```
✅ Compare to YESTERDAY's you:
   - Did I understand this better than yesterday?
   - Can I solve this faster than last week?
   - Do I recognize patterns quicker?

✅ Focus on:
   - YOUR milestones
   - YOUR improvements
   - YOUR goals

✅ Remember:
   - Slow and steady wins
   - Understanding > Speed
   - Consistency > Bursts
```

---

## 🚫 Mistake #14: Studying When Tired

### The Mistake:
```
Force study at 11 PM after long day → Frustration → Poor retention
```

### The Fix:
```
✅ Study when fresh:
   - Morning is best for most people
   - Find YOUR peak time
   - 2 hours focused > 4 hours tired

✅ If tired:
   - Do reviews (easier than new problems)
   - Watch visualizations
   - Read guides
   - Update trackers
   - Or just rest!

✅ Quality over quantity:
   - 1.5 hours focused > 3 hours distracted
   - Better to skip a day than burn out
```

### Energy Management:
```
High Energy → New Medium/Hard problems
Medium Energy → New Easy problems + Reviews
Low Energy → Only reviews or rest

Listen to your body!
```

---

## 🚫 Mistake #15: Not Taking Breaks

### The Mistake:
```
Study 4 hours straight → Brain fog → Diminishing returns
```

### The Fix:
```
✅ Use Pomodoro technique:
   - 45 min focus
   - 10 min break
   - Repeat

✅ Take real breaks:
   - Walk around
   - Stretch
   - Hydrate
   - Look away from screen

✅ Weekly rest:
   - Day 7 each week: lighter study
   - Day 21: Full day off!

✅ Signs you need a break:
   - Can't focus
   - Making silly errors
   - Feeling frustrated
   - Headache
```

---

## 💡 Top 10 Success Habits

```
1. ✅ Think before coding (5 min planning saves 30 min debugging)
2. ✅ Draw every problem (visualize!)
3. ✅ Read problem twice (catch all details)
4. ✅ Use templates (don't reinvent wheel)
5. ✅ Test edge cases (always!)
6. ✅ Do spaced reviews (don't forget!)
7. ✅ Struggle before hints (builds strength)
8. ✅ Track progress (stay motivated)
9. ✅ Study when fresh (quality over quantity)
10. ✅ Rest regularly (prevent burnout)
```

---

## 🎯 Quick Mistake Checklist

**Before submitting any solution:**

```
□ Did I read the problem carefully?
□ Did I check constraints?
□ Did I draw/visualize the solution?
□ Did I identify the pattern?
□ Did I calculate time complexity?
□ Did I calculate space complexity?
□ Did I test with given examples?
□ Did I test edge cases?
□ Did I use clear variable names?
□ Did I add comments explaining approach?
□ Can I explain this to someone?
```

If all ✅, submit with confidence! 🚀

---

**Remember: Mistakes are how we learn!**

Everyone makes these mistakes. The key is learning from them and not repeating them. 💪
