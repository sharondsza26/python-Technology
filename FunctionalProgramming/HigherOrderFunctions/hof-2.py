# Stage 2 -Customization in Server
# Client-Server 

# Server
def Server(choice) :
    print("Entering Server")
    print("Task1")

    if choice == 0 :
        print("------")
        print("------")
        print("------")
    if choice == 1 :
        print("/////")
        print("/////")
        print("/////")
    print("Task3")
    print("Leaving Server")

# Client1
def Client1() :
    print("Entering Client1")
    print("Job1")
    Server(0)
    print("Job2")
    print("Leaving Client1")

# Client2
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