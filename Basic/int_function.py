
# int () function

# Example 1
first_number = int(input("Enter your first number : "))
second_number = int(input("Enter your second number : "))
total = first_number + second_number
print(total)

# Example 2
number1 = str(4)
number2 = float("44")
number3 = int("44")
print(type(number2))
print(number2+number3)


# Two or more input in one line
# Split is string method
name, age = input("Enter your name & age : ").split(",")
print(name)
print(age)
print("\n")

# Example
"""
input three numbers and you have to print average of 
three numbers using string formatting.
"""

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

average = a + b + c / 3
print(average)
