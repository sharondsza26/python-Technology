# Stage 1
print("Namaste")
print("Namaste")
print("Namaste")

# Stage 2 -while
i = 0
while i < 5 :
    print("Namaste")
    i = i + 1

#  Stage 3 -function
def greeting() :
    i = 0
    while i < 5 :
        print("Namaste")
        i = i + 1

print("Welcome")
greeting()
print("Bye")

# Stage 4 -parameters
print("Welcome")
def greeting(v) :
    i = 0
    while i < v :
        print("Namaste")
        i = i + 1

greeting(3)
print("Once Again")
greeting(5)

# Stage 5 -2 param
print("Welcome")
def greeting(message, times) :
    i = 0
    while i < times :
        print(message)
        i = i + 1

greeting("Namaste",3)
print("Once Again")
greeting("Hello World",5)

# 
print("Welcome")
def greeting(message,times) :
    i = 0
    while i < times :
        print(message)
        i = i + 1

# greeting("Namaste",3)
# print("Once Again")
# greeting("Hello World",5)
# greeting("oh","ok",4)
# greeting(7,"ok")
# greeting(times)

# Stage 6 - return val of a function
print("Welcome")

def f1(a,b) :
    r1 = 2 * a
    r2 = 2 + b
    r = r1 + r2
    return r

i = f1(1,2)
j = f1(3,4)
k = f1(5,6)
