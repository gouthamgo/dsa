"""
Tries (Prefix Trees) - Code Templates
=====================================

Reusable templates for prefix-tree problems. Every trie is just a dict of
dicts: each node owns a `children` map and a flag saying "a word ends here".
"""

# ============================================================================
# TEMPLATE 1: TrieNode + Trie (insert / search / startsWith)
# ============================================================================

class TrieNode:
    """A single node: a map of char -> child, plus an end-of-word flag."""

    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_end = False     # True if a word terminates at this node


class Trie:
    """
    Standard prefix tree.

    Time:  insert/search/startsWith all O(m), m = length of the word
    Space: O(total characters inserted)
    """

    def __init__(self):
        # The root holds no character - it is just the empty prefix "".
        self.root = TrieNode()

    def insert(self, word):
        """Walk down the tree, creating nodes for characters that are missing."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]      # descend into the child
        node.is_end = True                  # mark the LAST node as a word end

    def search(self, word):
        """True only if the exact word was inserted (not just a prefix)."""
        node = self._walk(word)
        # Falling off the tree -> None. Landing on a node that is only an
        # internal prefix (is_end False) -> the word itself was never inserted.
        return node is not None and node.is_end

    def startsWith(self, prefix):
        """True if any inserted word begins with `prefix`."""
        # Same walk as search, but we don't care about the is_end flag.
        return self._walk(prefix) is not None

    def _walk(self, chars):
        """Follow `chars` from the root; return the final node or None."""
        node = self.root
        for char in chars:
            if char not in node.children:
                return None                 # dead end - prefix not present
            node = node.children[char]
        return node


# ============================================================================
# TEMPLATE 2: Trie with Wildcard '.' Matching (DFS)
# ============================================================================

class WordDictionary:
    """
    Trie where search supports '.' as "any single character".

    Time:  insert O(m); search O(m) with no dots, O(26^d * m) worst case
           where d = number of dots (every dot forks into all children)
    Space: O(total characters inserted)
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Kick off a DFS from the root at character index 0."""
        return self._dfs(word, 0, self.root)

    def _dfs(self, word, i, node):
        # Consumed the whole pattern: this is a match only if a word ends here.
        if i == len(word):
            return node.is_end

        char = word[i]

        if char == '.':
            # Wildcard: try EVERY child; any one succeeding is enough.
            for child in node.children.values():
                if self._dfs(word, i + 1, child):
                    return True
            return False

        # Concrete character: only one possible path forward.
        if char not in node.children:
            return False
        return self._dfs(word, i + 1, node.children[char])


# ============================================================================
# TEMPLATE 3: Trie + DFS Grid Word Search (Word Search II)
# ============================================================================

def find_words_in_grid(board, words):
    """
    Find every word from `words` that can be spelled on the board.

    The trie lets one grid DFS hunt for ALL words at once: at each cell we
    check whether the current character keeps us inside the trie, and prune
    immediately if it does not.

    Time:  O(rows * cols * 4^L), L = longest word (trie prunes most branches)
    Space: O(total characters in words)
    """
    # --- Build a trie of all target words, stashing the word at its end node.
    root = TrieNode()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word            # store the whole word for easy collection

    rows, cols = len(board), len(board[0])
    found = []

    def dfs(r, c, node):
        # Off the board -> stop.
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return

        char = board[r][c]
        # '#' marks a cell already used on the current path.
        if char == '#' or char not in node.children:
            return                  # PRUNE: no word continues this way

        node = node.children[char]

        # getattr because internal nodes never got a .word attribute set.
        word = getattr(node, 'word', None)
        if word is not None:
            found.append(word)
            node.word = None        # de-duplicate: don't report it twice

        board[r][c] = '#'           # mark visited (choose)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            dfs(r + dr, c + dc, node)
        board[r][c] = char          # restore (un-choose / backtrack)

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)         # every cell is a possible word start

    return found


# ============================================================================
# TEMPLATE 4: Delete a Word from a Trie
# ============================================================================

def delete_word(root, word):
    """
    Remove `word` from the trie, pruning nodes that become useless.

    A node may be deleted only if it (a) ends no other word and (b) has no
    remaining children. The recursion returns True when the CHILD it just
    handled should be unlinked from its parent.

    Time:  O(m)   Space: O(m) recursion stack
    """

    def helper(node, i):
        if i == len(word):
            if not node.is_end:
                return False        # word was never in the trie - change nothing
            node.is_end = False     # un-mark it
            # Safe to delete this node only if it is now a childless leaf.
            return len(node.children) == 0

        char = word[i]
        if char not in node.children:
            return False            # word not present - nothing to unlink

        child = node.children[char]
        should_prune = helper(child, i + 1)

        if should_prune:
            del node.children[char]
            # This node in turn becomes deletable if it is now a childless
            # non-terminal node.
            return not node.is_end and len(node.children) == 0

        return False

    helper(root, 0)


# ============================================================================
# TEMPLATE 5: Collect All Words with a Given Prefix (Autocomplete)
# ============================================================================

def words_with_prefix(root, prefix):
    """
    Return every inserted word starting with `prefix`.

    Two phases: walk down to the prefix node, then DFS everything beneath it.

    Time:  O(len(prefix) + total characters in the subtree)
    Space: O(depth) recursion + O(k) output
    """
    node = root
    for char in prefix:
        if char not in node.children:
            return []               # no word has this prefix
        node = node.children[char]

    results = []

    def collect(node, path):
        if node.is_end:
            results.append(prefix + ''.join(path))

        for char, child in node.children.items():
            path.append(char)       # choose
            collect(child, path)
            path.pop()              # un-choose

    collect(node, [])
    return results


# ============================================================================
# TEMPLATE 6: Array-Backed Trie (26 lowercase letters)
# ============================================================================

class ArrayTrieNode:
    """
    Fixed-size children array instead of a dict.

    Slightly faster and avoids hashing, at the cost of 26 slots per node
    even when only one is used. Handy when the alphabet is known and small.
    """

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


def array_trie_insert(root, word):
    """Index children by ord(char) - ord('a')."""
    node = root
    for char in word:
        idx = ord(char) - ord('a')
        if node.children[idx] is None:
            node.children[idx] = ArrayTrieNode()
        node = node.children[idx]
    node.is_end = True


def array_trie_search(root, word):
    """Mirror of insert, but bail out on a missing slot."""
    node = root
    for char in word:
        idx = ord(char) - ord('a')
        if node.children[idx] is None:
            return False
        node = node.children[idx]
    return node.is_end
