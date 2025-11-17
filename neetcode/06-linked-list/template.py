"""
Linked List - Code Templates
============================
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================================
# TEMPLATE 1: Reverse Linked List
# ============================================================================

def reverse_list(head):
    """Reverse a linked list"""
    prev = None
    current = head

    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp

    return prev


# ============================================================================
# TEMPLATE 2: Find Middle (Slow & Fast Pointers)
# ============================================================================

def find_middle(head):
    """Find middle node"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# ============================================================================
# TEMPLATE 3: Detect Cycle
# ============================================================================

def has_cycle(head):
    """Detect if linked list has cycle"""
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# ============================================================================
# TEMPLATE 4: Merge Two Sorted Lists
# ============================================================================

def merge_two_lists(l1, l2):
    """Merge two sorted linked lists"""
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2

    return dummy.next


# ============================================================================
# TEMPLATE 5: Remove Nth From End
# ============================================================================

def remove_nth_from_end(head, n):
    """Remove nth node from end"""
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both until fast reaches end
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next
