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

