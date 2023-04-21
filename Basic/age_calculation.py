import datetime
user_input = input("Enter your Age : ")
Age = datetime.date.today().year - int(user_input)
print("You Are " + str(Age) + " years old")
print('\n')
