"""
Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""
x = 50000
if x <= 100:
    print(100)
elif x > 100 and x <= 1000:
    print(1000)
elif x > 1000 and x <= 2000:
    print(2000)
else:
    print("out of range")