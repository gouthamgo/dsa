"""
Math & Geometry - Code Templates
=================================

Matrix manipulation done in place, plus the number-theory routines that keep
reappearing: gcd/lcm, sieve, fast power, digit surgery, cycle detection.
"""


# ============================================================================
# TEMPLATE 1: Rotate a Matrix 90 Degrees In Place
# ============================================================================

def rotate_matrix(matrix):
    """Rotate an n x n matrix clockwise, O(1) extra space."""
    n = len(matrix)

    # Step 1 - transpose (mirror across the main diagonal).
    # Start j at i so each pair is swapped once; starting at 0 would swap
    # every pair twice and undo the transpose.
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2 - reverse each row (mirror left-right).
    # Transpose + horizontal mirror == 90 degree clockwise rotation.
    for row in matrix:
        row.reverse()

    return matrix


def rotate_matrix_ccw(matrix):
    """Counter-clockwise: transpose, then reverse the COLUMN order instead."""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    matrix.reverse()  # flips top-to-bottom
    return matrix


# ============================================================================
# TEMPLATE 2: Spiral Traversal
# ============================================================================

def spiral_order(matrix):
    """Walk a matrix in spiral order using four shrinking boundaries."""
    if not matrix or not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Across the top row, then retire that row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Down the right column, then retire it
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # The two guards below matter for single-row / single-column leftovers:
        # without them the last line would be re-read backwards.
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


# ============================================================================
# TEMPLATE 3: Set Matrix Zeroes in O(1) Space
# ============================================================================

def set_zeroes(matrix):
    """Zero out the row and column of every 0, using row 0 / column 0 as flags."""
    rows, cols = len(matrix), len(matrix[0])

    # Row 0 and column 0 will serve as the marker strips, but they overlap at
    # cell (0,0) and so cannot encode both themselves. Record column 0
    # separately first.
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(rows))
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(cols))

    # Pass 1: for each interior zero, stamp its row header and column header
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Pass 2: apply the markers to the interior only (headers still hold flags)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Pass 3: finally clear the marker strips themselves, using the two
    # booleans saved before the markers overwrote the originals.
    if first_row_has_zero:
        for j in range(cols):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(rows):
            matrix[i][0] = 0

    return matrix


# ============================================================================
# TEMPLATE 4: GCD and LCM (Euclid)
# ============================================================================

def gcd(a, b):
    """Greatest common divisor - repeatedly replace the pair by (b, a mod b)."""
    # gcd(a, b) == gcd(b, a mod b); the remainder strictly shrinks, so this
    # terminates, ending when b hits 0 and a holds the divisor.
    while b:
        a, b = b, a % b
    return abs(a)


def gcd_recursive(a, b):
    """Same recurrence, written recursively."""
    return abs(a) if b == 0 else gcd_recursive(b, a % b)


def lcm(a, b):
    """Least common multiple - divide FIRST to keep the product small."""
    if a == 0 or b == 0:
        return 0
    return abs(a // gcd(a, b) * b)


# ============================================================================
# TEMPLATE 5: Primes
# ============================================================================

def is_prime(n):
    """Trial division up to sqrt(n) - any factor above it has a partner below."""
    if n < 2:
        return False
    if n < 4:
        return True  # 2 and 3
    if n % 2 == 0:
        return False

    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2  # even divisors were already ruled out
    return True


def sieve_of_eratosthenes(n):
    """All primes <= n. O(n log log n)."""
    if n < 2:
        return []

    is_composite = [False] * (n + 1)
    primes = []

    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)

            # Start crossing off at i*i: every smaller multiple of i already
            # has a smaller prime factor and was struck out earlier.
            for multiple in range(i * i, n + 1, i):
                is_composite[multiple] = True

    return primes


# ============================================================================
# TEMPLATE 6: Fast Exponentiation
# ============================================================================

def my_pow(x, n):
    """Pow(x, n) by binary exponentiation - O(log n) multiplications."""
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    base = x

    while n > 0:
        # n's binary digits pick which squarings contribute:
        # x^13 == x^8 * x^4 * x^1 because 13 == 1101 in binary
        if n & 1:
            result *= base
        base *= base  # base is now x^(2^k) for the next bit
        n >>= 1

    return result


def mod_pow(base, exponent, modulus):
    """(base ** exponent) % modulus without ever building the huge number."""
    if modulus == 1:
        return 0

    result = 1
    base %= modulus  # reduce early; (a*b) % m == ((a%m) * (b%m)) % m

    while exponent > 0:
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1

    return result


# ============================================================================
# TEMPLATE 7: Digit Manipulation
# ============================================================================

def reverse_integer(x):
    """Reverse a signed 32-bit integer's digits; return 0 on overflow."""
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    sign = -1 if x < 0 else 1
    x = abs(x)

    result = 0
    while x:
        result = result * 10 + x % 10  # x % 10 peels the last digit
        x //= 10                       # // 10 drops it

    result *= sign

    # Python ints never wrap, so the 32-bit bound is enforced by hand
    return result if INT_MIN <= result <= INT_MAX else 0


def is_palindrome_number(x):
    """Palindrome Number - compare against half the digits, no string used."""
    # Negatives read as -121 <-> 121-, and any nonzero number ending in 0
    # would need a leading 0 to match.
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reverted = 0
    # Stop once the reverted tail has caught up with the shrinking head
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x //= 10

    # Even digit count: halves match exactly.
    # Odd digit count: drop the middle digit with reverted // 10.
    return x == reverted or x == reverted // 10


def plus_one(digits):
    """Add 1 to a number stored as a digit array."""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits  # no carry: done
        digits[i] = 0      # 9 becomes 0 and the carry continues left

    return [1] + digits    # carried off the front: 999 -> 1000


def digit_sum_of_squares(n):
    """Helper for happy numbers: replace n by the sum of its squared digits."""
    total = 0
    while n:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


# ============================================================================
# TEMPLATE 8: Cycle Detection on a Number Sequence
# ============================================================================

def is_happy_set(n):
    """Happy Number via a seen-set - simple, O(log n) space."""
    seen = set()

    # The sequence is deterministic, so revisiting a value means a cycle
    while n != 1 and n not in seen:
        seen.add(n)
        n = digit_sum_of_squares(n)

    return n == 1


def is_happy_floyd(n):
    """Same, with Floyd's tortoise-and-hare - O(1) space."""
    slow = n
    fast = digit_sum_of_squares(n)

    # If a cycle exists the fast pointer laps the slow one inside it;
    # if the sequence reaches 1 it sticks there (1 -> 1) and both meet at 1.
    while fast != 1 and slow != fast:
        slow = digit_sum_of_squares(slow)
        fast = digit_sum_of_squares(digit_sum_of_squares(fast))

    return fast == 1


# Example usage
if __name__ == "__main__":
    print(rotate_matrix([[1, 2], [3, 4]]))            # [[3,1],[4,2]]
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(gcd(48, 18), gcd_recursive(48, 18), lcm(4, 6))  # 6 6 12
    print(is_prime(97), sieve_of_eratosthenes(30))
    print(my_pow(2.0, 10), mod_pow(2, 100, 1_000_000_007))
    print(reverse_integer(-123), reverse_integer(1534236469))  # -321 0
    print(is_palindrome_number(121), is_palindrome_number(10))  # True False
    print(plus_one([1, 2, 9]))                        # [1,3,0]
    print(is_happy_set(19), is_happy_floyd(19))       # True True
    print(is_happy_set(2), is_happy_floyd(2))         # False False
