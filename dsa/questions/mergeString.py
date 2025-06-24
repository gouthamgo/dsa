'''

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

#   got 2 string , merge by adding alternate order , if string is longer append extra at the end 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

 

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters


'''
#   got 2 string , merge by adding alternate order , if string is longer append extra at the end 



def merger(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    s = ''

    if l1 == l2: 
        for i in range(0,l1):
           s += str1[i] + str2[i]
        return s
    else:
        difference = abs(l1-l2)
        print(difference)

        if l1> l2:
            g = l1 - difference
            print(g)
            for i in range(0,g):
                s +=  str1[i] + str2[i] 
            return s
        else:
            d = l2 - difference
            print(d)
            for i in range(0,d):
                s +=  str1[i] + str2[i]
            return s
        


print(merger('abc','pqr'))
print(merger('abc','pqrss'))

print(merger('abcsder','pqrss'))