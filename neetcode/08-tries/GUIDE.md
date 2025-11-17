# Tries (Prefix Trees) - Complete Guide

## 🎯 What is a Trie?

A tree data structure for storing strings efficiently. Each path from root to leaf represents a word.

**Visual:**
```
Words: ["cat", "car", "dog"]

      root
     /    \
    c      d
    |      |
    a      o
   / \     |
  t   r    g
  *   *    *
  (* = end of word)
```

## 🧠 Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char → TrieNode
        self.is_end_of_word = False
```

## 🔑 Core Operations

### Insert
```python
def insert(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.is_end_of_word = True
```

### Search
```python
def search(self, word):
    node = self.root
    for char in word:
        if char not in node.children:
            return False
        node = node.children[char]
    return node.is_end_of_word
```

### Starts With (Prefix)
```python
def startsWith(self, prefix):
    node = self.root
    for char in prefix:
        if char not in node.children:
            return False
        node = node.children[char]
    return True
```

## 💡 When to Use Tries

- ✅ Autocomplete
- ✅ Spell checker
- ✅ IP routing
- ✅ Word search problems
- ✅ Prefix matching

## ⚡ Key Problems

**Medium:**
- Implement Trie ⭐
- Design Add and Search Words Data Structure
- Word Search II

**Hard:**
- Word Search II

## 💡 Complexity

- Insert: O(m) where m = word length
- Search: O(m)
- Space: O(ALPHABET_SIZE × N × M) worst case

---
**Tries excel at prefix operations!** 🌿
