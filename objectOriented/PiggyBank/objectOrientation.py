# Stage 1
class PiggyBank:
    pass

print("Hello")
pg1 = PiggyBank()
print(pg1)
print(id(pg1))
print(hex(id(pg1)))
print(type(pg1))
print(pg1.__class__)

# Stage 2 -Extensible
class PiggyBank:
    pass


pg1 = PiggyBank()
print(pg1)
print(id(pg1))
print(pg1.__class__)
pg1.balance = 10        # It creates a variable balance  i.e Object pg1 got extended
pg1.lt = 10             # It creates a variable lt
print(pg1.balance)
print(pg1.lt)


pg2 = PiggyBank()
print(pg2)
print(id(pg2))
print(pg2.__class__)
pg2.balance = 200       # It creates a variable balance  i.e Object pg2 got extended
pg2.lt = 200            # It creates a variable lt
print(pg2.balance)
print(pg2.lt)


print(isinstance(pg1,PiggyBank))
print(isinstance(pg2,PiggyBank))


# Stage 3 - __init__
class PiggyBank:
    def __init__(self):
        print("Entering Init")
        print(id(self))
        print("Leaving Init")


pg1 = PiggyBank()
print(id(pg1))
pg1.balance = 10
pg1.lt = 10
print(pg1.balance)
print(pg1.lt)


pg2 = PiggyBank()
print(id(pg2))
pg2.balance = 200
pg2.lt = 200
print(pg2.balance)
print(pg2.lt)

# Stage 4 - self
class PiggyBank:
    def __init__(self):           #Constructor
        print("Entering Init")
        self.balance = 0
        self.lt = 0
        print("Leaving Init")


pg1 = PiggyBank()
print(pg1.balance)
print(pg1.lt)

pg2 = PiggyBank()
print(pg2.balance)
print(pg2.lt)


# Stage 5 - Object Oriented Piggy
print("Welcome to Object Oriented PiggyBank")

class PiggyBank:

    def __init__(self):
        self.balance = 0
        self.lt = 0

    def deposit(self,amount):
        self.balance = self.balance + amount
        self.lt = amount

    def withdraw(self,amount):
        if(self.balance >= amount):
            self.balance -= amount
            self.lt = -amount

    def statement(self):
        print("Balance =",self.balance)
        print("Last Transaction =",self.lt)



pg1 = PiggyBank()

pg1.deposit(100)
pg1.deposit(100)

pg1.statement()

pg1.withdraw(50)

pg1.statement()

pg2 = PiggyBank()

pg2.deposit(1000)
pg2.deposit(1000)

pg2.statement()

pg2.withdraw(500)

pg2.statement()