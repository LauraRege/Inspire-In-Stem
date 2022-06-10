#! /user/bin/python

#########################################################
#                  scarping
#                  Name: Laura Rege
#                  Date: 10/6/22
#########################################################

import requests
from bs4 import BeautifulSoup as bs
user_name = "LauraRege" #Ask for the input of the user input("Enter your username")
url = "https://github.com/" + user_name #input("Enter cite url")
results = requests.get(url)

soup = bs(results.content, "html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})
print(profile_pic)