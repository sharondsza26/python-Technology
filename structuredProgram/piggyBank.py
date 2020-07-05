# # Stage 1
# print("Welcome to PiggyBank")

# balance = 0
# lt = 0

# def Statement() :
#     print("Current Balance =",balance)
#     print("The last transaction was",lt)

# def Deposit(amount) :
#     global balance    #Important Note
#     global lt
#     balance = balance + amount
#     lt = amount

# def Withdraw(amount) :
#     global balance
#     global lt
#     if balance >= amount :
#         balance = balance - amount
#         lt = -amount
#     else :
#         print("Insufficient Balance")


# Statement()

# Deposit(20)
# Deposit(10)
# Statement()

# Withdraw(10)
# Statement()
# Withdraw(30)

# Statement()


# Stage 2 -User Input
print("Welcome to PiggyBank")

balance = 0
lt = 0

def Statement() :
    print("Current Balance =",balance)
    print("The last transaction was",lt)

def Deposit(amount) :
    global balance    #Important Note
    global lt
    balance = balance + amount
    lt = amount

def Withdraw(amount) :
    global balance
    global lt
    if balance >= amount :
        balance = balance - amount
        lt = -amount
    else :
        print("Insufficient Balance")

Statement()

amount = int(input("Enter the amount to be Deposited"))         #User input
Deposit(amount)
Statement()

amount = int(input("Enter the amount to be Deposited"))
Deposit(amount)
Statement()

amount = int(input("Enter the amount to be Withdrawn"))
Withdraw(amount)
Statement()

amount = int(input("Enter the amount to be Withdrawn"))
Withdraw(amount)
Statement()
