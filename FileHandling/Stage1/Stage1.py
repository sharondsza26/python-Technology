# Stage 1
import os

x = os.getcwd()
print("Cwd is .....", x)
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage1")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")
myfile = open("test.txt","r")

# Reading 12 characters
data = myfile.read(12)
print("The data you read from test.txt is ",data)