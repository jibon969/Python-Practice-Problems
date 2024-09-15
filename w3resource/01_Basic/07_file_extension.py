"""
Write a Python program that accepts a filename from the user and prints the extension of the file.
"""

# Output
"""
Sample filename : math.py
Output : py
"""

file_name = input('Enter your file name : ')
extension_name = file_name.split(".")
print(extension_name[-1])