# Stage 3
print("Welcome to Closure")

def f1(a,b):        #Environment in which f2 is born
    print("Entering f1")
    print("a = ",a)
    print("b = ",b)
    def f2(c,d):
        print("Entering f2")
        #local var of f2
        print("c = ",c)        
        print("d = ",d)
        # Captured variables
        #local var of f1
        print("a = ",a)        #f2 is printing value of a and b? Yes, because it is "born" in f1
        print("b = ",b)
        print("Leaving f2")
    f2(3,4)
    print("Leaving f1")

f1(10,20)
f1(1,2)