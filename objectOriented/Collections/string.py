# Stage 1
str = "HelloWorld"
print(str)

# Stage 2
str = "HelloWorld"
print(str)
print(id(str))
str = str + "HelloUniverse"
print(str)
print(id(str))

# Stage 3
str1 = "HelloWorld"
print(str1)
str2 = str1.upper()
print(str2)
str3 = str1.lower()
print(str3)
print(id(str1))
print(id(str2))
print(id(str3))

# Stage 4
str1 = "HelloWorld"
print(str1)
str2 = str1
print(str2)
str1 = str1 + "HelloUniverse"
print(str1)
print(str2)
print(len(str1))
print(len(str2))

# Stage 5
str1 = "HelloWorld"
print(str1)
str2 = str1[5:]
str3 = str1[:5]
print(str2)
print(str3)

# Stage 6
str1 = "10,20,30,40"
print(str1)
str2 = str1.replace(',',';')
print(str2)

# Stage 7
str1 = "cat,dog,sparrow,monkey"
print(str1)
str2 = str1.replace(',',';')
print(str2)
l1 = str1.split(',')
print(l1)

# Stage 8
l1 = ['mango','grapes','orange','pineapple']
print(l1)
str1 = ";"
print(str1)
str2 = str1.join(l1)
print(str2)

# Stage 9
str1 = "amit@gmail.com"
if(str1.endswith("gmail.com")) :
    print("Valid Email ID")
else:
    print("Invalid Emain ID")


# Stage 10
print("Please Enter gmail id")
str1 = input()
if(str1.endswith("gmail.com")) :
    print("Valid Email ID")
else:
    print("Invalid Emain ID")

# Stage 11
print("Please Enter gmail id")
str1 = input()
if(str1.startswith("amit")) :
    print("Valid Email ID")
else:
    print("Invalid Email ID")


# Stage 12
names = ['amit','parag','mangesh']
domains = ['google.com','yahoo.com','rajeshpatkar.com']
print("Please Enter email id")
email = input()
emailparts = email.split("@")
if(emailparts[0] in names and emailparts[1] in domains) :
    print("Valid Email ID")
else:
    print("Invalid Email ID")


# Stage 13
names = ['amit','parag','mangesh']
domains = ['google.com','yahoo.com','rajeshpatkar.com']
print("Please Enter email id")
email = input()
emailparts = email.split("@")
if(emailparts[0].lower() in names and emailparts[1].lower() in domains) :
    print("Valid Email ID")
else:
    print("Invalid Email ID")    