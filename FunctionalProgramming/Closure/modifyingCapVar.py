# Stage 4
print("Welcome to Closure")

def f1(a,b):
    print("Entering f1")
    print("a = ",a)
    print("b = ",b)
    def f2(c,d):
        #to modify captured vars, f2 has to declare them as non-local var
        nonlocal a
        nonlocal b
        print("Entering f2")
        print("c = ",c)
        print("d = ",d)
        # Captured variables
        print("a = ",a)
        print("b = ",b)
        a = a + 3       #non-local ***(this is not global a and b)
        b = b + 4       #non-local
        print("Leaving f2")
    f2(3,4)         
    print("a = ",a)     #after modifying
    print("b = ",b)
    print("Leaving f1")

f1(10,20)
f1(1,2)