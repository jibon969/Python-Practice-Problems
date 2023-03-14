
"""
Write a Python program to calculate the area of the sector.
সেক্টরের ক্ষেত্রফল।
Formula : pi r^2 d/360

"""

import math
pi = math.pi
radius = float(input("Enter Radius of a circle : "))
angle = float(input("Enter Angle measure : "))

result = pi * radius**2 * (angle/360)
print(result)

