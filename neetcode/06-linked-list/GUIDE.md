# Linked List - Complete Guide

## 🎯 What is a Linked List?

A data structure where elements (nodes) are connected via pointers/references.

**Visual:**
```
Singly Linked List:
[1] → [2] → [3] → [4] → None

Each node: [data | next]
```

## 🧠 Types

### Singly Linked List
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Doubly Linked List
```python
class DNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
```

## 🔑 Common Patterns

### 1. Two Pointers (Slow & Fast)
```python
slow = fast = head
while fast and fast.next:
    slow = slow.next        # Move 1 step
    fast = fast.next.next   # Move 2 steps
```
**Use for:** Cycle detection, find middle, nth from end

### 2. Dummy Head
```python
dummy = ListNode(0)
dummy.next = head
# Simplifies edge cases!
```

### 3. Reverse
```python
prev = None
curr = head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev
```

## ⚡ Key Problems

**Easy:**
- Reverse Linked List ⭐
- Merge Two Sorted Lists
- Linked List Cycle

**Medium:**
- Remove Nth Node From End
- Reorder List
- Add Two Numbers

**Hard:**
- Merge K Sorted Lists
- Reverse Nodes in K-Group

## 💡 Pro Tips

1. **Draw it!** Linked lists are visual
2. **Use dummy head** for cleaner code
3. **Watch pointers** - easy to lose references
4. **Two pointer** technique is key

Time: Operations vary
Space: O(1) for in-place modifications

---
**Master pointer manipulation - it's all about the arrows!** ➡️
