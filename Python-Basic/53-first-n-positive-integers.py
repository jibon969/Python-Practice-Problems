"""
 Write a Python program to sum the first n positive integers.
"""

user_input = int(input("Enter your number : "))

sum = 0
for i in range(user_input + 1):
    sum = sum + i

print(sum)

