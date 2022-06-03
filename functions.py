#! /user/bin/python

#########################################################
#                  Quadratic Equations
#                  Name: Laura Rege
#                  Date: 31/5/22
#########################################################

#import math

#a = int(input("Enter the coefficient of first term"))
#b = int(input("Enter the coefficient of the second term"))
#c = int(input("Ener the constant"))
#w = math.sqrt((b**2) - 4*a*c) 

#y_1 = (-b + w) / (2*a)
#y_2 = (-b - w) / (2*a)

#print("The roots of the quadratic equation are :",y_1, y_2)

#Blocks of code that execute together
#Use the key word def
#function definition
#def sum(a,b)-parameters:
#sum_numbs = a+b


#Using default parameters
def print_name( name = "Laura Rege"):
    print(name)
print()
print_name("Joseph")

#Return from a function
def get_sum(numb1,numb2):
    sum_numbs = numb1 + numb2
    return sum_numbs
print(get_sum(7,12))

#square of numbers
def powers(number,power):
    pow_numb = number**power
    return pow_numb
print(powers(6,4))

def  get_full_name(f_name,s_name):
    full_name = f_name +" "+ s_name
    return full_name.title()
print(get_full_name("Laura","Rege"))

#Returning a dictionary from a function
def create_full_name(first_name,second_name):
    person = {'fisrt':first_name,'second':second_name}
    return person
student = create_full_name('Laura','Rege')
print(student)

#Passing a list in a function:
def greet_friends(names):
    for name in names:
        msg = "Hello"+ " " + name.title() + "!"
        print(msg)
#Creating a list of friends
friends = ['Monicah','Naneu','Serena']
greet_friends(friends)
print(greet_friends)

