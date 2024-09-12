"""
Write a Python program to display the current date and time.
"""

# Output
"""
Sample Output :
Current date and time :
2014-07-05 14:34:14
"""

import datetime

current_date_time = datetime.datetime.now()
date = current_date_time.strftime("%Y-%M-%d %H:%M:%S")
print("Current date and time : ", date)