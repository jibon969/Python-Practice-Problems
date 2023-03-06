
"""
Write a Python program that accepts a sequence of comma-separated numbers from
the user and generates a list and a tuple of those numbers
"""

x = input("Enter your number : ").replace(' ', '')
y = x.split(',')

new_list = list(y)
print(new_list)

new_tuple = tuple(y)
print(new_tuple)