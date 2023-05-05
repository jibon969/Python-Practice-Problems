"""
Write a Python program to get the execution time of a Python method. 
"""

import time

# get the start time
st = time.time()

empty_list = []

# for i in range(1, 1000):
#     if i % 2 == 0:
#         empty_list.append(i)
# print(empty_list)

sum_x = 0
for i in range(1000000):
    sum_x += i

print("Sum :", sum_x)
# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

# or

import datetime
# print(datetime.datetime.now())

start_time = datetime.datetime.now()
for i in range(1, 100):
    print(i)
end_time = datetime.datetime.now()

result = end_time - start_time
print(result)
