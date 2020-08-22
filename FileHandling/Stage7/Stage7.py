import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage7")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")


# Appending data to File
myfile = open("test7.txt","a")

data = "Hello World!"

print("Writing ->",data)
myfile.write("{} \n".format(data))

myfile.close()