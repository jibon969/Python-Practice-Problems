"""
1. Write a Python program that accepts the user's first and last name and prints them
in reverse order with a space between them
"""

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
print(last_name, first_name)


def reverse_order(first_name, last_name):
    first_name, last_name = last_name, first_name

    return first_name + " " + last_name


output = reverse_order("Ahmed", "Jibon")
print("Result : ", output)


# Swap variable
a = 5
b = 6
a, b = b, a

print(a)
print(b)
