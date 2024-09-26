"""
Write a Python program to test whether a passed letter is a vowel or not.
"""
"""
vowel = [A, E, I, O, U]
search : C
"""

def check_vowel_or_not(char):
    
    all_vowel = ["aeiou"]
    for i in all_vowel:
        return char in i

result = check_vowel_or_not('e')
print(result)
