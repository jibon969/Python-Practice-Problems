"""
In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, 
while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
"""

# year = 1900
# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#     print("even")
# else:
#     print("No")


# def is_leap(year):
#     leap = False
#     if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
#         return True
#     else:
#         return leap
# year = 1992
# print(is_leap(year))


def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    return leap

# Test with year 1992
year = 1992
print(is_leap(year))

