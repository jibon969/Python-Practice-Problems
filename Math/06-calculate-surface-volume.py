"""
 Write a Python program to calculate surface volume and area of a sphere
 একটি গোলকের পৃষ্ঠের পরিমাণ এবং ক্ষেত্রফল গণনা করুন /
 Formula :
 1. The  area of a sphere is A = 4*π*r2
 2.  radius of the sphere V = 4/3*π*r3
"""
import math

pi = math.pi
radian = float(input("Enter Radius of sphere : "))
sur_area = 4 * pi * radian ** 2
volume = (4 / 3) * (pi * radian ** 3)
print("Surface Area is :", sur_area)
print("Volume is : ", volume)
