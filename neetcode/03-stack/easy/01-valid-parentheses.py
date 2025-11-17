"""
Problem: Valid Parentheses
Difficulty: Easy
Topics: Stack, String

Problem Statement:
-----------------
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
---------
Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s = "(]"
    Output: false

LEARNING NOTES:
--------------
THE classic stack problem!

Key Insight: Stack is perfect for matching pairs!
- Push opening brackets
- Pop and match closing brackets
"""


def isValid(s):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in matching:  # Opening
            stack.append(char)
        else:  # Closing
            if not stack or matching[stack.pop()] != char:
                return False

    return len(stack) == 0


# Tests
test_cases = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
]

for s, expected in test_cases:
    result = isValid(s)
    status = "✅" if result == expected else "❌"
    print(f"{status} '{s}' → {result}")
