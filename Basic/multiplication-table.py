# Example how to print multiplication table নামতা প্রিন্ট করবো ।

userInput = int(input("Multiplication Enter your number : "))
n = 1
while n <= 10:
    print(userInput, '*', n, '=', userInput * n)
    n += 1

print('\n')


for i in range(1, 10):
    print(i, '*', 3, i*3)