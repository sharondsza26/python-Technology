# Stage 1 -creation
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1)

# Stage 2 -read
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1["name"])
print(d1["surname"])
print(d1["address"])

d1["name"] = "Aegon"
d1["surname"] = "Targaryen"
d1["address"] = "Dragonstone"

#Adding a new Property
d1["house words"] = "Fire and Blood"

print(d1["name"])
print(d1["surname"])
print(d1["address"])
print(d1["house words"])

# Stage 3 -looping
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

for p in d1:
   print(p)
   print(d1[p])

# Methods

# Stage 1 -keys
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1.keys())

# Stage 2 -values
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1.values())

# Stage 3 -items
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1.items())

for key,value in d1.items():
    print(key,"-",value)

# Stage 4 -get
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1["name"])

print(d1.get("name"))

# Will not Work
# It will throw an exception
# print(d1["maidenname"])

print(d1.get("maidenname"))

# Stage 5 -pop
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1["name"])

print(d1.pop("name"))

print(d1)

# Stage 6 -update
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1)
d1.update({ "address":"Dragonstone" })
print(d1)
d1.update({ "house words":"Winter is Coming" })
print(d1)

# Stage 7 -clear
d1 = {
"name":"Jon",
"surname":"Snow",
"address":"Winterfell / Castle Black"
}

print(d1)

d1.clear()

print(d1)