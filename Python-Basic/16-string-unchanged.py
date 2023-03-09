"""
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is"
"""

x = "is This is string !"
y = x + "is "
if x.startswith('is'):
    print("actual : ", x)
else:
    print("change :", y)
