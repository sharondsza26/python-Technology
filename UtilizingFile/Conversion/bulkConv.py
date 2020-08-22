import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/UtilizingFile/Conversion")
x = os.getcwd()
print("Now cwd is .......", x)
print("Welcome to File Handling")


# Stage 3 -  Finding number frequency
file = open("./rawdata.txt",mode='r')
data = file.readline()
keys = file.readline()
result = []
print(data)
print(keys)
data = data.split(",")
keys = keys.split(",")
print(data)
print(keys)
for v in range(len(data)):
    data[v] = int(data[v].strip())
for v in range(len(keys)):
    keys[v] = int(keys[v].strip())
for k in keys:
    count = 0
    for v in data:
        if( v == k ): count = count + 1
    print(("The frequency of %d is %d")%(k,count))
    result.append(count)
print(result)