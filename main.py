#/user/bin/python

#########################################################
#                  file :operations.py
#                  Name : Laura Rege
#                  Date : 6/6/22
#########################################################



import operations
from student import student
from teachers import Teachers

print(operations.add_numbers(3,5))

print(operations.sub_numbers(7,2))

print(operations.mult_numbers(4,5))

print(operations.div_numbers(700,20))

new_student = student("Laura",)

new_teacher = Teachers("Mr Ngugi","11763","Matha","80000")

print(new_teacher.get_tsc_no)



