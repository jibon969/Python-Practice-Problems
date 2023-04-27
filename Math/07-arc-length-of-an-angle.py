"""
 Write a Python program to calculate arc length of an angle.
 একটি কোণের আর্ক দৈর্ঘ্য গণনা করতে পাইথন প্রোগ্রাম লিখুন।
"""


def arc_length():
    pi = 22 / 7
    diameter = float(input('Diameter of circle: '))
    angle = float(input('angle measure: '))
    if angle >= 360:
        print("Angle is not possible")
        return
    length_of_arc = (pi * diameter) * (angle / 360)
    print("Arc Length is: ", length_of_arc)


arc_length()
