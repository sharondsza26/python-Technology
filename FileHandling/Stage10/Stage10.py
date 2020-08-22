import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage10")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Write with read
myfile = open("test10.txt","w+")

list = [10,20,30,40,50,60,70,80,90,100]

for data in list:
    print("Writing ->",data)
    myfile.write("{} \n".format(data))


myfile.seek(0)

print("----------------------------------")
for data in myfile.readlines():
    print(data)
print("----------------------------------")