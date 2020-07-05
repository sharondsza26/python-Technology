# using while-loop with Lists 

#index-0--1--2--3
l1 =  [10,20,30,40]

# Printing list
i = 0
while i < 4:
    print(l1[i])
    i = i + 1

# Apply a tranform to every element of the list
j = 0  
while j < 4:
    l1[j] = l1[j]*2
    j = j + 1

# Printing modified list
i = 0
while i < 4:
    print(l1[i])
    i = i + 1