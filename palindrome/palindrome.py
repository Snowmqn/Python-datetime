"""
Write an efficient function has_palindrome that checks whether any permutation of an input string is a palindrome.

Examples:

has_palindrome('civic') should return True
has_palindrome('ivicc') should return True
has_palindrome('civil') should return False
Note, there is an O(n) solution to this problem.

Bonuses:
For bonus points, write a function that can read the text from a file.
"""



import os

#Takes in a string and outputs True or False.
#Will output True is there is a permutation of the
#string that is a palindrome.
def has_palindrome(arg):
    test = ""

    #Check if arg is a file and read if so. 
    if os.path.isfile(arg):
        with open(arg, "r") as temp_file:
            arg = temp_file.read()

    #Verify arg is string
    if type(arg) != str:
        return False

    #Remove spaces from arg and make it lowercase.
    #Keep track of pairs or letters by removing them from test.
    for char in arg.replace(" ", "").lower():
        if char in test:
            test = test.replace(char, "")
        else:
            test = test + char

    #Once all paired letters are removed then if one or less letters remain
    #there exists a palindrome in arg.
    if len(test) < 2:
        return True
    else:
        return False


