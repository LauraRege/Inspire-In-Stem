#! /user/bin/python

#########################################################
#                  
#                  Name: Laura Rege
#                  palindromes
#                  Date: 8/6/22
#########################################################

#Check if a number or a letter is a palindrome
#Ask user to select which input number or letter

#palindrome = input("Select which input to check number or letter?")

def check_palindrome(v):
    if len(v) < 1:
        return True
    else:
        if v[0] == v[-1]:
            return check_palindrome(v[1:-1])
        else:
            return False
var = input(("Enter a value: "))
if(check_palindrome(var)):
    print("The input is a palindrome")
else:
    print("The input is not a palindrome")

