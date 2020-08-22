import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage11")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Append with Read
myfile = open("test11.txt","a+")

print("Please Enter a Word")
data = input(">")

while data != "q":
    myfile.write("{} \n".format(data))
    print("Please Enter a Word")
    data = input(">")

myfile.seek(0)

print("----------------------------------")
for data in myfile.readlines():
    print(data)
print("----------------------------------")