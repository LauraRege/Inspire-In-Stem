#! /user/bin/python

#########################################################
#                  
#                  Name: Laura Rege
#                  gui_examples using tkinter
#                  Date: 7/6/22
#########################################################

from tkinter import *

window = Tk()
window.title("Welcome to my awesome App")
window.configure(bg = 'red')
window.geometry("400x400")#fix the size
f_name = Label(window, text="First Name", font=("Arial", 20))
s_name = Label(window, text="Second Name", font=("Arial", 20))

f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row = 120)

def open_popup():

    btn = Button(window, text= "Click here", bg= 'blue', fg= 'green',command= open_popup().pack())
    btn.grid(column = 100 ,row = 180)

f_name_box = Entry(window ,width=10)
f_name_box.grid(column = 100 , row = 100)

s_name_box = Entry(window ,width=10 )
s_name_box.grid(column = 100 , row = 120)

top = Toplevel(window)
top.geometry("300x300")
top.title("Pop Up Window")
top.config(bg= 'green')
msg= Label(top,text= "Welcome to the pop up",font=("Mistral", 18))

window.mainloop()
