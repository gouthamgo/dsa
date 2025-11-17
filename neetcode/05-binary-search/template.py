"""
Binary Search - Code Templates
==============================
"""

# ============================================================================
# TEMPLATE 1: Classic Binary Search
# ============================================================================

def binary_search(arr, target):
    """Find target in sorted array"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# ============================================================================
# TEMPLATE 2: Find First Occurrence
# ============================================================================

def find_first(arr, target):
    """Find first occurrence of target"""
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


# ============================================================================
# TEMPLATE 3: Search Insert Position
# ============================================================================

def search_insert(arr, target):
    """Find index where target should be inserted"""
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


# ============================================================================
# TEMPLATE 4: Search in Rotated Sorted Array
# ============================================================================

def search_rotated(nums, target):
    """Search in rotated sorted array"""
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


# Example usage
if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11, 13]
    print(binary_search(arr, 7))  # 3
    print(search_insert(arr, 6))  # 3
