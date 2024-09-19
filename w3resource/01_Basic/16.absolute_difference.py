"""
write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.
"""

# given_number = 14
# if given_number > 17:
#     difference = given_number - 17
#     print(difference*2)
# else:
#     result =  (given_number - 17)
#     print(abs(result))


def number_difference(number):
    if number > 17:
        difference = number - 17
        return (difference*2)
    else:
        difference = number - 17
        return abs(difference)

result = number_difference(22)
print("difference : ", result)