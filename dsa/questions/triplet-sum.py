'''
-> Given an array of Integers 

--> return all triplets [a,,bc,] --> such that a+b+c = 0 

--> no duplicate triplets are allowed eg --> [1,2,3] and [2,3,1]

--> if none found --> return empty array 

-> each triplet can be arranged in any order and can be returned in any order 

considering [-1 2 -2 1 -1 2]
 
'''


def triplets_sum(nums):
    triplets = [] 
    # ikkada manam triplets array create chesam --> which is empty 
    nums.sort() 
    # ikkada ichina array ni sort chasamu 
    for i in range(len(nums)):
        # ippudu --> ichcina array lo anni postive numbers unte --> sum appudu 0 avvadu 
        if nums[i] > 0: 
            break
        if i> 0 and nums[i] == nums[i-1]:
            continue
        # ikkada --> index element 0 kanna akkuva ayithae , and a indexth number and danni mundu number same ayitae --> continue
        pairs = pair_sum_sorted(nums, i+1, -nums[i])
        # ippudu inko function ki pass chatunam - array , loop ayinapude index element perugutundi , taget to "-a"
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets



def pair_sum_sorted(nums,start, target):
    pairs = []
    left = start
    right = len(nums)-1

    while left < right: 
        sum = nums[left]  + nums[right]
        if sum == target:
            pairs.append([nums[left] , nums[right]])
            left +=1
            while left < right and nums[left] == nums[left -1]:
                left +=1
        elif sum <target:
            left +=1
        else:
            right -=1
    return pairs



nums = [-1, 2,-2, 1, -1, 2]
print(triplets_sum(nums))

