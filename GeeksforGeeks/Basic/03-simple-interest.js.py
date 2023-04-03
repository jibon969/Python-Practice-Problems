"""
Simple Interest = (P x T x R)/100 Where, P is the principal amount T is the time and R is the rate
Input : P = 10000
        R = 5
        T = 5
Output :2500.0
"""

P = 10000
R = 5
T = 5

result = (P*R*T)/100
print(result)


def simple_interest(p, r, t):

    interest = (p*r*t)/100
    return interest


output = simple_interest(8, 6, 8)
print("The Simple Interest is ", output)
