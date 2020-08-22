import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/UtilizingFile/Frequency")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")


# Stage 1 - Finding frequency
file = open("./rawdata.txt",mode='r')
data = file.read()
print(data)
list1 = data.split(",")
print(list1)
num = int(input("Enter number"))
count = 0
for v in list1:
    if(int(v.strip()) == num ): count = count + 1
print("The frequency of number is ",count)