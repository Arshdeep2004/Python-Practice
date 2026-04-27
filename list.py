#LIST =>list is a type of data structure which is used to storemultiple items in a single
#variable,it is always enclosed under[] and each element is seperated by(,)
#List is mutable means we can changeit once we have declared
#We can access the list items acc. to their index value is always started from 0
# a=[10,2,2.3,"Siya",True]
# print(a)

# for i in a:
#     print(i,end=" ")
# print(a[0])    
# print(a[-1])

# a[0]=85
# print(a)
# a.append(74)
# print(a)
# a.insert(0,8.6)
# print(a)
# a.pop()
# print(a)
# del a[1]
# print(a)
# a.remove("Siya")
# print(a)
# a.clear()
# print(a)

# list1=[10,20,30,40,50]
# list2=[1,2,3,4,5]
# list1.extend(list2)
# print(list1)
# print(sum(list1))
# print(max(list1))
# print(min(list1))
# print(len(list1))
# print(list1.count(74))

# Take 5 numbers in a list and print all elements using a loop
# a=[1,2,3.5,"Arshu",False]
# for i in a:
#     print(i,end=" ")

# Find the sum of all elements in a list (without using sum())
# b=[10,20,30,40,50]
# total=0
# for i in b:
#     total=total+i
# print(total)

# Find the largest element in a list (without max())
# b=[10,20,30,40,50]
# largest=b[0]
# for i in b:
#     if i>largest:
#         largest=i
# print("largest= ",largest)        

# Count how many even and odd numbers are in a list
# b=[10,20,31,40,51]
# for i in b:
#     if(i%2==0):
#         print(i)
# b=[10,20,31,40,51]
# for i in b:
#     if(i%2!=0):
#         print(i)
# Create a list and remove all duplicate elements
# a=[1,2,2,3,4,3,5]
# unique=[]
# for i in a:
#     if i not in unique:
#         unique.append(i)
# print(unique)        
# Find the second largest number in a list
# a = [10, 20, 5, 80, 30]
# largest=a[0]
# second=a[0]
# for i in a:
#     if i>largest:
#         largest=i
# for i in a:
#     if i!=largest and i>second:
#         second=i
# print("second largest=",second)                

# Check if a number exists in the list or not (without in)
# a = [10, 20, 30, 40, 50]
# num=50
# found =False
# index=0
# for i in a:
#     if i==num:
#         found=True
#         break
#     index+=1
# if found:
#     print("Number found at index",index)
# else:
#     print("Number not found")    



# ele=int(input("Enter no. of Elements:"))
# list=[]
# for i in range(1,ele+1):
#   a=int(input(f"Enter {i} number :"))
#   list.append(a)
# print(list)


# name="siya"
# age=85
# print("The name is",name)
# print(f"the name is {name} and the age is {age}")

#sum of all even no. in the list 
# b=[10,20,31,40,51]
# sum=0
# for i in b:
#     if(i%2==0):
#         sum=sum+i
# print("sum of all even no. in this list:",sum)

#armstrong no . or not
# list=[153,248,567,345]
# for i in list:
#     total=0
#     temp=i
#     while temp>0:
#         r=temp%10
#         total=total+r**3
#         temp=temp//10
#     if(total==i):
#         print(i,"is an armstrong no.")
#     else:
#         print(i,"is not an armstrong no.") 


# print("STUDENT MANAGEMENT SYSTEM")
# student=[]
# while(True):
#     print("1.ADD STUDENTS")
#     print("2.UPDATE STUDENTS")
#     print("3.DELETE STUDENTS")
#     print("4.EXIT")
#     choice=int(input("Enter your choice:"))
#     if(choice==1):
#         print("ok! you wannt to add students")
#         std=int(input("Enter no. of students you want to add:"))
#         for i in range(1,std+1):
#             a=str(input(f"Enter {i} student name :"))
#             student.append(a)
#         print(student)
#     elif(choice==2):
#         print("ok! you wannt to update students")
#         std=int(input("Enter no. of students you want to update:"))
#         for i in range(1,std+1):
#             ind=0
#             ind=int(input(f"Eneter index where you want to insert student {i}:"))
#             a=str(input(f"Enter {i} student name :"))
#             student.insert(ind,a)
#         print(student)
#     elif(choice==3):
#         print("ok! you wannt to delete students")
#         num=int(input("Enter no. of students you want to delete:"))
#         for i in range(1,num+1):
#             a=str(input(f"Enter {i} student name :"))
#             student.remove(a)
#         print(student)
#     elif(choice==4):
#         print("EXIT!!")
#         break
#     else:
#         print("INVALID CHOICE")



        
     


