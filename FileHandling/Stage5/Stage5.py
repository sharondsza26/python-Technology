import os

os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage5")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Writing to File
myfile = open("test5.txt","w")

print("Please Enter a Word")
data = input(">")

print("Writing ->",data)
myfile.write("{} \n".format(data))

myfile.close()