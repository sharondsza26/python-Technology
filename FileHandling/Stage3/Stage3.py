import os

os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage3")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Reading one line at a time
myfile = open("test3.txt","r")
print("test.txt contains ->",myfile.readline())
print("test.txt contains ->",myfile.readline())
print("test.txt contains ->",myfile.readline())