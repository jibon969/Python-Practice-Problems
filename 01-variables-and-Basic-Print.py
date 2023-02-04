
# Variables and Basic Print

"""
1. Print "Hello World"
"""
print("Hello World")


"""
2. Create a variable named "name" that contains a string -a name
print "Hello" <name>
Example : Hello Jibon
"""

name = "Jibon "
print("Hello " + name)
print("\n")

"""
3. Create three variables to hold three strings - title, first, and last names
Print "Hello <title> <first> <last>
Example : Hello Mr Jibon Ahmed
"""
title = "Mr"
first = "Jibon"
last = "Ahmed"
print("Hello ", end=" ")
print(first, end=" ")
print(last, end=" ")
print("\n")

"""
4. Print "chicken chicken chicken chicken" by manually specifying the string chicken only once
Example : chicken chicken chicken chicken
"""

a = "chicken "
print(a*4)

# or
var = "chicken"
print((var + " ")*4)
print("\n")


"""
5. One on each line using only print statement
chicken
chicken
chicken
chicken
"""

b = "chicken\n"
print(b*4)
print("\n")

"""
6. There are three "chickens" in the house -  with the quotes around the world chickens
Example : There are three "chickens" in the house
"""

print("here are three \"chickens\" in the house")


