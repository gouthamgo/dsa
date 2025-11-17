'''
Two Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:

Input: nums = [4,5,6], target = 10

Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10

Output: [0,1]
Constraints:

2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
    

'''


def twoSum(nums, target):
    # Step 1: Create an empty hash map (dictionary)
    num_map = {}
    
    # Step 2: Iterate through the array
    for i, num in enumerate(nums):
        # Step 3: Calculate the complement
        complement = target - num
        
        # Step 4: Check if complement exists in hash map
        if complement in num_map:
            # Return indices if complement is found
            return [num_map[complement], i]
        
        # Step 5: Add current number and its index to hash map
        num_map[num] = i
    
    # Return empty list if no solution found
    return []



nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]





