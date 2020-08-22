import os

os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage2")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

myfile = open("test2.txt","r")

# Reading till the end of the file
data = myfile.read()
print("test.txt contains ->",data)
