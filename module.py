#A module is simply a file continuing python code
#1. Built in module- math,randon,calender,time
#2.External module- need installation (pip install)
#3. user defined modules- for eg our own files module.py,first.py,second.py

# import time
# while True:
#     print("Hello")
#     time.sleep(2)
#     print("Hii")
#     time.sleep(1)


# import phonenumbers
# from phonenumbers import geocoder
# a=phonenumbers.parse("+911415161578")
# print(geocoder.description_for_number(a,"en"))

# import phonenumbers                                                          
# number = phonenumbers.parse("+919876543210")
# print(number)

# import calendar
 # print(calendar.calendar(2004))
# print(calendar.month(2004,4))

# import math
# print(math.sqrt(49))
# print(math.pi)
# print(math.factorial(5))
# print(math.ceil(math.sqrt(36)))

# import random
# print(random.random())
# print(random.randint(1,100))
# print(random.randrange(1,10))


#re module=>stnds for regular expressions It is used for searchin,matching,and manipulating text
# import re
# #creating function 
# def check_password_strength():
#      while(True):    
#         password=input("Enter your password:")
#         if len(password)<8:
#             print("Password too short! be atleast 8 characters.")
#         elif not re.search("[a-z]",password):
#             print("password should contain atleast one lowercase letter.")
#         elif not re.search("[A-Z]",password):
#             print("password should contain atleast one uppercase letter.")
#         elif not re.search("[0-9]",password):
#             print("password should contain atleast one digit.")
#         elif not re.search("[!@#$%^&*(),.?\":{}|<>]",password):
#             print("password should contain atleast one special character.")
#         else:
#             print("Your password is strong")
#             break
# check_password_strength()   #call the function 



