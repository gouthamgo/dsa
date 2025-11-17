'''
Valid Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.



from collections import Counter

def isValid(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)


'''

def isValid(s, t):
    #  if lengths of strings are not the same 
    if  len(s) != len(t):
        return False
    
    char_count ={}
    
    # count chars in s
    for char in s:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char]=1

            # decerment the char count and remove if 0

    for char in t:
        if char not in char_count:
            return False
        char_count[char] -=1
        if char_count[char] == 0:
            del char_count[char]

    return len(char_count)  == 0
    

print(isValid("racecar", "carrace"))  # True
print(isValid("hello", "world"))  # False