"""
Write a program to iterate the first 10 numbers and in each iteration,
print the sum of the current and previous number.
"""

previous_number = 0

for i in range(1, 11):
    x = previous_number + i
    print("Current Number", i, "Previous Number", previous_number, "Sum", previous_number + i)

    previous_number = i
