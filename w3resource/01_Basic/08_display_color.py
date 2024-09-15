"""
Write a Python program to display the first and last colors from the following list.
"""

"""
# Input :
color_list = ["Red","Green","White" ,"Black"]
output : "Red", "Black"
"""

color_list = ["Red","Green","White" ,"Black"]
first_color = color_list[0]
last_color = color_list[-1]
print(first_color + " " + last_color)

# using string format also
print("%s %s" % (color_list[0], color_list[-1]))