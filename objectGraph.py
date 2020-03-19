print("Welcome to Object Graph1")
l1 = [10,20,True,"cat"]
l2 = [90,l1,False,[1,2,3],(4,5,6)]
t1 = [l1,l2,9,10]
d1 = {
    "a" : [-1,-2,-3],
    "b" : ['e','a','r'], 
    "c" : (t1,l1,l2),
    "d" : {"m":11,"n":22,"o":33,"p":[55.66]}
}
print(l1[3])
print(d1["b"][2])
print("Thankyou for using python's object graph")
