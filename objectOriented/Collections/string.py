# Stage 1
str1 = "HelloWorld"
str2 = "HelloWorld"
print(str1)
print(str2)
print(id(str1))
print(id(str2))

# is operator

if str1 is str2 :
    print("Same object")
else :
    print("Different object")

# is not operator
if str1 is not str2 :
    print("********")
else :
    print("#########")

# isinstance
k = isinstance(str1,str)
print(k)

# Stage 2
str = "HelloWorld"
print(str)
print(id(str))
str = str + "HelloUniverse"
print(str)
print(id(str))

# will always be true because we're  using the same handle
if str is str :
    print("#")
else :
    print("*")

# Stage 3  -upper and lower
str1 = "HelloWorld"
print(str1)
str2 = str1.upper()
print(str2)
str3 = str1.lower()
print(str3)
print(id(str1))
print(id(str2))
print(id(str3))

# Stage 4   -length
str1 = "HelloWorld"
print(str1)
str2 = str1
print(str2)
str1 = str1 + "HelloUniverse"
print(str1)
print(str2)
print(len(str1))
print(len(str2))
print(str1.__len__())

# Stage 5  -slicing
str1 = "HelloWorld"
print(str1)
str2 = str1[5:]
str3 = str1[:5]
print(str2)
print(str3)

# Stage 6  -replace
str1 = "10,20,30,40"
print(str1)
str2 = str1.replace(',',';')
print(str2)

# Stage 7 -split
str1 = "cat,dog,sparrow,monkey"
print(str1)
str2 = str1.replace(',',';')
print(str2)
l1 = str1.split(',')
print(l1)

# Stage 8   -join
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