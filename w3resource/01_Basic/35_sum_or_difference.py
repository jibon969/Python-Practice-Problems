"""
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def sum_or_equal(num, num1):
    if num == num1:
        return True
    elif num - num1 == 5:
        return True
    elif num + num == num+num1:
        return True
    return False

result = sum_or_equal(2, 2)
print(result)