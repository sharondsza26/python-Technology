account = [0,0,0]

def deposit(v):
    if v > 0:
        account[1] += v
        account[2] = v

def withdraw(v):
    if v > 0 and v <= account[1]:
        account[1] -= v
        account[2] = -v

def statement():
    print("Account: ",account[0])
    print("Balance: ",account[1])
    print("Last Transaction: ",account[2])

deposit(100)
statement()

deposit(190)
withdraw(87)
statement()