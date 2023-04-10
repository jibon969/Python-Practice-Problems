"""
Let us discuss the formula for compound interest. The formula to calculate compound interest annually is given by:

A = P(1 + R/100) t

Compound Interest = A – P

Where,
A is amount
P is the principal amount
R is the rate and
T is the time span
"""

"""
Input: Principal (amount): 1200, Time: 2, Rate: 5.4
Output: Compound Interest = 133.099243
"""

principal_amount = 1200
time = 2
rate = 5.4

compound_interest = principal_amount*(1+rate/100)**time
print(compound_interest)


# Using Function
def compound_interest(principal_amount, rate, time):
    return principal_amount*(1+rate/100)**time


result = compound_interest(1200, 5.4, 2)
print(result)
