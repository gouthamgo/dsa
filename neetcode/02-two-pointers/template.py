"""
Two Pointers - Code Templates
=============================

Reusable templates for two pointer patterns.
"""

# ============================================================================
# TEMPLATE 1: Opposite Direction (Left & Right)
# ============================================================================

def two_pointers_opposite(arr):
    """
    Two pointers starting from opposite ends.

    Use for: Sorted arrays, palindromes, two sum

    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(arr) - 1

    while left < right:
        # Process current pair
        # Example: check sum, compare values, etc.

        # Move pointers based on condition
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        else:
            return [left, right]  # Found

    return []


# ============================================================================
# TEMPLATE 2: Same Direction (Slow & Fast)
# ============================================================================

def two_pointers_same_direction(arr):
    """
    Both pointers move in same direction, different speeds.

    Use for: Remove duplicates, in-place modification

    Time: O(n)
    Space: O(1)
    """
    slow = 0  # Builds result

    for fast in range(len(arr)):  # Explores
        # If element meets condition
        if arr[fast] != some_value:
            arr[slow] = arr[fast]
            slow += 1

    return slow  # New length


# ============================================================================
# TEMPLATE 3: Sliding Window
# ============================================================================

def sliding_window(s):
    """
    Window defined by two pointers that slides/expands/shrinks.

    Use for: Substrings, subarrays with conditions

    Time: O(n)
    Space: O(1) or O(k) for char set
    """
    left = 0
    max_length = 0
    char_set = set()

    for right in range(len(s)):
        # Expand window
        while s[right] in char_set:
            # Shrink from left
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# ============================================================================
# TEMPLATE 4: Valid Palindrome
# ============================================================================

def is_palindrome(s):
    """Check if string is palindrome"""
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# ============================================================================
# TEMPLATE 5: Three Pointers (3Sum pattern)
# ============================================================================

def three_sum(nums):
    """Find all triplets that sum to zero"""
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Two pointers for remaining
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


# ============================================================================
# TEMPLATE 6: Container With Most Water
# ============================================================================

def max_area(height):
    """Maximum water container"""
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        # Calculate area
        width = right - left
        current_height = min(height[left], height[right])
        area = width * current_height
        max_water = max(max_water, area)

        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


# Example usage
if __name__ == "__main__":
    # Palindrome check
    print(is_palindrome("racecar"))  # True
    print(is_palindrome("hello"))     # False

    # Max area
    print(max_area([1,8,6,2,5,4,8,3,7]))  # 49
