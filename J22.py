'''
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    


         

'''


def hasDuplicate(arr):
    stack = []

    for num in arr:
        if num not in stack:
            stack.append(num)
    
    return len(stack) != len(arr)

nums = [1, 2, 3, 4]
print(hasDuplicate(nums))



