'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.

'''

def check_plan(s):
    # Convert to lowercase and remove non-alphanumeric characters
    s = ''.join(char.lower() for char in s if char.isalnum())
    
    stack = []

    # Push all characters onto the stack
    for char in s:
        stack.append(char)
    
    # Compare original string with characters popped from stack
    for char in s:
        if char != stack.pop():
            return False
    
    return True

print(check_plan("Was it a car or a cat I saw"))









        




        
    



