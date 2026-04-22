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

                                              
#Match Case Statement

#in this we use match key word
#--------------------------------------------------------------------
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
#---------------------------------------------------------------------------
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

# Some practice Questions------------------------------------------------------------      
#3. ATM Machine
# balance=20000
# while True:
#     print("1. Check Balance")
#     print("2. Withdraw Cash")
#     print("3. Deposit Cash")
#     print("4. Exit")
#     choice=int(input("Enter your choice :"))
#     match(choice):
#         case 1:
#             print("The Total balance is =", balance )
#         case 2:
#             amount=int(input("Enter the amount to withdraw :"))
#             if(amount<balance):
#                 balance-=amount
#                 print("Balance After withdrawing :",balance)
#             else:
#                 print("Insuficient balance")
#         case 3:
#             amount=int(input("Enter the amount to deposit :"))
#             balance+=amount
#             print("Balance after depositing amount :",balance)
#         case 4:
#             print("Thanyou for using the ATM")
#             break
#         case _:
#             print("Invalid Choice!")    

#4.wap to make Area Calculator------------------------------------------------------
# pie=3.14
# while True:
#     print("1. Area of Circle")
#     print("2. Area of rectangle")
#     print("3. Area of Square")
#     print("4. Exit")
#     choice=int(input("Enter your Choice: "))
#     match(choice):
#         case 1:
#             radius=int(input("Enter value of r: "))
#             print("Area of circle:", pie*radius**2)
#         case 2:
#             Length=int(input("Enter Length :"))
#             Breadth=int(input("Enter Breadth :"))
#             print("Area of rectangle: ",Length*Breadth)  
#         case 3:
#             Side=int(input("Enter Side: "))
#             print("Area of Square",Side**2)    
#         case 4:
#             print("EXIT")
#         break
#         case _:
#             print("INVALID choice !")         


#5.wap to make calculator-----------------------------------------------------
# while True:
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Division")
#     print("3. Multiplication")
#     print("4. Divide")
#     print("5. Exit")
#     choice=int(input("Enter your Choice: "))
#     match(choice):
#         case 1:
#             a=int(input("Enter value of a: "))
#             b=int(input("Enter value of b: "))
#             print("Addition:", a+b)
#         case 2:
#             a=int(input("Enter value of a: "))
#             b=int(input("Enter value of b: "))
#             print("Substraction: ", a-b)  
#         case 3:
#             a=int(input("Enter value of a: "))
#             b=int(input("Enter value of b: "))
#             print("Multiplication",a*b)   
#         case 4:
#             a=int(input("Enter value of a: "))
#             b=int(input("Enter value of b: "))
#             if(b==0):
#                 print("denominator cannot be zero, Please enter another Value of b")
#             else:
#                 print("divide:", a/b)
#         case 5:
#             print("EXIT")
#         case _:
#             print("INVALID choice !") 


#6.WAP to find the cube of 1-10 natural no.
# i=1
# while(i<=10):
#     print("Cube of i :",i**3)
#     i+=1
#7.WAP to find the sum of all even no. form 1-20
# sum=0
# i=2
# while(i<=20):
#  sum=sum+i
#  print(sum)
#  i+=2
#8.WAP to find the sum of all odd no. form 1-20
# sum=0
# i=1
# while(i<=20):
#  sum=sum+i
#  print(sum)
#  i+=2
#9. WAP to reverse a number 
# n=int(input("Enter the value of n:"))
# m=0
# while(n>0):
#     p=n%10
#     m=(m*10)+p
#     n=n//10
# print(m)
#10.WAP to add all the digit of number
# n=123
# sum=0
# while(n>0):
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)    
#11.WAP to find no of digit in a number 
# n=int(input("Enter your number :"))
# count=0

# while(n>0):
#     n=n//10
#     count=count+1
# print(count)   
#12. WAP to check no. is palindrom or not 
# n=int(input("Enter your number :"))
# reversed=0
# temp=n
# while(temp!=0):
#     r=temp%10
#     reversed=(reversed*10)+r
#     temp=temp//10
# if(reversed==n):
#         print(" palindrom number")
# else:
#     print("not a palindrom no.")
# 13.wap to check no. is amstrong or not 
# n=int(input("Enter your num :"))
# temp=n
# sum=0
# while(temp >0):
#     r=temp%10
#     sum=sum+(r**3)
#     temp//=10

# if(sum == n):
#         print("Armstrong Number")
# else:
#         print("Not an armstrong number ")

