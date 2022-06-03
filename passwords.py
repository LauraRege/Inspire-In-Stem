#/user/bin/python

#########################################################
#                  lesson on passwords
#                  Name : Laura Rege
#                  Date : 3/6/22
#########################################################

#import random
print('Welcome to our password generator')
#ask user number of passwords they wan to generate
#convert the number of passwords into integers
#ask user for password length

import random
num_password = int(input("What is the number of passwords you want to generate?"))
print(num_password)
len_password = int(input("What is the length of your password?"))
print(len_password)
character = "Laura Rege"

#print here are your passwords

for passwords in range (num_password):
    passwords = ""
for c in range(len_password): 
    passwords += random.choice(character)
print(passwords)

#assignment store user and their password