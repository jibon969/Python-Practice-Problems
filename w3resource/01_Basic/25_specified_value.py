"""
Write a Python program that checks whether a specified value is contained within a group of values.
3 ->  [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False
"""


def check_number_list(num):
    my_list = [1, 5, 8, 3]
    for i in my_list:
        if num == i:
            return True
    return False

result = check_number_list(-1)
print(result)