balance = 0
transactions = [0,0,0,0,0,0,0,0,0,0]
counter = 0

def deposit(amount):
    global balance
    if(amount > 0):
        balance = balance + amount
        transaction(amount)

def withdraw(amount):
    global balance
    if(amount > 0 and balance >= amount):
        balance = balance - amount
        transaction(-amount)

def transaction(amount):
   global counter
   if counter == 10:
      counter = 0
   transactions[counter] = amount
   counter += 1

def statement():
   print("|Statment|")
   print("----------------------------------")
   print("Balance =",balance)
   print("Last Transactions")
   for t in range(len(transactions)):
      if(transactions[t] != 0):
        print("|Transaction {}| ---> |{}|".format(t+1,transactions[t]))
   print("----------------------------------")


print("Welcome to Interactive PiggyBank\n")
print("Help-")
print("Type d to Deposit")
print("Type w to Withdraw")
print("Type s to print the Statement")
print("Type q to Quit\n")

action = input("action> ").lower()
while(action != "q"):
    if(action == "s"):
        statement()
    elif(action == "d"):
        print("Please Enter the value to be Deposited")
        amount = int(input("deposit> "))
        deposit(amount)
    elif(action == "w"):
        print("Please Enter the value to be Withdrawn")
        amount = int(input("withdraw> "))
        withdraw(amount)
    elif(action == "h"):
        print("Help-")
        print("Type d to Deposit")
        print("Type w to Withdraw")
        print("Type s to print the Statement")
        print("Type q to Quit\n")
    else:
        print("Please Enter A Correct Command")
    action = input("action> ").lower()