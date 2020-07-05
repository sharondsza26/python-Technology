bank = []
for i in range(10): bank.append([i,0,0])

def deposit(accno,v):
    acc = bank[accno]
    if v > 0:
        acc[1] += v
        acc[2] = v
def withdraw(accno,v):
    acc = bank[accno]
    if v > 0 and v <= acc[1]:
        acc[1] -= v
        acc[2] = -v

def statement(accno):
    acc = bank[accno]
    print("Account: ",acc[0])
    print("Balance: ",acc[1])
    print("Last Transaction: ",acc[2])

def transfer(sender,receiver,v):
    withdraw(sender,v)
    deposit(receiver,v)

def printBank():
    for i in range(len(bank)):
        statement(i)

printBank()

print("---------------------Testing Operations---------------------")

deposit(0,100)
statement(0)

deposit(7,190)
withdraw(7,50)
statement(7)

print("---------------------Testing Transfer---------------------")

transfer(7,0,35)
statement(7)
statement(0)