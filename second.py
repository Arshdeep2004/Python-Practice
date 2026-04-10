#for taking input
# a=input("enter a:")
# print(type(a))   #gives string type 
# b=int(input("enter b :"))
# print(type(b))


#Conditional Statements
# 1. if Statement
# 2. if else Statement
# 3. if elif ladder 
# 4. nested if

#if statement
# age=int(input("Enter your age :"))
# if(age>=18):
#     print("Person can vote")


#if else Statement


#wap to check no. is even or odd--------------------------
# num=int(input("enter num:"))
# if(num%2==0):
#     print("even")
# else:
    # print("odd")
# write a code if person is egligible to vote or not---------------------------
# age=int(input("Enter your age :"))
# if(age>=18):
#     print("Person can vote")
# else:
#     print("Preson cannot able to vote")

#write a code to display witch number is greater---------------------------
# num1=int(input("Enter the first number :"))
# num2=int(input("Enter the second number :"))
# if(num1>num2):
#     print("first number is greater")
# else:
#     print("second number is greater")

#1
#--------------------------------------------------------------
# username=input("Enter your username :")
# password=int(input("Enter your Password :"))
# if(username=="lakshya" and password==1234):
#     print("Access Granted")
# else:
#     print("Access Denied")
  
#2
#----------------------------------------------------------
# age=int(input("Enter your age :"))
# if(age>=18 and age<=70):
#     print("Person Can drive")
# else:
#     print("person cannot drive")

#3
#----------------------------------------------------
# age=int(input("Enter your age :"))
# weight=int(input("Enter your weight :"))
# if(age>18 and weight>50):
#     print("egligible for blood donation")
# else:
#     print("not egligible for blood donation ")

#4
#-----------------------------------------------------------
# account_balance=int(input("Enter your Account Balance :"))
# amount=int(input("enter amount you want to withdraw :"))
# if(amount<account_balance):
#     current_balance=account_balance-amount
#     print(current_balance)
# else:
#   print("insufficient balance")

#5
#--------------------------------------------------------
# temp=int(input("enter temp :"))
# if(temp>=30):
#     print("its hot outside")
# else:
#     print("its cold outside")
  
# if elif  ladder 

# num=int(input("Enter the num:"))
# if(num%2==0):
#     print("Num is divisible by 2")
# elif(num%3==0):
#     print("num is divisible be 3")
# elif(num%4==0):
#     print("num is divisible by 4")
# else:
#     print("num is not divisible by 2,3,4")

# wap to find greater number between 3
# `a=int(input("Enter the a"))
# b=int(input("Enter the b"))
# c=int(input("Enter the c"))
# if(a>b and a>c):
#     print("a is greater")
# elif(b<a and b<c):
#     print("b is greater")
# else:
#     print("c is greater")`

# a=int(input("Enter value of a"))
# b=int(input("Enter value of b"))
# c=input("Enter your operator")
# if(a==10 and b==20 and c=="+"):
#     print("85")
# elif(a==20 and b==5 and c=="-"):
#     print("77")
# elif(a==10 and b==3 and c=="*"):
#     print("88")
# else:
#    if(c=="+"):
#        print(a+b)
#    elif(c=="-"):
#        print(a-b)
#    else:
#        print(a*b)


# #Nested if 

# # num=int(input("Enter the num"))
# # if(num!=0):
# #     if(num>0):
# #         print("positive number")
# #     else:
# #         print("Negitive number")
# # else:
# #     print("number is Zero")


# num=int(input("Enter the num"))
# if(num>=0):
#     if(num%2==0):
#         print("even and positive")
#     else:
#         print("odd and positive")
# else:
#      if(num%2==0):
#         print("even and Negative")
#      else:
#         print("odd and Negative")
            


#1.Question----------------------------------------------------------------------------
# subject1=input("Enter Subject1:")
# subject2=input("Enter Subject2:")
# subject3=input("Enter Subject3:")
# subject4=input("Enter Subject4:")
# subject5=input("Enter Subject5:")
# subject6=input("Enter Subject6:")
# subject7=input("Enter Subject7:")
# marks_subject1=int(input("Enter narks of subject1:"))
# marks_subject2=int(input("Enter narks of subject2:"))
# marks_subject3=int(input("Enter narks of subject3:"))
# marks_subject4=int(input("Enter narks of subject4:"))
# marks_subject5=int(input("Enter narks of subject5:"))
# marks_subject6=int(input("Enter narks of subject6:"))
# marks_subject7=int(input("Enter narks of subject7:"))
# total=marks_subject1+marks_subject2+marks_subject3+marks_subject4+marks_subject5+marks_subject6+marks_subject7
# print("Total Marks:",total)
# percentage=total/7
# print("Percentage :",percentage)
# if(percentage>=80 and percentage<=100):
#     print("Passed with A grade")
# elif(percentage>=60 and percentage<=80):
#     print("passed with B grade")
# elif(percentage>=40 and percentage<=60):
#     print("passed with C grade")
# else:
#     print("FAIL")
#2.question-----------------------------------------------------------------------------
# num=int(input("Enter your num:"))
# if(num%3==0):
#  if(num%5==0):
#     print("number is divisible by 3 and 5")
#  else:
#    print("number is not divisible by 3 and 5")
# else:
#   print("number is divisible by 3 only")   

#3.Question---------------------------------------------------------------------------
# direction=input("Enter direction :")
# if(direction=="left"):
#     print("You find something Good :")
# elif(direction=="right"):
#     print("Thier is nothing in right direction")
# else:
#     print("You are not writting correct name of direction ")
#4.Question----------------------------------------------------------------------------------
# amount=int(input("Enter amount:"))
# if(amount>=15000):
#     discount=amount*20/100
#     print("you will be given 20% of discount i.e of about :",discount)
# elif(amount>=10000):
#     discount=amount*15/100
#     print("you will be given 15% of discount i.e of about :",discount)
# else:
#     print("No discounts uder this amount")
#5.Question--------------------------------------------------------------------------
# temp=int(input("Enter temperature :"))
# if(temp<0):
#     print("Wear heavy coat and golves")
# elif(temp<0 and temp<10):
#     print("coat and sweater should be enought")
# elif(temp<10 and temp<20):
#     print("wearing a jacket is enough")
# elif(temp<20 and temp<30):
#     print("wera tshirt")
# elif(temp<30 and temp<40):
#     print("wear shorts")
# else:
#     print("wear cotton shorts")
#6.gretaest between 5 no.s--------------------------------------------------------
# a=int(input("Enter a:"))
# b=int(input("Enter b:"))
# c=int(input("Enter c:"))
# d=int(input("Enter d:"))
# e=int(input("Enter e:"))
# if(a>b and a>c and a>d and a>e):
#     print("a is greater")
# elif(b>a and b>c and b>d and b>e):
#     print("b is greater")
# elif(c>a and c>b and c>d and c>e):
#     print("c is greater")
# elif(d>a and d>b and d>c and d>e):
#     print("d is greater")
# else:
#     print("e is greater")

#Control Statement----------------------------------------------------------------------------
#1.While loop
#2.For loop

#1.while loop
#write a program to display 1-100 natural numbers
# i=1
# while(i<=100):
#  print(i)
#  i+=1

#wap to display table of input no.
# n=int(input("Enter the number:"))
# i=1
# while(i<=10):
#     print(n ,"*",i,"=",n*i)
#     i+=1

#wap to display 1-20 even numbers
# i=2
# while(i<=20):
#  print(i)
#  i+=2
#wap to display 1-20 odd numbers
# i=1
# while(i<=20):
#  print(i)
#  i+=2

#wap to find the sum of frst 1-10 numbers 
# sum=0
# i=1
# while(i<=10):
#     sum=sum+i
#     print(sum)
#     i+=1


#1000-25000 display no. which is divisible by 2 and 5 
# i=1000
# while(i<=2500):
#     if(i%2==0 and i%5==0):
#         print(i)
#     i+=1


# WAP to find the factorial of num input by the user 
# n=5
# fact=1
# i=1
# while(i<=5):
#     fact=fact*i
#     i+=1
#     print(fact)



#Match Case statement
#in this we use match key word
#1.--------------------------------------------------------------------
# year=int(input("Enter your year:"))
# match(year):
#     case 1:
#         print("The year is 2001")
#     case 2:
#         print("the year is 2002")
#     case 3:
#         print("the year is 2003")
#     case _:
#         print("Invalid")
#2.---------------------------------------------------------------------------
# num=int(input("enter num"))
# match(num):
#     case 1:
#         print("Addition")
#     case 2:
#         print("Substraction")
#     case 3:
#         print("multiplication")
#     case _: 
#         print("Invalid")       
        



