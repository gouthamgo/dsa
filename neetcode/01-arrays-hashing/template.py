"""
Arrays & Hashing - Code Templates
==================================

This file contains reusable templates for common array and hashing patterns.
Study these templates and use them as starting points for solving problems.
"""

# ============================================================================
# TEMPLATE 1: Frequency Counting
# ============================================================================

def frequency_counter_template(items):
    """
    Count how many times each item appears.

    Time: O(n)
    Space: O(n)
    """
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1

    return freq


# Alternative using collections
from collections import Counter, defaultdict

def frequency_counter_v2(items):
    """Using Counter (built-in)"""
    return Counter(items)


def frequency_counter_v3(items):
    """Using defaultdict"""
    freq = defaultdict(int)
    for item in items:
        freq[item] += 1  # No need for .get()
    return freq


# ============================================================================
# TEMPLATE 2: Duplicate Detection
# ============================================================================

def has_duplicate(nums):
    """
    Check if array contains any duplicates.

    Time: O(n)
    Space: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# One-liner version
def has_duplicate_oneliner(nums):
    """Compare set size with array length"""
    return len(set(nums)) < len(nums)


# ============================================================================
# TEMPLATE 3: Complement Search (Two Sum Pattern)
# ============================================================================

def find_complement(nums, target):
    """
    Find two numbers that add up to target.

    Time: O(n)
    Space: O(n)
    """
    seen = {}  # value → index

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []


# ============================================================================
# TEMPLATE 4: Grouping/Categorizing
# ============================================================================

def group_by_property(items, key_func):
    """
    Group items based on a property/key function.

    Args:
        items: List of items to group
        key_func: Function that returns the grouping key

    Example:
        Group words by length:
        group_by_property(["cat", "dog", "bird"], len)
        → {3: ["cat", "dog"], 4: ["bird"]}

    Time: O(n * k) where k is cost of key_func
    Space: O(n)
    """
    groups = defaultdict(list)

    for item in items:
        key = key_func(item)
        groups[key].append(item)

    return dict(groups)


def group_anagrams_template(words):
    """
    Specific example: Group anagrams together.

    Anagrams have the same characters when sorted.
    "eat" → "aet", "tea" → "aet" (same!)
    """
    groups = defaultdict(list)

    for word in words:
        # Create key: sorted characters
        key = ''.join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


# ============================================================================
# TEMPLATE 5: Index Mapping
# ============================================================================

def create_index_map(nums):
    """
    Map each value to its index(es).

    Time: O(n)
    Space: O(n)
    """
    index_map = defaultdict(list)

    for i, num in enumerate(nums):
        index_map[num].append(i)

    return index_map


# ============================================================================
# TEMPLATE 6: Set Operations
# ============================================================================

def set_operations_template():
    """Common set operations for interviews"""

    # Union: elements in A or B
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union = set_a | set_b  # {1, 2, 3, 4, 5}

    # Intersection: elements in both A and B
    intersection = set_a & set_b  # {3}

    # Difference: elements in A but not in B
    difference = set_a - set_b  # {1, 2}

    # Symmetric Difference: elements in A or B but not both
    sym_diff = set_a ^ set_b  # {1, 2, 4, 5}

    return union, intersection, difference, sym_diff


# ============================================================================
# TEMPLATE 7: Running Product/Sum (Prefix/Suffix)
# ============================================================================

def prefix_sum(nums):
    """
    Compute prefix sums: prefix[i] = sum of nums[0:i+1]

    Example: [1,2,3,4] → [1,3,6,10]

    Time: O(n)
    Space: O(n)
    """
    prefix = [0] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] + nums[i]

    return prefix


def prefix_product(nums):
    """
    Compute prefix products.

    Example: [2,3,4] → [2,6,24]
    """
    prefix = [1] * len(nums)
    prefix[0] = nums[0]

    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i]

    return prefix


# ============================================================================
# TEMPLATE 8: Sliding Window with Hash Map
# ============================================================================

def sliding_window_hash_template(s):
    """
    Sliding window that tracks character frequencies.

    Useful for substring problems.

    Time: O(n)
    Space: O(k) where k is alphabet size
    """
    window = {}
    left = 0
    result = 0

    for right in range(len(s)):
        # Add right element to window
        char = s[right]
        window[char] = window.get(char, 0) + 1

        # Shrink window if needed
        while window[char] > 1:  # Example condition
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1

        # Update result
        result = max(result, right - left + 1)

    return result


# ============================================================================
# TEMPLATE 9: Two-Pass Solution
# ============================================================================

def two_pass_template(nums):
    """
    Pass 1: Collect information
    Pass 2: Use that information

    Time: O(n)
    Space: O(n)
    """
    # Pass 1: Gather data
    data = {}
    for num in nums:
        # Collect info
        data[num] = data.get(num, 0) + 1

    # Pass 2: Process using collected data
    result = []
    for num, count in data.items():
        if count > 1:  # Example condition
            result.append(num)

    return result


# ============================================================================
# TEMPLATE 10: In-Place Array Manipulation
# ============================================================================

def two_pointer_modify(nums):
    """
    Modify array in-place using two pointers.

    Common for: removing duplicates, moving zeros, etc.

    Time: O(n)
    Space: O(1)
    """
    left = 0  # Slow pointer

    for right in range(len(nums)):  # Fast pointer
        # If element meets condition
        if nums[right] != 0:  # Example: non-zero
            nums[left] = nums[right]
            left += 1

    return left  # New length


# ============================================================================
# EXAMPLES AND PRACTICE
# ============================================================================

def example_usage():
    """Examples of using the templates"""

    # Example 1: Count frequencies
    print("Frequency counting:")
    chars = ['a', 'b', 'a', 'c', 'b', 'a']
    print(f"Input: {chars}")
    print(f"Frequencies: {frequency_counter_template(chars)}")
    print()

    # Example 2: Detect duplicates
    print("Duplicate detection:")
    nums1 = [1, 2, 3, 4]
    nums2 = [1, 2, 3, 1]
    print(f"{nums1} has duplicate: {has_duplicate(nums1)}")
    print(f"{nums2} has duplicate: {has_duplicate(nums2)}")
    print()

    # Example 3: Two Sum
    print("Two Sum (complement search):")
    nums = [2, 7, 11, 15]
    target = 9
    print(f"Input: {nums}, target: {target}")
    print(f"Indices: {find_complement(nums, target)}")
    print()

    # Example 4: Group anagrams
    print("Group anagrams:")
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(f"Input: {words}")
    print(f"Grouped: {group_anagrams_template(words)}")
    print()


if __name__ == "__main__":
    example_usage()
