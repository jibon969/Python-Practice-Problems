"""
Write a Python program that converts seconds into days, hours, minutes, and seconds.

Case 1 : 60 second  = 1 minutes
case 2 : 60 minutes = 1 hours
case 3 : 24 hours   = 1 day

case 4 : 1 minutes = 3600 second
case 5 : 86400 second = 24 hours (1 day)

case 6 : 1 hours = second 60 *60

"""

# input

"""
23 hours
59 minute
59 second
86399
"""

second = 60
minute = 60
hour = 24

time = float(input("Enter your time in second : "))
day = time * minute * hour
print("Day      :", day)

hour_ = time * minute
print("Hour     : ", hour_)

minute_ = time // second
print("Minute   : ", minute_)

second_ = time
print("Second   : ", second)

