"""
 Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

num = 10
num2 = 1
num3 = 13

if num == num2 or num2 == num3 or num == num3:
    sum = 0
    print(sum)
else:
    sum = num + num2 + num3
    print(sum)
