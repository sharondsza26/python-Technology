import os

os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage4")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Read Multiple Lines
myfile = open("test4.txt","r")
for data in myfile.readlines():
    print("test.txt contains ->",data)