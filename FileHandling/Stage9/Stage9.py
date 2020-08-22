import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage9")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Read with write 
myfile = open("test9.txt","r+")

print("----------------------------------")
for data in myfile.readlines():
    print("test9.txt contains ->",data)
print("----------------------------------")

myfile.write("Testing Read with Write")
myfile.seek(0)

print("----------------------------------")
for data in myfile.readlines():
    print("test.txt contains ->",data)
print("----------------------------------")