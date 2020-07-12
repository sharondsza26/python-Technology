# Stage 2
print("Welcome to Closure")

# Container / Environment
def f1(a,b):  
    print("Entering f1")
    print("a = ",a)
    print("b = ",b)
    # f2 is not visible outside
    def f2(c,d):        #nested/local functn
        print("Entering f2")
        print("c = ",c)
        print("d = ",d)
        print("Leaving f2")
    f2(3,4)             #Can be called inside f1 only
    print("Leaving f1")

f1(10,20)
f1(1,2)

# after f1 is over Activation rec of f1 will die
# AR of f1 has a,b,f2(ref var f2)
# which means f2 will be deleted
# since nothing is pointing to f2
# f2 obj will get garbage collected
# how many ever times f1 is called, f2 is created and destroyed