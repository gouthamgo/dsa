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

The key insight: **"cat" and "car" share the prefix "ca", so they share nodes.**
A hash set of words stores "ca" twice; a trie stores it once. That shared
structure is what makes prefix questions cheap.

**Root holds no character.** It represents the empty prefix `""`. Every edge
is labelled with a character, and a *node* is really "the prefix formed by the
path that reached it".

## 🧠 Trie Node Structure

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char → TrieNode
        self.is_end_of_word = False
```

Two fields, and both matter:

- `children` — the outgoing edges. A dict keeps it flexible (any alphabet);
  a 26-slot list is faster when you know it's lowercase a–z.
- `is_end_of_word` — **without this flag a trie cannot tell a word from a
  prefix.** Insert "cat" and the node at "ca" exists, but no one ever typed
  "ca". The flag is the only thing separating `search` from `startsWith`.

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

Notice `search` and `startsWith` are **the same walk**. They differ only in
the last line: `search` demands the flag, `startsWith` is happy to have
arrived. Factor the walk into a helper and you write it once.

## 🔍 When to Reach for a Trie

The tell is almost always the word **prefix**, or a set of strings being
queried repeatedly. Concrete trigger phrases in a problem statement:

| You read this... | Think trie |
|---|---|
| "words that start with..." | prefix walk |
| "autocomplete" / "search suggestions" | prefix walk + DFS below it |
| "design a data structure that stores words" | it's a trie, guaranteed |
| "`.` matches any character" | trie + DFS branching on wildcards |
| "find **all** words in this grid" (plural!) | trie + grid DFS |
| "longest common prefix of these strings" | walk while exactly 1 child |
| "spell checker" / "dictionary of valid words" | trie membership |
| "IP routing" / "longest matching prefix" | bitwise trie |
| "count words with prefix X" | store a counter per node |

**The plural is the giveaway on Word Search II.** Word Search (singular,
topic 09) is plain backtracking. Word Search *II* asks for many words at
once — running the singular solution k times is O(k · rows · cols · 4^L)
and times out. The trie collapses those k searches into one traversal.

**Anti-signal:** if you only ever ask "is this exact string present?", a
`set` is simpler and faster. Tries earn their keep on *prefixes*.

## ⚡ Complexity Analysis

Let **m** = length of the word being operated on, **n** = number of words,
**A** = alphabet size (26 for lowercase).

| Operation | Time | Why |
|---|---|---|
| `insert(word)` | O(m) | one node hop per character |
| `search(word)` | O(m) | same walk, then check the flag |
| `startsWith(prefix)` | O(m) | same walk |
| `delete(word)` | O(m) | walk down, prune on the way back up |
| collect all words under a prefix | O(m + total chars in subtree) | walk, then DFS |
| Build from n words | O(n · m) | n independent inserts |
| Space | O(n · m) nodes worst case | shared prefixes reduce this a lot |

**The headline:** every operation is O(m) and **independent of n**. A trie
holding ten words and a trie holding ten million answer `startsWith("pre")`
in the same time. Compare with scanning a list of words: O(n · m).

**Space is the trade-off.** Each dict-based node carries hash-table overhead
(~100+ bytes in CPython) for maybe one child. A 26-slot array node wastes
25 pointers. Worst case with no shared prefixes, a trie is strictly bigger
than the list of strings it stores. You buy prefix speed with memory.

**Wildcard search is the exception to O(m).** Each `.` forks into every
child, so a pattern with *d* dots costs up to O(A^d · m). `"...."` on a
large dictionary really does explore a lot of the tree.

## 💡 When to Use Tries

- ✅ Autocomplete
- ✅ Spell checker
- ✅ IP routing
- ✅ Word search problems
- ✅ Prefix matching

## 🎨 Beyond the Basics

### Storing the word at its end node

For Word Search II, instead of a bare `is_end` flag, hang the whole word on
the terminal node. When the DFS lands there you can append it directly with
no path reconstruction:

```python
node.word = word          # instead of node.is_end = True
...
if node.word:
    found.append(node.word)
    node.word = None      # de-duplicate: never report it twice
```

That `node.word = None` line is doing double duty — it's also how you avoid
returning "oath" twice when the board can spell it two different ways.

### Counting instead of flagging

Swap the boolean for an integer and you can answer "how many stored words
start with this prefix?" in O(m):

```python
node.count += 1           # on every node along the insert path
```

### Pruning on delete

Deleting is the only operation with real subtlety: you must unlink nodes
that became useless, but only those. A node survives if it still ends
another word (`is_end`) **or** still has children. See TEMPLATE 4 in
`template.py` — the recursion returns "should my parent unlink me?" and
bubbles that decision upward.

## 🐛 Common Pitfalls

1. **Forgetting `is_end_of_word`.** Then `search("ca")` returns True after
   inserting only "cat". This is *the* classic trie bug.

2. **Returning `True` from `search` just because the walk survived.** The
   walk succeeding only proves a prefix exists. Check the flag.

3. **Reusing one `TrieNode()` for multiple children.** Writing
   `node.children[char] = shared_node` aliases subtrees and corrupts
   everything. Construct a fresh node per edge.

4. **Making `children` a class attribute:**
   ```python
   class TrieNode:
       children = {}          # ☠️ SHARED BY EVERY INSTANCE
   ```
   Every node now points at the same dict. Always initialise inside
   `__init__`.

5. **Forgetting to restore the board in grid DFS.** `board[r][c] = '#'`
   must be undone with `board[r][c] = char` after the recursion, or later
   starting cells search a corrupted grid.

6. **Not de-duplicating Word Search II results.** The same word reachable by
   two paths gets appended twice. Null out the stored word, or use a set.

7. **Building the trie inside the grid loop.** Build it once before scanning
   cells — rebuilding per cell throws away the entire point.

8. **Empty string handling.** `search("")` should return `root.is_end`
   (False unless you inserted `""`), and `startsWith("")` should be True.
   The loop-based implementations get this right for free; hand-rolled
   special cases often don't.

## 🔬 Worked Example: Trace an Insert and a Search

Insert `"cat"`, then `"car"`, into an empty trie.

**insert("cat")** — start at root, `node = root`:

```
char 'c': 'c' not in root.children     → create node C, descend
char 'a': 'a' not in C.children        → create node A, descend
char 't': 't' not in A.children        → create node T, descend
loop ends: T.is_end = True

  root
   |c
   C
   |a
   A
   |t
   T*
```

**insert("car")** — the shared prefix is reused, no new nodes for c/a:

```
char 'c': 'c' IS in root.children      → descend to existing C
char 'a': 'a' IS in C.children         → descend to existing A
char 'r': 'r' not in A.children        → create node R, descend
loop ends: R.is_end = True

  root
   |c
   C
   |a
   A
  t/ \r
  T*  R*
```

Two words, five nodes — not six, because "ca" is stored once.

**search("ca")** — walk succeeds, flag fails:

```
'c' → C,  'a' → A,  loop ends
return A.is_end  →  False    ✅ correct: "ca" was never inserted
```

**startsWith("ca")** — same walk, no flag check:

```
'c' → C,  'a' → A,  loop ends
return True                  ✅ correct: "cat" and "car" both start with it
```

**search("cab")** — falls off the tree:

```
'c' → C,  'a' → A
'b' not in A.children  →  return False immediately
```

Same two lines of code, three different questions answered correctly. That's
the whole data structure.

## 📝 Problems in This Category

### Medium
1. **Implement Trie (Prefix Tree)** ⭐ — the foundation. `insert`, `search`,
   `startsWith`. Do this one until it's muscle memory; everything else builds
   on it.
2. **Design Add and Search Words Data Structure** ⭐ — adds `.` wildcards.
   The moment search can branch, it stops being a loop and becomes a DFS.
3. **Word Search II** ⭐ — trie + grid backtracking. The hardest and most
   instructive of the three; genuinely Hard despite its listing.

### Related problems that secretly want a trie
- Longest Common Prefix — walk down while each node has exactly one child
  and isn't a word end.
- Replace Words — insert the dictionary roots, then for each word walk until
  you hit the first `is_end`.
- Maximum XOR of Two Numbers — a *bitwise* trie over 32-bit numbers; at each
  bit greedily take the opposite branch to maximise XOR.

**Suggested order:** Implement Trie → Add and Search Words → Word Search II.
Do not attempt Word Search II before the first two feel automatic — it
combines a trie, a grid DFS, and backtracking all at once.

## 🚀 Next Steps

1. Study the `template.py` file — all six patterns
2. Implement a trie from a blank file, no reference, until it's automatic
3. Solve **Implement Trie** first, then layer on wildcards
4. Come back to **Word Search II** after topic 09 (Backtracking)

---
**Tries excel at prefix operations!** 🌿
