
# Problems : Write a Python program to calculate surface volume and area of a cylinder

"""
পৃষ্ঠের পরিমাণ এবং একটি সিলিন্ডারের ক্ষেত্রফল
Volume = πr2h
link : https://ncalculators.com/geometry/cylinder-calculator.htm
"""

import math

height = float(input("Enter Height of cylinder : "))
radius = float(input("Enter Radius of cylinder : "))
pi = math.pi
result = (pi * radius**2) * height
print('Calculate surface volume : ', result)



