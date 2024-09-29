"""
Write a Python program that concatenates all elements in a list into a string and returns it.
"""

my_list = [1, 5, 12, 2]

new_list = ""
for i in my_list:
    new_list +=  str(i)
print(new_list)

