#! /user/bin/python

#########################################################
#                  Quadratic Equations
#                  Name: Laura Rege
#                  Date: 31/5/22
#########################################################

import math

a = int(input("Enter the coefficient of first term"))
b = int(input("Enter the coefficient of the second term"))
c = int(input("Ener the constant"))
w = math.sqrt((b**2) - 4*a*c) 

y_1 = (-b + w) / (2*a)
y_2 = (-b - w) / (2*a)

print("The roots of the quadratic equation are :",y_1, y_2)
