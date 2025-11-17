# Bit Manipulation - Complete Guide

## 🎯 What is Bit Manipulation?

Operations on individual bits of numbers. Faster and more space-efficient than arithmetic!

**Binary Representation:**
```
5 in decimal = 101 in binary
         421
         101
         = 4 + 0 + 1 = 5
```

## 🧠 Basic Bit Operations

### AND (&)
```
  101  (5)
& 011  (3)
-----
  001  (1)

Both bits must be 1
```

### OR (|)
```
  101  (5)
| 011  (3)
-----
  111  (7)

At least one bit is 1
```

### XOR (^)
```
  101  (5)
^ 011  (3)
-----
  110  (6)

Bits are different
Key property: x ^ x = 0, x ^ 0 = x
```

### NOT (~)
```
~101 = ...11111010  (inverts all bits)
```

### Left Shift (<<)
```
5 << 1
101 → 1010  (10)
Multiplies by 2
```

### Right Shift (>>)
```
5 >> 1
101 → 10  (2)
Divides by 2
```

## 🎨 Common Bit Tricks

### Check if Kth bit is set
```python
def is_bit_set(num, k):
    return (num & (1 << k)) != 0
```

### Set Kth bit
```python
def set_bit(num, k):
    return num | (1 << k)
```

### Clear Kth bit
```python
def clear_bit(num, k):
    return num & ~(1 << k)
```

### Toggle Kth bit
```python
def toggle_bit(num, k):
    return num ^ (1 << k)
```

### Check if power of 2
```python
def is_power_of_2(n):
    return n > 0 and (n & (n - 1)) == 0

# Why? Power of 2 has single 1-bit
# 8 = 1000, 8-1 = 0111
# 1000 & 0111 = 0
```

### Count set bits (1s)
```python
def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Or use Brian Kernighan's algorithm:
def count_bits_fast(n):
    count = 0
    while n:
        n &= (n - 1)  # Clears rightmost 1-bit
        count += 1
    return count
```

## 💡 Classic Problems

### 1. Single Number
```python
def singleNumber(nums):
    """Find number that appears once (others appear twice)"""
    result = 0
    for num in nums:
        result ^= num  # XOR cancels pairs!
    return result

# [4,1,2,1,2] → 4
# 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4
```

### 2. Hamming Distance
```python
def hammingDistance(x, y):
    """Count differing bits"""
    return bin(x ^ y).count('1')
```

### 3. Reverse Bits
```python
def reverseBits(n):
    result = 0
    for i in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
```

### 4. Missing Number
```python
def missingNumber(nums):
    """Array [0..n] with one missing number"""
    result = len(nums)
    for i, num in enumerate(nums):
        result ^= i ^ num
    return result
```

## ⚡ Key Problems

**Easy:**
- Single Number ⭐
- Number of 1 Bits
- Reverse Bits
- Missing Number

**Medium:**
- Counting Bits
- Sum of Two Integers
- Single Number II

**Hard:**
- Maximum XOR of Two Numbers

## 🔑 Why Use Bit Manipulation?

- ✅ **Fast**: Bit ops are O(1)
- ✅ **Space efficient**: Compress data
- ✅ **Elegant**: Solve problems cleverly
- ✅ **Low-level**: Systems programming

## 💡 XOR Properties (Most Important!)

```
x ^ 0 = x
x ^ x = 0
x ^ y = y ^ x  (commutative)
(x ^ y) ^ z = x ^ (y ^ z)  (associative)
```

These properties make XOR powerful for:
- Finding unique elements
- Swapping without temp variable
- Missing number problems

## ⚡ Complexity

Most bit operations: O(1) per operation
Counting bits: O(log n) or O(number of bits)

---
**Bit manipulation is like magic - powerful and elegant!** ✨
