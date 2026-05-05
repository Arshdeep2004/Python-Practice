#file Handling File handling = working with files (create, read, write, update)
#1. Text Files Eg:.txt, .py, .html
#2. Binary Files Eg: .jpg, .mp4
#3. CSV Files(Comma seperated values)

# x= create new file
# r= read the content in a file
# w= write the content in a file
# a= append the content in a file(add at the end)

#Creates a new file
# open("data.txt","x")
# a=open("data.txt","w")
# #writes text
# a.write("This is my first file handling program.")
# a.close()     #frees memory


# b=open("data.txt", "a")  # add data in the end of previous ond but not delete previous content
# b.write("hello")
# b.close()

# x=open("data.txt","r")
# print(x.read())
# x.close()

# automtically closes file BEST METHOD
# with open("data.txt")as f:
#     print(f.read())



while(True):
    print("FILE MANAGEMENT IN PYTHON ")
    print("1. Create file")
    print("2. Read file")
    print("3. Edit file")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if(choice==1):
        create=input("Enter the name of the file you want to create:")
        open(create,"x")
        print(create,"has been created successfully")
    elif(choice==2):
        create2=input("Enter the name of the file you want to read:")
        print("The content in",create2,"is:",)
        b=open(create2,"r")
        print(b.read())
        b.close()
    elif(choice==3):
        create3=input("Enter the name of the file you want to edit:")
        data=input("Enter the data to add:")
        a=open(create3,"w")
        a.write(data)
        a.close()
        print("Data added to the ",create3,"successfully")
    else:
        print("closing this program")
        break


