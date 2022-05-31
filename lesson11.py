#! /user/bin/python

#########################################################
#                  loops:for and while
#                  Name: Laura Rege
#                  Date: 25/5/22
#########################################################

#print(range(0,20))
for numbers in range(0,10):
    print(numbers)
for numbers in range(0,10):
    if(numbers%2==0):
      print(numbers)

#Sum of all odd numbers between (0,50)
#Sum of all even numbers between (0,50)

sum_nums = 0
prod_nums = 1
#sum of even numbers between (0,50)
for numbers in range(0,50):
    if(numbers %2 == 0):
       sum_nums = sum_nums + numbers
print(sum_nums)       
#sum of odd number between (0,50)
for numbers in range(1,50):
    if(numbers %2 == 1):
       sum_nums = sum_nums + numbers
print(sum_nums)

for numbers in range(0,20):
     if(numbers %2 == 1):
        prod_nums = prod_nums + numbers
print(prod_nums)

#factorial of six and factorial of nine
#factorial is the number times the number -1 

#while loops
num = 0
while num < 10 :
      print(num)
      num = num + 1
if(num %2 == 0):
   print(num)