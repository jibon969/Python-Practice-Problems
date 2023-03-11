"""
Write a Python program to print all even numbers from a given list of numbers
in the same order and stop printing any after 237 in the sequence.

Case 1 : list all even number
Case 2 : stop printing any after 237
"""

numbers = [
    386, 462, 47, 418, 907, 344, 236, 237, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 743, 527
]

for i in sorted(numbers):
    # if i >= 237:
    #     break
    # elif i % 2 == 0:
    #     print(i)

    if i % 2 == 0:
        if i >= 237:
            break
        print(i)
