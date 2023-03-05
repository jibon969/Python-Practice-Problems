
# Write a Python program to display the current date and time.

from datetime import datetime

date_time = datetime.today()
current_date_time = date_time.strftime("%y-%m-%d %H:%M:%S")
"""
2. %y-%m-%d  = year, month, date
1. %H:%M%S    = Hour, Minute, Second
"""
print("current date time : ", current_date_time)
print("\n")


def current_date_time():
    today_date = datetime.today()
    current_time = today_date.strftime("%y-%m-%d %H:%M:%S")
    return current_time


result = current_date_time()
print("current date time : ", result)