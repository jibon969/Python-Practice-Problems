"""
Write a Python program that retrieves the
date and time of file creation and modification.
"""

import datetime
with open('test.txt', 'w') as test:
    if test:
        print(datetime.datetime.now())
    else:
        print("No, Edit")