"""
Write a Python program that accepts a sequence of comma-separated numbers 
from the user and generates a list and a tuple of those numbers.
"""

# Output
"""
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

my_list = input("Enter your number : ")
new_list = my_list.split(",")

convert_tuple = tuple(new_list)
convert_list = list(new_list)

print(convert_tuple)
print(convert_list)
