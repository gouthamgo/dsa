# Stack - Complete Guide

## 🎯 What is a Stack?

A **LIFO** (Last In, First Out) data structure. Think of a stack of plates - you add and remove from the top only!

**Visual:**
```
    Push(3)     Pop()
    ↓           ↓
   [3]         [ ]
   [2]         [2]
   [1]         [1]
   ---         ---
```

## 🧠 Core Operations

- **Push**: Add to top - O(1)
- **Pop**: Remove from top - O(1)
- **Peek/Top**: View top without removing - O(1)
- **IsEmpty**: Check if empty - O(1)

## 🎨 When to Use Stack

Use stack when you need to:
- ✅ Match pairs (parentheses, brackets)
- ✅ Reverse something
- ✅ Track history (undo/redo)
- ✅ Process nested structures
- ✅ Evaluate expressions
- ✅ DFS traversal

## 💡 Common Patterns

### Pattern 1: Matching Pairs
```python
Valid Parentheses: "({[]})" → Valid
Use stack to match opening/closing
```

### Pattern 2: Monotonic Stack
```python
Keep stack in increasing/decreasing order
Useful for: Next greater element, daily temperatures
```

### Pattern 3: Expression Evaluation
```python
Evaluate: "2 + 3 * 4"
Use stack for operators and operands
```

## 🔑 Key Problems

**Easy:**
- Valid Parentheses ⭐
- Min Stack
- Baseball Game

**Medium:**
- Daily Temperatures
- Evaluate Reverse Polish Notation
- Decode String

**Hard:**
- Largest Rectangle in Histogram
- Maximal Rectangle

## ⚡ Implementation

Python list works as stack:
```python
stack = []
stack.append(x)  # push
stack.pop()      # pop
stack[-1]        # peek
```

---
**Stacks are simple but powerful! Master the patterns.** 📚
