# Stage 5
print("Welcome to Closure")
g = None
def f1(a,b):
    print("Entering f1")
    print("a = ",a)
    print("b = ",b)
    def f2(c,d):
        nonlocal a
        nonlocal b
        print("Entering f2")
        print("c = ",c)
        print("d = ",d)
        print("a = ",a)
        print("b = ",b)
        a = a + 3
        b = b + 4
        print("Leaving f2")
        # end of f2
    f2(3,4)
    print("a = ",a)
    print("b = ",b)
    global g    #to modify g f1 has to declare global g
    g = f2      #g is now referring to f2 obj
    print("Leaving f1")
# end of f1

f1(10,20)       
#activation record of f1 is destroyed, 
# but f2 will not die because g is referring to f2
#nested function is alive 

g(-1,-2)       #nested function escaped its environment f1 
g(8,9)


# because f2 is escaping its enclosure
# and wont be able to access a and b after escaping
# python creates closure obj before a and b are destroyed (ie before f1 is ended)
# and since a,b is required by f2  
# python gives the closure object to f2