
"""
Write a Python program to sum the first n positive integers

Sum of Integers Formula:
    S = n(n + l)/2
    where,
    S = sum of the consecutive integers
    n = number of integers
    n = first term
    l = last term
"""

number = int(input("Enter your number : "))
output = number*(number + 1)/2
print(output)


sum = 0
for i in range(1, 3):
    sum += i
print(sum)
