# Stage 4 -CallBack Design Patterns and HoF
# Client-Server

# Server
def Server(choice) :
    print("Entering Server")
    print("Task1")
    choice()            #Callback
    print("Task3")
    print("Leaving Server")

# Client1
def m1() :              
    print("------")
    print("------")
    print("------")

def Client1() :
    print("Entering Client1")
    print("Job1")
    Server(m1)
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
    Server(m2)
    print("Work2")
    print("Leaving Client2")

# Client3
def m3() :
    print("****")
    print("****")
    print("****")

def Client3() :
    print("Entering Client3")
    print("Chore1")
    Server(m3)
    print("Chore2")
    print("Leaving Client3")


print("Entering Program for Higher Order Function")
Client1()
Client2()
Client3()
print("Thank You...")

# Functions which take other functions as parameters are called higher order functions
