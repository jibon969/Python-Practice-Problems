"""
Write a  Python program to calculate the distance between the points (x1, y1) and (x2, y2).
"""

# Formula
"""
To summarize, the Euclidean distance between two data points can be calculated using the formula sqrt((x2 – x1)^2 + (y2 – y1)^2 + … + (zn – z1)^2). We can implement this formula in Python using a function that takes two points as input and returns the Euclidean distance
"""

import math

p1 = [4, 0]
p2 = [6, 6]

distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
print(distance)