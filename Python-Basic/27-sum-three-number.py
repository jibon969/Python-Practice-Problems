"""
Write a Python program to sum three given integers. 
However, if two values are equal, the sum will be zero.
"""
a = 10
b = 10
c = 30
d = a + b + c
if a == b and b == a:
    print("Zero")
else:
    print(d)