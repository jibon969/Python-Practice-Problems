
"""
Write a Python program to add two objects if both objects are integers
"""

a = 33
b = 6
if isinstance(a, int) and isinstance(b, int):
    print(a+b)
else:
    print("Inputs must be integers!")


def add_two_object(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        print("Inputs must be integers!")


output = add_two_object(20, 4)
print(output)