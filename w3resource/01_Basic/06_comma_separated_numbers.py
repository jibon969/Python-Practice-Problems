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

values = input("Input some comma-separated numbers: ")

list = values.split(",")

tuple = tuple(list)

# Print the list
print('List : ', list)

# Print the tuple
print('Tuple : ', tuple)
