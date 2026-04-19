
# for loop
# for i in range(1,101):
#     print(i)
# for i in range(1,101):
#     print(i,end=" ")
# for i in range(1,101,2):
#     print(i,end=" ")

# for i in range(1,51):
#     if(i==25):
#         break
#     print(i,end=" ")
# for i in range(1,51):
#     if(i<=25):
#         continue
#     print(i,end=" ")
# for i in range(1,51):
#     if(i<=25):
#         pass
#     print(i,end=" ")


# import calendar
 # print(calendar.calendar(2004))
# print(calendar.month(2004,4))

# import math
# print(math.sqrt(49))
# print(math.pi)
# print(math.factorial(5))
# print(math.ceil(math.sqrt(36)))

# import random
# print(random.Random())
# print(random.randint(1,100))
# print(random.randrange(1,10))


# import random
# num=random.randint(1,100)
# guess=1
# while(guess<=9):
#       a=int(input("Enter your num:"))

#       if(a>num):
#         print("You entered greater no. pls add smaller no.",)
#       elif(a<num):
#         print("You entered smallest no. pls add greater no.")
#       else:
#         print("YOU WON and completed this in",guess,"guesses")
#         break
#       print(9-guess,"guesses left ")
#       guess+=1
# if(guess>9):
#    print("Game Over")


#even no. using for loop 
# for i in range(2,11,2):
#     print(i,end=" ")
#odd no. using for loop
# for i in range(1,10,2):
#     print(i,end=" ")
#print no. form -10 to -1
# for i in range(-10,0):
#     print(i)

# Write a program to display a message “Done” after the successful execution of a for loop that iterates from 0 to 4.
# for i in range(0,5):
#     print(i)
# else:
#     print("Done !")


#4. Calculate the sum of all numbers from 1 to N
# N=int(input("Enter your num: "))
# sum=0
# for i in range(1,N+1):
#     sum += i
# print(sum)

#5. Print multiplication table of a given number
# N=int(input("Enter your num: "))
# for i in range(1,N+1):
#     print(N,"X",i,"=",N*i)

#6. Calculate the cube of all numbers from 1 to a given number
# N=int(input("Enter your num: "))
# for i in range(1,N+1):
#     print("Current Number is :", i,"and the cube is",i**3)

#Factorial of number 
# n=int(input("Enter your num: "))
# fact=1
# if(n<0):
#     print("Factorial of -ve no. does not exist")
# elif(n==0):
#     print("Factorial of 0 is 1")
# else:
#     for i in range (1,n+1):
#         fact=fact*i
# print("factorial of",n,"is",fact)