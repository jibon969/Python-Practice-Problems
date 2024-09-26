"""
 Write a Python program that determines whether a given number (accepted from the user) 
 is even or odd, and prints an appropriate message to the user.
"""


number = int(input("Enter your number : "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd Number")
