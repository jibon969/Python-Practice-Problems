"""
Write a Python program to sum two given integers.
However, if the sum is between 15 and 20 it will return 20.
"""

a = 7
b = 10

sum = a + b

if sum > 15 and sum < 20:
    print(sum)
else:
    print("No")


def sum_number(num1, num2):
    sum = num1 + num2
    if sum > 15 and sum < 20:
        return sum
    else:
        x = "No match"
        return x


result = sum_number(10, 6)
print(result)


def add_sum(num1, num2):
    sum = num1 + num2
    if sum in range(15, 20):
        return 20
    else:
        return sum


output = add_sum(10, 8)
print(output)

