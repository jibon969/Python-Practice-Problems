"""
Write a Python program that prints the calendar for a given month and year.
"""
import calendar
import datetime


year =  datetime.datetime.now().year
month =  datetime.datetime.now().month
x = calendar.month(year, month)
print(x)


"""
Print all month
"""

all_month = calendar.calendar(2024)
print(all_month)

