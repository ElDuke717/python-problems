import string

"""
Create a function that checks if a word or phrase is a palindrome 
(reads the same backward and forward). 
Ignore spaces, punctuation, and case sensitivity.
"""

# Declare isPalindromeString takes one arg str a string
# Declare variable s, assigned the value of str with spaces and 
# punctuation removed, all lower case.
# compare s against s reversed, return true if they are the same
# 

def isPalindromeString(str):
    s = str.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    return s == reversed(s)

print(isPalindromeString("Reza and Arya are a pain in the ass."))