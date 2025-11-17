# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

'''
we get bunch of strings in an array -- check the length 

# idea is comparing the counts of each string 
# another idea is loop through each string element and compare with counts of each other string elements (expensive)
'''



def group_anagrams(strs):
    if not strs:  # Handle empty array
        return []
    
    # Initialize hash map to group anagrams
    anagram_groups = {}
    
    # Iterate through each string
    for s in strs:
        # Create frequency array for 26 lowercase letters
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        # Convert frequency array to tuple (hashable key)
        key = tuple(freq)
      
        
        
        # Add string to corresponding anagram group
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(s)

        print(anagram_groups)
    
    # Return all groups as list of lists
    return list(anagram_groups.values())



strs = ["act","pots"]
print(group_anagrams(strs))




    


