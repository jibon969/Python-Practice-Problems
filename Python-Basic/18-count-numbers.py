# x = [1, 3, 4, 4, 5]
# y = x.count(4)
# print(y)

# using for loop

nums = [1, 3, 4, 4, 5]
count = 0
for num in nums:
    if num == 4:
        count = count + 1

print(count)
