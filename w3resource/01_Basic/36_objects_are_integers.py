"""
Write a Python program to add two objects if both objects are integers.
"""

def check_both_object_integer(obj, obj2):
    if type(obj) == type(obj2):
        return obj  + obj2
    else:
        return "Inputs must be integers!"
    

result = check_both_object_integer(2, 3)
print(result)


# def check_both_object_integer(obj, obj2):
    
#     if not (isinstance(obj, int) and isinstance(obj, int)):
#         return "Inputs must be integers!"
#     return obj + obj2

# result = check_both_object_integer("2", 3)
# print(result)