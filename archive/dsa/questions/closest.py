'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.

Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.

 

Constraints:

    1 <= n <= 1000
    -105 <= nums[i] <= 105


'''

#  nums  - sizze n , return number close to 0 , if we get 2 numbers , give the larger one 


def close(nums):
    # i need to calcuate the distance from 0 
    #  0 - 4 , how --> 4-0  and what about -4 to 0 , 0- (-4)
    s= []
    for num in nums: 
        if num > 0:
            s.append(num-0)
        else:
            s.append(0-(num))
    s.sort()
    return s[0]


    



print(close([-4,-2,1,4,8]))
print(close([2,-1,1]))



 # better appraoch 
#     here i am assuming first number is the closeset and compare to other numbers 


def close1(nums):
    closest = nums[0]
    for num in nums:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest

   
print(close1([-4,-2,1,4,8]))



'''
Approach and Thinking

    Initialization:
    Assume the first number is the closest. This is a common pattern when searching for an optimal value in a list.

    Iterative Comparison:
    For each number, check if it's closer to zero than the current best.

        Use abs() to measure distance from zero.

    Tie-breaker:
    If two numbers are equally close, pick the larger one.

        This is handled by the second part of the if condition.

    Single Pass:
    The loop goes through the list once, making the solution efficient (O(n) time, O(1) space).

Example Walkthrough

Let's walk through nums = [2, -1, 1]:
Iteration	num	closest	abs(num)	abs(closest)	Condition True?	New closest
Start		2				2
1	2	2	2	2	Yes	2
2	-1	2	1	2	Yes	-1
3	1	-1	1	1	Yes (tie, 1 > -1)	1


Initialize	Start with the first element
Loop through list	Compare each number to current best
Use absolute value	For "distance" from zero
Tie-breaker	Prefer the larger number
Return result	After checking all numbers

'''