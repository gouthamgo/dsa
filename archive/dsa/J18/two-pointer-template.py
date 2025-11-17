# two pointer pattern template

def two_pointer_template(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        left_val = arr[left]
        right_val = arr[right]

        if some_condition:
            return True
        elif need_bigger_value:
            left +=1
        else:
            right -=1

    return False

