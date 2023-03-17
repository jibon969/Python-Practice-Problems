"""
Given two integer numbers return their product only if the product is equal to or lower than 1000,
else return their sum.
"""


def multiplication_or_sum(num1, num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2


result = multiplication_or_sum(20, 30)
print("Result :", result)
