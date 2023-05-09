"""
Write a Python program to calculate the body mass index.
bmi formula example
bmi = weight(kg) / height(m)2
"""

weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height*height)
print("body mass index : ", bmi)
