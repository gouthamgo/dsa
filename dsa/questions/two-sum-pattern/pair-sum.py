'''
--> array of integers --> sorted in asending order  --> and we are given a target --> return the indexes of any pair of numbers in array that sum to the target 
--> no pair --> return empty 

Input :nums = [-5,-2,3,4,6] and target is 7 

'''



def pair_sum_sorted(nums,target):
    left = 0
    right = len(nums)-1

    while left < right:
        sum = nums[left] + nums[right]
        if sum < target : 
            left +=1
        elif sum > target:
            right -=1
        else:
            return [left,right]
    return []


nums = [-5,-2,3,4,6]
target = 7 

print(pair_sum_sorted(nums,target))

'''
Here we do inward traversal here 

--> main is since its a sorted array 
--> we start from left and right 
--> left side and right side sum < target --> we  move towards right 
--> if sum > target --> ew move towards left 



'''