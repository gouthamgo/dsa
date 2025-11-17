'''
Largest Container 

--> given an array of numbers --> each represting the height of a vertical line on a graph 
--> a container can be formed with any pair of these lines , along with the x-axis on the graph 
--> return the amount of water which the largest container can hold 


Input heights --> [2,7,8,3,7,6]
output - 24 


'''


def largest_container(heights):
    max_water = 0
    left = 0 
    right = len(heights)-1

    while(left < right):
        # ikkada asulu water antha undi anni calculate cheyi firs t
        water = min(heights[left],heights[right]) * (right - left )
        max_water = max(max_water,water)

        if(heights[left] < heights[right]):
            left +=1
        elif (heights[left] > heights[right]):
            right -=1
        else:
            left +=1
            right -=1
    return max_water

heights = [2,7,8,3,7,6]
print(largest_container(heights))
