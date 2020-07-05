# for with else
print("Entering Program")
print("About to enter For Loop")

for i in [0,1,2,3,4]:        
    print("Namaste")        
    print("Python")
else:                
    print("शेषतस्")

print("Just Completed For Loop")
print("Leaving program")

# for with break
print("Entering Program")
print("About to enter For Loop")

for i in [0,1,2,3,4]:        
    print("Namaste")
    if i == 3 :
        break   
    print("Python")
else:                
    print("शेषतस्")

print("Just Completed For Loop")
print("Leaving program")

# for with continue
print("Entering Program")
print("About to enter For Loop")

for i in [0,1,2,3,4]:        
    print("Namaste")
    if i < 3 :
        continue  
    print("Python")
else:                
    print("शेषतस्")

print("Just Completed For Loop")
print("Leaving program")

# for with range
print("Entering Program")
print("About to enter For Loop")

for i in range(5):        
    print("Namaste")
    if i < 3 :
        continue  
    print("Python")
else:                
    print("शेषतस्")

print("Just Completed For Loop")
print("Leaving program")