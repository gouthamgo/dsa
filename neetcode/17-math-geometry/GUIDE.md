# Math & Geometry - Complete Guide

## 🎯 What is This Category?

Problems requiring mathematical reasoning, formulas, or geometric properties.

## 🧠 Common Math Concepts

### 1. Prime Numbers
```python
def is_prime(n):
    """Check if n is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

### 2. GCD (Greatest Common Divisor)
```python
def gcd(a, b):
    """Euclidean algorithm"""
    while b:
        a, b = b, a % b
    return a

# Or use built-in:
from math import gcd
```

### 3. LCM (Least Common Multiple)
```python
def lcm(a, b):
    return (a * b) // gcd(a, b)
```

### 4. Fast Power
```python
def power(x, n):
    """Compute x^n efficiently"""
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n

    result = 1
    current = x

    while n > 0:
        if n % 2 == 1:
            result *= current
        current *= current
        n //= 2

    return result
```

### 5. Factorial & Combinations
```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combination(n, k):
    """nCk = n! / (k! * (n-k)!)"""
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)
    return result
```

## 🎨 Geometry Concepts

### 1. Distance Between Points
```python
def distance(x1, y1, x2, y2):
    """Euclidean distance"""
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
```

### 2. Area of Triangle
```python
def triangle_area(x1, y1, x2, y2, x3, y3):
    """Using coordinate geometry"""
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2)
```

### 3. Rotate Point
```python
def rotate_90(x, y):
    """Rotate point 90° clockwise around origin"""
    return y, -x

def rotate_90_ccw(x, y):
    """Rotate point 90° counter-clockwise"""
    return -y, x
```

### 4. Check if Point in Rectangle
```python
def in_rectangle(px, py, x1, y1, x2, y2):
    """Check if point (px,py) in rectangle"""
    return x1 <= px <= x2 and y1 <= py <= y2
```

## 💡 Classic Problems

### 1. Rotate Image (Matrix)
```python
def rotate(matrix):
    """Rotate matrix 90° clockwise in-place"""
    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

### 2. Spiral Matrix
```python
def spiralOrder(matrix):
    """Return elements in spiral order"""
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Right
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Down
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            # Left
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            # Up
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result
```

### 3. Happy Number
```python
def isHappy(n):
    """Sum of squares of digits eventually reaches 1?"""
    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit)**2 for digit in str(n))

    return n == 1
```

### 4. Plus One
```python
def plusOne(digits):
    """Add 1 to number represented as array"""
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits  # Overflow case: 999 + 1 = 1000
```

## ⚡ Key Problems

**Easy:**
- Happy Number
- Plus One
- Rotate Image

**Medium:**
- Spiral Matrix ⭐
- Set Matrix Zeroes
- Pow(x, n)
- Detect Squares

**Hard:**
- Regular Expression Matching
- Valid Number

## 🔑 Problem-Solving Tips

### For Math:
1. **Look for patterns** in small examples
2. **Use formulas** when applicable
3. **Check edge cases**: 0, 1, negative numbers
4. **Modulo arithmetic** for large numbers

### For Geometry:
1. **Draw it!** Visual helps immensely
2. **Consider coordinate system**
3. **Use symmetry** when possible
4. **Watch for edge cases**: collinear points, overlapping shapes

## 💡 Important Math Patterns

### Modulo Arithmetic
```python
# For large numbers
(a + b) % m = ((a % m) + (b % m)) % m
(a * b) % m = ((a % m) * (b % m)) % m
```

### Sum Formulas
```python
# Sum 1 to n
sum_n = n * (n + 1) // 2

# Sum of squares 1 to n
sum_squares = n * (n + 1) * (2*n + 1) // 6
```

### Prime Sieve (Eratosthenes)
```python
def sieve(n):
    """Find all primes up to n"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [i for i in range(n + 1) if is_prime[i]]
```

---
**Math & Geometry problems test problem-solving creativity!** 📐
