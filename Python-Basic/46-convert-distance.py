"""
 Write a Python program to convert the
 distance (in feet) to inches, yards,and miles.
    1 foot = 12 inches
    1 yard = 3 feet = 36 inches
    1 mile = 1,760 yards
    1 mile = 5,280 feet
    1 mile = 63,360 inches
"""

days = int(input("Input days: ")) * 3600 * 24
hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60
seconds = int(input("Input seconds: "))

time = days + hours + minutes + seconds
print("The  amounts of seconds", days)