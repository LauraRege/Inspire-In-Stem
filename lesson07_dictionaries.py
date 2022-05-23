#/user/bin/python

#########################################################
#                  Dictionaries
#                  Name: Laura Rege
#                  Date: 23/5/22
#########################################################

# Initializing dictionaries
student = {"Name":"Laura","age":"18","gender":"female"}
print(student["Name"])
print(student["age"])
print(student["gender"])

#adding key values pair to dictionaries

student["ID.No"] = "20774796"
student["hobby"] = "swimming"
student["club"] = "manunited"
print(student)

#starting empty dictionaries

student = {}
#Add pairs

student["favorite_food"] = "chapati"
student['home_city'] = "Nairobi"
print(student)

#modifying values
student["Name"] = "Rege"
print(student)
del student["favorite_food"]
print(student)