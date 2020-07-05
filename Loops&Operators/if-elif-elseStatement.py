#Learning if statements.

#if-else
flag = False
print("Entering Program1")
if flag :                  #<--- if expression:  
    print("Inside If")
else:                    #<---clause
    print("Inside Else") #<---suite
print("Leaving program1")


#if-elif-else
i = 20
print("Entering Program2")

if i == 1 :
    print("Value of i is 1")
elif i == 2 :
    print("Value of i is 2")
elif i == 3 :
    print("value of i is 3")
else:
    print("Value of i is other than 1,2 or 3")

print("Leaving program2")

#nested if
i = 3
j = 4
print("Entering Program3")
if i < 5: #venus
    print("###")
    if j == 4: #mars
        print("%%%")
else: #belongs to venus
    print("$$$")

print("Leaving program3")
