'''
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

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

def checkPalindrom(s):
    newString = s.replace(" ","").lower().replace("?","")
    print(newString)

    i = 0 
    j = len(newString)- 1
    print(i,j)

    if i<j:
        s[i] == s[j]
        return True
    else:
        return False








print(checkPalindrom('Was it a car or a cat I saw'))



#  a two pointer technique -- need to revisie 