"""
Write a Python program that returns true if the two given
integer values are equal or their sum or difference is 5

"""


def check_values(num1, num2):
    if num1 == num2 or abs(num1-num2) == 5 or abs(num1+num2) == 5:
        return True
    else:
        return False


result = check_values(20, 15)
print(result)
