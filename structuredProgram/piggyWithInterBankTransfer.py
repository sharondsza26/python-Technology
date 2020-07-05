banks = []
for i in range(3):
    bank = []
    for j in range(10): 
        bank.append([j,0,0])
    banks.append(bank)

def deposit(bank,accno,v):
    bank = banks[bank]
    acc = bank[accno]
    if v > 0:
        acc[1] += v
        acc[2] = v

def withdraw(bank,accno,v):
    bank = banks[bank]
    acc = bank[accno]
    if v > 0 and v <= acc[1]:
        acc[1] -= v
        acc[2] = -v

def statement(bank,accno):
    bank = banks[bank]
    acc = bank[accno]
    print("Account: ",acc[0])
    print("Balance: ",acc[1])
    print("Last Transaction: ",acc[2])

def transfer(sender,sbank,receiver,rbank,v):
    withdraw(sbank,sender,v)
    deposit(rbank,receiver,v)

def printBank(bank):
    size = len(banks[bank])
    for i in range(size):
        statement(bank,i)

for i in range(3):
    printBank(i)

print("---------------------Testing Operations---------------------")

deposit(2,0,100)
statement(2,0)

deposit(0,7,190)
withdraw(0,7,50)
statement(0,7)

print("---------------------Testing Transfer---------------------")

transfer(7,0,0,2,35)
statement(0,7)
statement(2,0)