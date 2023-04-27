"""
Write a Python program that determines whether a given number
(accepted from the user) is even or odd,
and prints an appropriate message to the user.
"""

user = int(input("Enter your number : "))
if user % 2 == 0:
    print("Even number")
else:
    print("Odd number")
