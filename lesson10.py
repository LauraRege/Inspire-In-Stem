er/bin/python#! /us

#########################################################
#                  Dictionaries
#                  Name: Laura Rege
#                  Date: 24/5/22
#########################################################

#A dictionary is a collection of key value pairs
#syntax : dictionary = ['key' : 'value']
#list names = {'john','Mary'}
colors = ['red','green','blue','purple']
i = 1 
while i < len(colors):
      if(colors[1]=='green'):
        print(colors[1].upper())
        i += 1

i = 2
while i < len(colors):
     if(colors[2]=='blue'):
        print(colors[2].upper())
        i += 1

i = 3
while i < len(colors):
      if(colors[3]=='purple'):
        print(colors[3].upper)
        i += 1
        
vehicle = {'type':'toyota','plate number':'ABCD'}
#print(type(names)) #we use the type method to read datatypes
#accessing values in a dictionary
#print(vehicle['type']) #You can acces the value of an element inside a dictionary using the key
person = {'name':'Laura'}
person['age']='18'
person['favfood']='ugali'
id_number = {'number':'20774796'}
gender = {'gend':'female'}
phone_number = {'number':'0741724577'}
print(person['name'], ['number'],gender['gend'], phone_number['number'])

print(person.get["'password','the','location' key is non-existent"])
#using get to access a value in the dictionary


mary_fav_food = ['beef','chicken','vegetable']
jane_fav_food= ['rice','ugali','potatoes']

person = {
        'mary':['fav_food':'beef']
}