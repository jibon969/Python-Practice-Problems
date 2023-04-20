# Escape Sequences
"""
Escape sequences allow you to include special characters in strings. 
To do this, simply add a backslash (\) before the character you want to escape.

https://www.python-ds.com/python-3-escape-sequences
https://www.freecodecamp.org/news/escape-sequences-python/
https://www.toolsqa.com/python/escape-sequences-in-python/
"""

"""
ESCAPE SEQUENCE	        MEANING
\	                    Backslash (\)
'	                    Single quote (')
"	                    Double quote (")
\n	                    ASCII Linefeed (adds newline)
\b	                    ASCII Backspace

"""

# Example
print("Hello \nWorld")

# Example
print("Hello \t World")

# Example
print("Hello \b World!")

# output : Line A \n Line B
print("Line A\\n Line B")
print("Line A\\t Line B")
print("This is 2 backslash \\\\")

print("This is 4 backslash \\\\\\\\")

# ************ print these following lines *****************
# 1. this is \\ double backslash
# 2. these are /|/\/\/\ mounains
# 3. he is      awesome (use escape sequence instead ofmanual spaces )
# 4. \" \n \t \' (print this is an output)

# Example 1
print("this is \\\\ double backslash")

# Example 2
print("these are /\\/\\/\/\\ mounains")

# Example 3
print("he is\tawesome")

# Example
print("\\\" \\n \\t \\'")
