#! /user/bin/python

#########################################################
#                  assignment on if statements
#                  Name: Laura Rege
#                  Date: 24/5/22
#########################################################


#Write a programme to withdraw kshs 25000 if the account balance is between kshs 100000-200000
#30% if account balance is between 500000-1000000
#Above 1000000 deduct 700000

name = "Laura"
account_balance = ("What is your account balance?")
account_balance = 167000
if (int(account_balance) > 100000 and int(account_balance) < 200000):
    account_balance = account_balance - 25000
    print("We have deducted 25000 from your account")
else: 
    ("int(account_balance) > 500000 and int(account_balance) < 1000000")
    account_balance = account_balance - (0.3*account_balance)
    print("We have deducted 30 percent from your account")
if (int(account_balance) > 1000000):
    account_balance = account_balance- 700000
    print("We have deducted 700000 from your account")