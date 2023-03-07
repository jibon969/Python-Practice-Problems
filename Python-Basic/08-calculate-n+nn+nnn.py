"""
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
"""

n = int(input("Enter number : "))
# n+nn+nnn

a = str(n)
b = a + a
print(b)
c = n + int((a+a)) + int(a+a+a)
# c = 5 + 55 + 555
print(c)