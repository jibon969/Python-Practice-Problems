"""
Write a Python program to find the least common multiple (LCM) of two positive integers.

case 1 : two positive integers
case 2 : find the least common multiple
a =  2 ===> 1*2 = 2
b =  5 ===> 1*2*3*4*5
"""

a = 4
b = 6

counter = 1
a_set = set()
b_set = set()

while True:
    a_result = counter * a  #
    b_result = counter * b  # 10
    a_set.add(a_result)
    b_set.add(b_result)

    c = a_set.intersection(b_set)
    if c:
        print("LCM", c)
        break
    else:
        counter += 1
