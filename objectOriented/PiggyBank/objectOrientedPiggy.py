print("Welcome to Object Oriented PiggyBank")

class PiggyBank:

    def __init__(self):
        self.balance = 0
        self.lt = 0

    def deposit(self,amount):
        if(amount > 0):
            self.balance = self.balance + amount
            self.lt = amount

    def withdraw(self,amount): 
        if(self.balance >= amount):
            self.balance -= amount
            self.lt = -amount

    def statement(self):
        print("|Statment|")
        print("----------------------------------")
        print("Balance =",self.balance)
        print("Last Transaction =",self.lt)
        print("----------------------------------")



pg = PiggyBank()

print("Welcome to Interactive PiggyBank\n")
print("Help-")
print("Type d to Deposit")
print("Type w to Withdraw")
print("Type s to print the Statement")
print("Type q to Quit\n")

action = input("action> ").lower()
while(action != "q"):
    if(action == "s"):
        pg.statement()
    elif(action == "d"):
        print("Please Enter the value to be Deposited")
        amount = int(input("deposit> "))
        pg.deposit(amount)
    elif(action == "w"):
        print("Please Enter the value to be Withdrawn")
        amount = int(input("withdraw> "))
        pg.withdraw(amount)
    elif(action == "h"):
        print("Help-")
        print("Type d to Deposit")
        print("Type w to Withdraw")
        print("Type s to print the Statement")
        print("Type q to Quit\n")
    else:
        print("Please Enter A Correct Command")
    action = input("action> ").lower()