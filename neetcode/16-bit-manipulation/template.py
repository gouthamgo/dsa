"""
Bit Manipulation - Code Templates
==================================

Operators: &  |  ^  ~  <<  >>

XOR is the workhorse:
    x ^ 0 = x        x ^ x = 0
    x ^ y = y ^ x    (x ^ y) ^ z = x ^ (y ^ z)

PYTHON CAVEAT: ints are arbitrary precision and negatives behave as if they
had infinitely many leading 1s. Anything that assumes a fixed 32-bit word
must mask explicitly - see TEMPLATE 6.
"""


# ============================================================================
# TEMPLATE 1: Single-Bit Operators (Cheat Sheet)
# ============================================================================

def get_bit(num, k):
    """Is bit k set? Shift a 1 into position and test the overlap."""
    return (num >> k) & 1  # 1 if set, 0 if not


def is_bit_set(num, k):
    """Same test, written as a boolean."""
    return (num & (1 << k)) != 0


def set_bit(num, k):
    """Force bit k to 1. OR with a mask leaves every other bit alone."""
    return num | (1 << k)


def clear_bit(num, k):
    """Force bit k to 0. ~(1 << k) is all 1s except at position k."""
    return num & ~(1 << k)


def toggle_bit(num, k):
    """Flip bit k. XOR with 1 inverts; XOR with 0 preserves."""
    return num ^ (1 << k)


def update_bit(num, k, value):
    """Write an arbitrary 0/1 into bit k: clear it first, then OR it in."""
    cleared = num & ~(1 << k)
    return cleared | ((value & 1) << k)


def is_power_of_two(n):
    """A power of two has exactly one set bit."""
    # 8 = 1000, 7 = 0111 -> the AND is 0. Any extra set bit survives.
    return n > 0 and (n & (n - 1)) == 0


def lowest_set_bit(n):
    """Isolate the rightmost 1-bit (n & -n), e.g. 12 (1100) -> 4 (100)."""
    # -n is two's complement: ~n + 1, which flips every bit above the lowest
    # 1 and leaves that bit standing. Only that one position matches.
    return n & -n


def clear_lowest_set_bit(n):
    """Drop the rightmost 1-bit: 12 (1100) -> 8 (1000)."""
    return n & (n - 1)


# ============================================================================
# TEMPLATE 2: Counting Set Bits
# ============================================================================

def count_bits_naive(n):
    """Number of 1 Bits - inspect every bit position. O(total bits)."""
    count = 0
    while n:
        count += n & 1  # test the lowest bit
        n >>= 1         # slide the next bit down
    return count


def count_bits_kernighan(n):
    """Brian Kernighan's - loops once per SET bit, not once per bit."""
    count = 0
    while n:
        # n - 1 flips the rightmost 1 to 0 and every 0 below it to 1;
        # ANDing therefore erases exactly that rightmost 1 and nothing else.
        #   12 = 1100, 11 = 1011  ->  1100 & 1011 = 1000
        n &= n - 1
        count += 1
    return count


def counting_bits_dp(n):
    """Counting Bits - set-bit count for every i in 0..n, in O(n) total."""
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # i >> 1 is i without its lowest bit position, already computed;
        # add back whether that dropped bit was a 1.
        dp[i] = dp[i >> 1] + (i & 1)

    return dp


# ============================================================================
# TEMPLATE 3: XOR Tricks
# ============================================================================

def single_number(nums):
    """Every value appears twice except one - XOR cancels the pairs."""
    result = 0
    for num in nums:
        result ^= num  # x ^ x = 0, so only the lonely value survives
    return result


def missing_number(nums):
    """Array holds 0..n with one value missing - XOR indices against values."""
    result = len(nums)  # seed with n, the one index that has no slot

    for i, num in enumerate(nums):
        # Every present value cancels its matching index; the gap remains
        result ^= i ^ num

    return result


def swap_without_temp(a, b):
    """Swap two ints using XOR only (a party trick - tuple unpacking is better)."""
    a = a ^ b  # a now holds the difference pattern
    b = a ^ b  # (a^b)^b == original a
    a = a ^ b  # (a^b)^new_b == original b
    return a, b


def hamming_distance(x, y):
    """Count positions where x and y differ - XOR marks them, then count."""
    return count_bits_kernighan(x ^ y)


# ============================================================================
# TEMPLATE 4: Reverse Bits
# ============================================================================

def reverse_bits(n):
    """Reverse the 32 bits of an unsigned integer."""
    result = 0
    for _ in range(32):
        # Shift the answer left to open a slot, then pour in n's lowest bit
        result = (result << 1) | (n & 1)
        n >>= 1
    return result


# ============================================================================
# TEMPLATE 5: Bitmask Subset Enumeration
# ============================================================================

def all_subsets(items):
    """Every subset of `items`, one per integer in 0 .. 2^n - 1."""
    n = len(items)
    subsets = []

    # Each mask is an n-bit selector: bit i set means items[i] is included
    for mask in range(1 << n):  # 1 << n == 2**n
        subset = [items[i] for i in range(n) if mask & (1 << i)]
        subsets.append(subset)

    return subsets


def submasks(mask):
    """Enumerate every submask of `mask` (subsets of its set bits)."""
    result = []
    sub = mask

    while sub > 0:
        result.append(sub)
        # Subtracting 1 borrows through the low zeros; re-ANDing with mask
        # snaps back to the next smaller submask. Runs in O(2^popcount).
        sub = (sub - 1) & mask

    result.append(0)  # the empty submask, which the loop exits before adding
    return result


# ============================================================================
# TEMPLATE 6: Addition Without '+'  (the Python trap)
# ============================================================================

def get_sum(a, b):
    """Sum of Two Integers - add using only bitwise operators.

    THE TRAP: in C/Java the carry eventually shifts out of the 32-bit word
    and the loop ends. Python ints are arbitrary precision, so for a negative
    operand the carry keeps growing forever and the loop NEVER terminates.
    The fix is to emulate a 32-bit word by masking after every step, then
    convert the result back to a signed Python int at the end.
    """
    MASK = 0xFFFFFFFF   # keeps values inside a 32-bit window
    MAX_INT = 0x7FFFFFFF  # largest positive value in that window

    a &= MASK  # negatives become their 32-bit two's-complement pattern
    b &= MASK

    while b:
        # Positions where both have a 1 produce a carry into the next column
        carry = ((a & b) << 1) & MASK
        # XOR is addition with the carries thrown away
        a = (a ^ b) & MASK
        b = carry
        # Masking guarantees termination: the carry only ever moves left, and
        # anything past bit 31 is discarded, so b reaches 0 within 32 rounds.

    # Anything above MAX_INT is really a negative number in two's complement
    return a if a <= MAX_INT else ~(a ^ MASK)


def get_sum_nonnegative(a, b):
    """Simpler variant, valid ONLY for a, b >= 0 - no masking needed.

    With both operands non-negative the carry strictly marches leftward and
    dies out on its own, so arbitrary-precision ints cause no trouble.
    """
    assert a >= 0 and b >= 0, "negative inputs require the masked version"

    while b:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    return a


# ============================================================================
# TEMPLATE 7: Reverse Integer with 32-bit Overflow Check
# ============================================================================

def reverse_integer(x):
    """Reverse the digits of a signed 32-bit int; return 0 if it overflows."""
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        result = result * 10 + x % 10  # pull the last digit off and append it
        x //= 10

    result *= sign

    # Python never overflows, so the bound has to be checked by hand
    return result if INT_MIN <= result <= INT_MAX else 0


# Example usage
if __name__ == "__main__":
    print(get_bit(5, 0), get_bit(5, 1), get_bit(5, 2))   # 1 0 1
    print(set_bit(5, 1), clear_bit(5, 0), toggle_bit(5, 2))  # 7 4 1
    print(is_power_of_two(8), is_power_of_two(6))        # True False
    print(lowest_set_bit(12), clear_lowest_set_bit(12))  # 4 8
    print(count_bits_naive(11), count_bits_kernighan(11))  # 3 3
    print(counting_bits_dp(5))                           # [0,1,1,2,1,2]
    print(single_number([4, 1, 2, 1, 2]))                # 4
    print(missing_number([3, 0, 1]))                     # 2
    print(swap_without_temp(3, 7))                       # (7, 3)
    print(hamming_distance(1, 4))                        # 2
    print(len(all_subsets([1, 2, 3])))                   # 8
    print(submasks(0b101))                               # [5, 4, 1, 0]
    print(get_sum(2, 3), get_sum(-2, 3), get_sum(-5, -7))  # 5 1 -12
    print(get_sum_nonnegative(2, 3))                     # 5
    print(reverse_integer(-123), reverse_integer(1534236469))  # -321 0
