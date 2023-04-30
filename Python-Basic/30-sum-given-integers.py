"""
Write a Python program to sum three given integers. 
However, if two values are equal, the sum will be zero.

case 1 : sum three given integers
case 2 : if two values are equal, the sum will be zero.
"""

a = 1
b = 1
c = 1

d = a + b + c

if a == b or b == c or a == c:
    print("Zero")
else:
    print(d)


def three_integer(a, b, c):
    if a == b or b == c or a == c:
        x = "Zero"
        return x
    else:
        return a + b + c


d = three_integer(20, 60, 7)
# print(d)
