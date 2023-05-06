
"""
 Write a Python program to convert height (in feet and inches) to centimeters
"""

height_feet = int(input("Feet: "))
height_inch = int(input("Inches: "))

height_inch += height_feet * 12
height_cm = round(height_inch * 2.54, 1)

print("Your height is : %d cm." % height_cm)