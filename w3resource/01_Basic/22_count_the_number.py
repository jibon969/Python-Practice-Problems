"""
Write a Python program to count the number 4 in a given list.
"""

list_count_4 = [1, 4, 6, 7, 4, 4]
count = 0
for i in list_count_4:
    if i == 4:
        count = count + 1
print(count)