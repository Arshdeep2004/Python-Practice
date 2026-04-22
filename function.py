#Function-> is ablock of code which runs only when it is call It is used for performing repetitive task
#Types of Function 
#1.user defined func.(def)
#2.Library function or buit in function
#3.Anonymous func.(lambda)

# def first():
#     print("This is my first function")
# first()

#4. Based on Argument and return value
# a. NO argument,Noreturn value
# def first():
#     print("Hello")
# first()
# b. Argument,No return value
# def first(name):
#     print("Hello",name)
# first("Arshdeep")
# c. Return value,No argument
# def first():
#     return "arshdeep"
# print(first())
# d.argument with return value 
# def sum(x,y):
#     return(x+y)
# print(sum(10,20))


#Rock paper scissor Game---------------------------------------------------------------------------------------------------------------------------------------------
# import random
# def game():
#     print("Rock paper scissor Game")
#     print("1.Rock")
#     print("2.paper")
#     print("3.Scissor")
#     Choice_user=int(input("Enter your choice: "))
#     Choice_machine=random.randint(1,3)
#     print("Option choosed by machine is:",end=" ")
#     if(Choice_machine==1):
#         print("Rock")
#     elif(Choice_machine==2):
#         print("paper")
#     else:
#         print("Scissior")
#     if(Choice_user==1 and Choice_machine==3):
#         print("User won")   
#     elif(Choice_user==2 and Choice_machine==1):
#         print("user Won")
#     elif(Choice_user==3 and Choice_machine==2):
#         print("user Won")
#     elif(Choice_user==Choice_machine):
#         print("Draw")
#     else:
#         print("Machine won")
#     again=input("Do you want to play again: ")
#     if(again=="y" or again=="Y" or again=="yes" or again=="YES"):
#         game()
#     else:
#         print("Thank You")
# game() 
#Snake Water Gun Game---------------------------------------------------------------------------------------------------------------------------------------------------
#snake-water->snake
#water-gun->water
#gun-snake->gun
# import random
# def game():
#     print("Snake Water Gun Game")
#     print("1.Snake")
#     print("2.Water")
#     print("3.Gun")
#     Choice_user=int(input("Enter your choice: "))
#     Choice_machine=random.randint(1,3)
#     print("Option choosed by machine is:",end=" ")
#     if(Choice_machine==1):
#         print("Snake")
#     elif(Choice_machine==2):
#         print("Water")
#     else:
#         print("Gun")
#     if(Choice_user==3 and Choice_machine==1):
#         print("User won")   
#     elif(Choice_user==1 and Choice_machine==2):
#         print("user Won")
#     elif(Choice_user==2 and Choice_machine==3):
#         print("user Won")
#     elif(Choice_user==Choice_machine):
#         print("Draw")
#     else:
#         print("Machine won")
#     again=input("Do you want to play again: ")
#     if(again=="y" or again=="Y" or again=="yes" or again=="YES"):
#         game()
#     else:
#         print("Thank You")
# game()        
#Random No. game--------------------------------------------------------------------------------------------------------------------------------------------------
# import random
# def randomnumber():
#     return(random.randint(1,6))
# randomnumber()
# def game():
#     player1=0
#     player2=0
#     winning_score=30
#     while(True):
#         input("Press enter for Player 1 turns ")
#         roll=randomnumber()
#         player1+=roll
#         print("Player1 Score is: ",player1,"having roll",roll)
#         if(player1>=winning_score):
#             print("Player1 wins!")
#             break
#         input("Press enter for Player 2 turns ")
#         roll=randomnumber()
#         player2+=roll
#         print("Player2 Score is: ",player2,"having roll",roll)
#         if(player2>=winning_score):
#             print("Player2 wins!")
#             break
#         print("-"*30)
# game()        



#Practice Question for Functions
#1.Write a function that takes a number and returns whether it is prime or not.
# def is_prime(n):
#     if n<= 1:
#         return False
#     for i in range(2,n):
#         if n%i ==0:
#             return False
#     else:
#         return True
# num=int(input("Enter yoyr num: "))
# result=is_prime
# if(result):
#     print("prime no.")
# else:
#     print("Not a prime no.")       
#2.Write a function to count even and odd numbers from 1 to n.
# def count_even(n):
#     count=0
#     for i in range(2,n+1,2):
#             count=count+i
#     return count
# n=int(input("Enter no.till you want to calculate sum of even numbers: "))
# result=count_even(n)
# print("Total Even No.s: ",result)
# def count_odd(n):
#     count=0
#     for i in range(1,n+1,2):
#             count=count+i
#     return count
# n=int(input("Enter no.till you want to calculate sum of odd numbers: "))
# result=count_odd(n)
# print("Total odd No.s: ",result)
#3.Write a function to find the square of a number.
# def Square(n):
#     return n**2
# n=int(input("Enter your no."))
# result=Square(n)
# print("Square=",result)
#4.Write a function to reverse a number and check if it is palindrome
# def reverse_number(n):
#         rev=0 
#         temp=n
#         while(temp>0):
#             r=temp%10
#             rev=rev*10+r
#             temp=temp//10
#         return rev
# def is_palindrom(n):
#         return n ==reverse_number(n)

#     num=int(input("Enter the no.: "))



    