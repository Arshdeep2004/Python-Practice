# set1={"apple","banana","cherry",True,1,2}
# print(set1)
# set2={"apple","banana","cherry",False,0,True,2}
# print(set2)
# print(len(set2))
# set3=set(("apple","banana","cherry"))
# print(set3)

# #add element in set
# set4={"apple","banana","cherry"}
# set4.add("orange")
# print(set4)      
#
# fruit1={"apple","banana","cherry"}
# fruit2={"avacado","Papaya","chicku"}
# fruit2.update(fruit1)
# print(fruit2)

# fruits={"apple","banana","cherry"}
# fruits.remove("banana")
# print(fruits)
# fruits={"apple","banana","cherry"}
# fruits.discard("banana")
# print(fruits)

# a={10,20,30}
# print(a)
# print(len(a))
# print(type(a))

# for i in a:
#     print(i)



# print(input("Welcome to the Python Quiz!"))
# question1=[
#     {
#     "question":"Q1. What is the capital of India?",
#     "Options":["A. Delhi","B. Mumbai", "C. Kolkata", "D. Chennai"],
#     "answer":"A"
#     },
#     {
#     "question":"Q2. What data type is immutable in python?",
#     "Options":["A. List","B. Set", "C. Dictionary", "D. Tuple"],
#     "answer":"D"
#     },
#     {
#     "question":"Q3. What is the result of 3 ** 2 in Python",
#     "Options":["A. 5","B. 6", "C. 9", "D. 8"],
#     "answer":"C"
#     },
#     {
#     "question":"Q4. Which symbol is used for comments in Python?",
#     "Options":["A. //","B. #", "C. --", "D. /**/"],
#     "answer":"B"
#     },
#     {
#     "question":"Q5. Which keyword is used for decision making?",
#     "Options":["A. loop","B. if", "C. check", "D. decide"],
#     "answer":"B"
#     }
# ]
# score=0
# for q in question1:
#     print(q["question"])
#     for opt in q["Options"]:
#         print(opt)
#     answer=input("Your answer (A/B/C/D): ").upper()
#     if(answer==q["answer"]):
#         print("CORRECT!")
#         score+=1
#     else:
#         print("INCORRECT")
# print("Quiz Completed!")
# print("Your Final Score:", score,"out of 5")
# print("Good Job!")
     
        
