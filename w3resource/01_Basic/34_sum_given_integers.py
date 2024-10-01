"""
Write a Python program to sum two given integers. 
However, if the sum is between 15 and 20 it will return 20.
"""

num = 10
num2 = 8

sum = num + num2
if sum <= 20:
    print(20)
else:
    print(sum)
