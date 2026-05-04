

riddle=[
    {
    "riddle":"Riddle 1. What has to be broken before you can use it. What am I?",
    "answer":"egg"
    },
    {
    "riddle":"Riddle 2. I am tall i am young, and I'm old what am I?",
    "answer":"candle"
    },
    {
    "riddle":"Riddle 3. what is always in front of you but can't be seen?",
    "answer":"future"
    },
    {
    "riddle":"Riddle 4. what gets wet while drying?",
    "answer":"towel"
    },
    {
    "riddle":"Riddle 5. I have branches, but no fruits, trunck or leaves. what am i",
    "answer":"bank"
    }
]
print(input("Welcome to the Riddle Game!"))
name=(input("Enter your Name:"))
print("Hi",name,"Let's start the challenge!")
score=0
for r in riddle:
  print(r["riddle"])
  answer=input("your answer: ")
  if(answer==r['answer']):
    print("CORRECT")
    score+=1
  else:
    print("INCORRECT") 
print("Game OVER!")
print("Your score:",score,"out of 5")       