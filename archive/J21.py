'''
ou are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        


def isValid(s):
    # logic here 

        stack = []
        validPairs = {'()', '{}', '[]'} 

        for char in s:
                if char in '({[':
                        stack.append(char)
                elif not stack or stack.pop() + char not in validPairs:
                        return False

        return not stack

print(isValid("[{}]"))               
print(isValid('[[}]'))






'''


def isValid(s):

    stack = []
    
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != bracket_pairs[char]:
                return False
        stack.pop()

    return len(stack) == 0





