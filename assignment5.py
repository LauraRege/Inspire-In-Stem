#! /user/bin/python

#########################################################
#                  assignment on lists
#                  Name: Laura Rege
#                  Date: 25/5/22
#########################################################

#Create a list of vehicles with the following:
#Bmw,Audi,Toyota,Mercedes,Jeep
#Using if statement find a jeep in the list and convert into uppercase

#a list of vehicles
vehicles = ['bmw','audi','toyota','mercedes','jeep']

#using a forloop to print all vehicles
for vehicle in vehicles:
    if (vehicle == "jeep"):
       print(vehicle.upper())

