import random

print("Welcome to the Auction")

base = random.randint(1,100)

print("Please Enter you Bid")

bid = int(input())

print("The base value was = ",base)
print("The bid you offered =",bid)

if bid >= base:
   print("Item sold! :)")
else:
   print("Item Auction Lost! :(")

print("Market Closed")
