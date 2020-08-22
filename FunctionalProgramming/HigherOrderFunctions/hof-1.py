# Stage 1 -understanding HoF
# Client-Server

# Server
def Server() :
    print("Entering Server")
    print("Task1")
    print("Task2")
    print("Task3")
    print("Leaving Server")

# Client1
def Client1() :
    print("Entering Client1")
    print("Job1")
    Server()
    print("Job2")
    print("Leaving Client1")

# Client2
def Client2() :
    print("Entering Client2")
    print("Work1")
    Server()
    print("Work2")
    print("Leaving Client2")


print("Entering Program for Higher Order Function")
Client1()
Client2()
print("Thank You...")