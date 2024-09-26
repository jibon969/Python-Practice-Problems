"""
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.
"""

my_str = ["abcdefgh"]
for i in my_str:
    x = i[:2]
    y = x + x
    print(y)