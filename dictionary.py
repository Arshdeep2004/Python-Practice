# person={
#     "name":"arshu",
#     "age":22,
#     "email":"arshdeepkaur@gmail.com"
# }
# for keys,values in person.items():
#     print(keys,":",values)

#printing dictionary----------------------
# print(person)
#Updating data------------------------------
# print(person["age"])
# person["age"]=21
# print(person)
#Adding new data--------------------------------
# person["gender"]="Female"
# print(person)
#deleting data--------------------------------
# del person["email"]
# print(person)


# print(len(person))
# print(person.keys())
# print(person.values())
# print(person.items())

# menu={
#     "Fries":160,
#     "Pizza":500,
#     "Pasta":150,
#     "Tea":50
# }
# for keys,values in menu.items():
#     print(keys,":",values)
# total=0
# while (True):
#     order=(input("Do you want to order Something(yes/no):"))
#     if(order=="yes"):
#         food_item=(input("Which food item do you want to add: "))
#         if(food_item in menu):
            
#             total+=menu[food_item]
            
#         else:
#           print("This food item is not available")
           
#     else:
#       print("OK!!Thankyou for visiting")
#       break
#     # else:
#     #     print("SORRY!!,you entered wrong info")

# print("Total price of food items:",total)
       
