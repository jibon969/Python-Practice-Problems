"""
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.
"""

# Case 1 
"""
num1 = 1
num2 = 2
num3 = 3
"""
# output : 6

# Case 2
"""
num1 = 3
num2 = 3
num3 = 3
"""
# output : 27

num1 = 1
num2 = 2
num3 = 3

total_sun = num1 + num2 + num3
if num1 == num2 or num2 == num3:
    result =  total_sun * 3
    print(result)
else:
    print(total_sun)


# Use Function ===================================
def calculate_given_number(x, y, z):
    
    if x == y or y == z:
        result = (x+y+z) * 3
        return result
    else:
        return x + y + z

result = calculate_given_number(3,3,3)
print(result)