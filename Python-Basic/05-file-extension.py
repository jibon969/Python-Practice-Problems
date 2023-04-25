"""
Write a Python program that accepts a filename from the user and prints
the extension of the file.
"""
user_input = input("Enter your filename : ")
c = user_input.split('.')
print(c[-1])

