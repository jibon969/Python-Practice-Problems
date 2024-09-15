"""
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
"""

# Output
"""
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""



import datetime
s = datetime.date.today()
x = s.strftime("%d / %m / %Y")
print(x)


# Now code 
exam_st_date = (11, 12, 2014)
# Note : The placeholders %i are used to format the integers
print("The examination will start from : %i / %i / %i" % exam_st_date)
# print(type("%i"))


"""
The said code creates a tuple called "exam_st_date" containing three integers: 11, 12, and 2014. 
It then uses string formatting to print a string that states 
"The examination will start from :" followed by the integers in the tuple in the order they appear, formatted as day/month/year. 
The placeholders %i are used to format the integers.
"""