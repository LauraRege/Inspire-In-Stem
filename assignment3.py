#Write a programme that gets user input and adds ksh 10000 to her account if she is between 25-30 years

age = input("What is your age?")

account_balance = 0
 
if (int(age) > 25) and (int(age) < 30):
    account_balance = account_balance + 10000
    print ("Confirmed you have received 10000")
else:
    print("Sorry no money for you")
