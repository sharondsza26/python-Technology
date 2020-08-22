import os
os.chdir("C:/Users/sharo/OneDrive/Desktop/online-pythonTech/UtilizingFile/Keys")
x = os.getcwd()
print("Now cwd is .......", x)

# Stage 2 - Finding key frequencies
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
for k in keys:
    count = 0
    for v in data:
        if(int(v.strip()) == int(k.strip()) ): count = count + 1
    print(("The frequency of %d is %d")%(int(k.strip()),count))
    result.append(count)
print(result)