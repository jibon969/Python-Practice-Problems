"""
 Write a Python program that calculates the area of a circle based on the radius entered by the user
"""

import math


def area_circle():
    """
    Formula : πr2
    https://www.cuemath.com/geometry/area-of-a-circle/
    :return:
    """
    radius = 1.1
    circle = math.pi * radius**2
    return circle


output = area_circle()
print("Result : ", output)
