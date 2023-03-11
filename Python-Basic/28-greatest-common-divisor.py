"""
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
divisor :
6 = 1, 2, 3
8 = 1, 2, 4
Common : 1, 2
greatest : 2
"""

a = 8
b = 6

a_divisor = [n for n in range(1, a + 1) if a % n == 0]
b_divisor = [n for n in range(1, b + 1) if b % n == 0]

c = set(a_divisor).intersection(set(b_divisor))
s = sorted(c)

print(s[-1])
