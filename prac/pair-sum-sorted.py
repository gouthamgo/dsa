'''
Pair Sum - Sorted
difficulty -->Easy
Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in the array that sum to the target. The order of the indexes in the result doesn't matter. If no pair is found, return an empty array.

Example 1:
Input: nums = [-5, -2, 3, 4, 6], target = 7
Output: [2, 3]
Explanation: nums[2] + nums[3] = 3 + 4 = 7

Example 2:
Input: nums = [1, 1, 1], target = 2
Output: [0, 1]
Explanation: other valid outputs could be [1, 0], [0, 2], [2, 0], [1, 2] or [2, 1].


// we need to return the indexes from the array that equals target 
// no pair then return and empty array 
'''

def sorted_sum(nums,target):
    left = 0
    right = len(nums)-1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return[left,right]
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return []


# here sum < target --> move to left forward to increase the sum -- bcz of increasing order 
#  or else move to right to decrease the sum 


print(sorted_sum([-5, -2, 3, 4, 6],7))

        




