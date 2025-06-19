'''
Remove Duplicates

Given a sorted list of numbers, remove duplicates and return the new length. You must do this in-place and without using extra memory.

Input: [0, 0, 1, 1, 1, 2, 2].

Output: 3.

Your function should modify the list in place so that the first three elements become 0, 1, 2. Return 3 because the new length is 3.
'''


# arr =[0, 0, 1, 1, 1, 2, 2]
# print(arr[2])


def remove_duplicates(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1,len(nums)):
        if nums[j] != nums[i]:
            print('value of i and j' , nums[i] , nums[j])
            i+=1
            print(i)
            nums[i] = nums[j]
            print('last',nums[i],nums[j])
    return i+1
        

print(remove_duplicates([0, 0, 1, 1, 1, 2, 2]))



def check_freq(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

nums = [0, 0, 1, 1, 1, 2, 2]
freq_dict = check_freq(nums)

# Get unique elements
unique_elements = list(freq_dict.keys())
print(unique_elements) 

    
