
"""
Given two numbers, return True if the sum of both numbers is less than 100.
Otherwise return False.
"""


def less_than_100(a, b):
    sum = a + b
    if sum <= 100:
        return True
    else:
        return False


ans = less_than_100(83, 34)
print(ans)

