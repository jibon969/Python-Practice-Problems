"""
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is".
"""


given_string = "Is"
my_string = "IsEmpty"

if my_string[:2] == "Is":
    print("Already exits")
else:
    result = given_string + my_string
    print(result)

print("\n")


# using function ======================
give_str = "Is"
def check_string(name):
    if name[:2] ==  give_str:
        print("Already exits")
    else:
        result = give_str + name
        print(result)

check_string("Is")

