# Contains Duplicate
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false




def contains_duplicate(nums):

    count = {}

    for num in nums:
        count[num] = count.get(num,0) + 1
    for num in count:
        if count[num]>1:
            return True
        
    return False




        
        

    




print(contains_duplicate([1,2,3,4]))


#  better way 


def contains_duplicates(nums):

    seen = set()


    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

print(contains_duplicates([1,2,3,3]))
        









