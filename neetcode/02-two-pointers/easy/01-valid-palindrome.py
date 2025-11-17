"""
Problem: Valid Palindrome
Difficulty: Easy
Topics: Two Pointers, String

Problem Statement:
-----------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward
and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:
---------
Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.

LEARNING NOTES:
--------------
Perfect introduction to TWO POINTERS pattern!

Key Insight: Compare characters from both ends moving inward.

Visualization:
    "racecar"
     ↑     ↑
     L     R    r==r ✓ Move both inward
      ↑   ↑
      L   R     a==a ✓ Move both inward
       ↑ ↑
       L R      c==c ✓ Move both inward
        ↑
      L=R       Done! Is palindrome ✓
"""


def isPalindrome(s):
    """
    Approach: Two pointers from opposite ends

    Time: O(n)
    Space: O(1)
    """
    # Clean string: lowercase + alphanumeric only
    cleaned = ''.join(c.lower() for c in s if c.isalnum())

    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def isPalindrome_v2(s):
    """
    Optimized: No extra space for cleaned string
    Skip non-alphanumeric on the fly

    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


# Tests
def test():
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("racecar", True),
    ]

    for s, expected in test_cases:
        result = isPalindrome_v2(s)
        status = "✅" if result == expected else "❌"
        print(f"{status} '{s}' → {result}")


if __name__ == "__main__":
    test()
