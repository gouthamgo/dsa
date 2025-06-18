def two_sum_sorted(nums, target):
    left = 0 
    right = len(nums)-1

    while left <right:
        current_sum = nums[left] +nums[right]

        if current_sum == target:
            return[left,right]
        elif current_sum < target:
            left+=1
        else:
            right -=1
    return []


print(two_sum_sorted([1,2,3,4,5],7))