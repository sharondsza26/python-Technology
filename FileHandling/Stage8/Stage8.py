import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/FileHandling/Stage8")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")

# Appending Multiple data to file
myfile = open("test8.txt","a")

list = [10,20,30,40,50,60,70,80,90,100]

for data in list:
    print("Writing ->",data)
    myfile.write("{} \n".format(data))

myfile.close()