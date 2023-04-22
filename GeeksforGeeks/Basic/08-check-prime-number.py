"""
Check Prime Number Using For Loop
"""
num = int(input("Enter your number : "))

for i in range(2, num):
    if num % i == 0:
        print("Not prime Number")
        break
else:
    print("Prime Number")
