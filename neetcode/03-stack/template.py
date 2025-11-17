"""
Stack - Code Templates
======================
"""

# ============================================================================
# TEMPLATE 1: Valid Parentheses
# ============================================================================

def is_valid_parentheses(s):
    """Match opening/closing brackets"""
    stack = []
    matching = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in matching:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or matching[stack.pop()] != char:
                return False

    return len(stack) == 0


# ============================================================================
# TEMPLATE 2: Monotonic Stack
# ============================================================================

def next_greater_element(nums):
    """Find next greater element for each number"""
    result = [-1] * len(nums)
    stack = []  # Store indices

    for i in range(len(nums)):
        # While current is greater than stack top
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]

        stack.append(i)

    return result


# ============================================================================
# TEMPLATE 3: Min Stack
# ============================================================================

class MinStack:
    """Stack that supports O(1) getMin()"""

    def __init__(self):
        self.stack = []
        self.min_stack = []  # Track minimums

    def push(self, val):
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Example usage
if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))  # True
    print(next_greater_element([2,1,2,4,3]))  # [4,2,4,-1,-1]
