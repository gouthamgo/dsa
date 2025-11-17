"""
Sliding Window - Code Templates
===============================
"""

# ============================================================================
# TEMPLATE 1: Variable Size Window
# ============================================================================

def longest_substring_without_repeating(s):
    """Find longest substring without repeating characters"""
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Expand window
        while s[right] in char_set:
            # Shrink window
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# TEMPLATE 2: Fixed Size Window
# ============================================================================

def max_sum_subarray(arr, k):
    """Maximum sum of subarray of size k"""
    if len(arr) < k:
        return 0

    # First window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


# ============================================================================
# TEMPLATE 3: Window with Character Frequency
# ============================================================================

def min_window_substring(s, t):
    """Minimum window containing all characters of t"""
    from collections import Counter

    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    formed = 0
    window_counts = {}

    left = 0
    min_len = float('inf')
    min_left = 0

    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in dict_t and window_counts[char] == dict_t[char]:
            formed += 1

        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_left = left

            char = s[left]
            window_counts[char] -= 1
            if char in dict_t and window_counts[char] < dict_t[char]:
                formed -= 1

            left += 1

    return "" if min_len == float('inf') else s[min_left:min_left + min_len]


# Example usage
if __name__ == "__main__":
    print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
    print(max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))  # 39
