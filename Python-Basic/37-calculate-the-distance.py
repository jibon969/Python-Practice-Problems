"""
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
case : distance (x1, y1)
case : distance (x2, y2)

√[(x₂ - x₁)² + (y₂ - y₁)²].

"""

import math
x1 = 4
y1 = 0

x2 = 6
y2 = 6

result = ((x2 - x1)**2 + (y2 - y1)**2)
x = math.sqrt(result)
print(x)

