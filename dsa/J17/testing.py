# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.



def get_Numbers(nums,target):
    for i in range(len(nums)):
        current_sum = nums[i] + nums[len(nums) - 1]
        if current_sum == target:
            return (nums[i], nums[len(nums-1)])
        
    
print(get_Numbers([1,2,3,4], 7))
def find_two_sum(numbers, target):
    """
    Given a 1-indexed array of integers `numbers` that is already sorted in
    non-decreasing order, find two numbers such that they add up to a specific `target`.

    Args:
        numbers: A list of integers sorted in non-decreasing order.
        target: The target sum.

    Returns:
        A list containing the 1-indexed indices of the two numbers.
    """
    # Initialize two pointers, one at the beginning and one at the end.
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # Found the pair. Return their 1-indexed positions.
            return [left + 1, right + 1]
        elif current_sum < target:
            # The sum is too small, so we need a larger number.
            # Move the left pointer to the right.
            left += 1
        else:  # current_sum > target
            # The sum is too large, so we need a smaller number.
            # Move the right pointer to the left.
            right -= 1