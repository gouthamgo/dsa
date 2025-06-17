# Valid Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
# Constraints:

# s and t consist of lowercase English letters.

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    # Count characters in s
    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    # Count characters in t
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    # Compare counts
    return count_s == count_t


print(is_anagram('racecar', 'carrace'))



#  with array counting 

def is_anagram1(s,t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for char in s:
        count[ord(char) - ord('a')] += 1
    for chat in t:
        count[ord(char) - ord('a')] -= 1
    return all(c ==0 for c in count)





