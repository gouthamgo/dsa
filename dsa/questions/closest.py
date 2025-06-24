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