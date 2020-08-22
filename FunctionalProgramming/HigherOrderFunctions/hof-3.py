# Stage 3 -Customization in Client Side Function
# Client-Server

# Server
def Server(choice) :
    print("Entering Server")
    print("Task1")
    if choice == 0 :
        m1()            #Inversion of control
    if choice == 1 :
        m2()
    print("Task3")
    print("Leaving Server")

# Client1
def m1() :              #CallBack-Server calling client
    print("------")
    print("------")
    print("------")

def Client1() :
    print("Entering Client1")
    print("Job1")
    Server(0)
    print("Job2")
    print("Leaving Client1")

# Client2
def m2() :
    print("/////")
    print("/////")
    print("/////")

def Client2() :
    print("Entering Client2")
    print("Work1")
    Server(1)
    print("Work2")
    print("Leaving Client2")


print("Entering Program for Higher Order Function")
Client1()
Client2()
print("Thank You...")
