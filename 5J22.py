'''
Group Anagrams
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
Example 2:

Input: strs = ["x"]

Output: [["x"]]
Example 3:

Input: strs = [""]

Output: [[""]]
Constraints:

1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.


'''



def groupA(arr):
    # empty dictionary 
    word_groups = {}

    # iterate through each word in input array 
    for word in arr:
        # create a unique signature by sorting out letters 
        sorted_signature = ''.join(sorted(word))


        # check if signature in dictionary or not 
        if sorted_signature not in word_groups:
            #  if not create a new empty list for this signature 
            word_groups[sorted_signature] = []

        # add orignal group to matching group 
        word_groups[sorted_signature].append(word)

        return list(word_groups.values())



