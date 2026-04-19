#BASIC LOOP QUESTIONS
#1. Print numbers from 1 to 10
# for i in range(1,11):
#     print(i)
#2.Print numbers from 10 to 1
# for i in range(10,0,-1):
#     print(i)
#3.Print all even numbers from 1 to 50
# for i in range(2,51,2):
#     print(i)
#4.Print all odd numbers from 1 to 50
# for i in range(1,51,2):
#     print(i)
#5. Print multiplication table of a given number
# N=int(input("Enter your num: "))
# for i in range(1,11):
#          print(N,"X",i,"=",N*i)
#6.Print first N natural numbers
# N=int(input("Enter your num: "))
# for i in range(1,N+1):
#     print(i)
#7.Find sum of first N natural numbers
# N=int(input("Enter your num: "))
# sum=0
# for i in range(1,N+1):
#     sum+=i
# print(sum)
#8.Find sum of even numbers till N
# N=int(input("Enter your num: "))
# sum=0
# for i in range(2,N+1,2):
#     sum+=i
# print(sum)
#9.Find sum of odd numbers till N
# N=int(input("Enter your num: "))
# sum=0
# for i in range(1,N+1,2):
#     sum+=i
# print(sum)
#10.Find sum of odd numbers till N
# N=int(input("Enter your num: "))
# count=0
# for i in range(1,N+1):
#     count+=1
# print(count)


#NUMBER BASED LOOP QUESTION
#11.Reverse a number
# n=123
# rev=0
# for i in range(n):
#     if(n==0):
#         break
#     remainder=n%10
#     rev=rev*10+remainder
#     n=n//10
# print(rev)
#12.Count digits in a number
# n=int(input("Enter n:"))
# count=0
# for i in range(n):
#     if(n==0):
#         break
#     else:
#         n=n//10
#         count=count+1
# print(count)  
# 13. Find sum of digits
# n =int( input("Enter number: "))
# sum=0
# while(n>0):
#     r=n%10
#     sum=sum+r
#     n=n//10
# print(sum)    
#14.Find product of digits
# n =int( input("Enter number: "))
# product=1
# while(n>0):
#     r=n%10
#     product=product*r
#     n=n//10
# print(product)  
#15.Check palindrome number
# n =int( input("Enter number: "))
# reversed=0
# temp=n
# while(n>0):
#     r=n%10
#     reversed=reversed*10+r
#     n=n//10
# if(temp==reversed):
#     print("Palindrom no.")
# else:
#     print("Not palindrom no.")    
#16.Check Armstrong number
# n =int( input("Enter number: "))
# temp=n
# sum=0
# while(temp>0):
#     r=temp%10
#     sum=sum+(r**3)
#     temp=temp//10
# if(sum==n):
#     print("armstrong no.")
# else:
#     print("not an armstrong no.")
#17.Find power of a number (without using operator)
# base = int(input("Enter base: "))
# exp = int(input("Enter exponent: "))
# result=1
# for i in range(exp):
#     result=result*base
# print(result)    
#18.Check if number is prime
# n = int(input("Enter number: "))
# if n <= 1:
#     print("Not a prime number")
# else:
#     for i in range(2, n):
#         if n % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
#19.Print all prime numbers till N
# n = int(input("Enter number: "))
# for num in range(2,n+1):
#     for i in range(2,num):
#         if (num%i==0):
#             break
#     else:
#       print(num,end=" ")
#20.find the factorial of no.
# n = int(input("Enter number: "))
# fact = 1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)