# Stage 1
print("Welcome to Closure")

def f1(a,b):        #functn def
    print("Entering f1")
    print("a = ",a)
    print("b = ",b)
    print("Leaving f1")

f1(10,20)       #functn call
d = f1(1,2)     #python will always return a value [in this case it returns none]
print(d)
