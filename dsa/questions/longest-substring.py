'''
Longest Substring Without Repeating Characters

Description: Given a string, find the length of the longest substring without repeating characters.

Example: Input: "abcabcbb" Output: 3 ("abc")
'''


def longest_substring(s:str):
    char_set = set()
    # i initialised an empty set 
    left = 0
    max_length = 0 
    #  initalisation on left side and to keep track of length found 

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])


        max_length = max(max_length,right-left +1)
    return max_length




