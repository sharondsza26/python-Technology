# #Creating a List
# a = [10,20,30,40]
# #Printing List
# print(a)
# #Obtaining length of List
# l = len(a)
# #Printing length
# print(l)

# # Stage 1
# print("Entering Python Program")
# a = [10,20,30,40]
# #Printing List
# i = 0
# while i < 4:
#     print(a[i])
#     i = i + 1  # can also be written as i+=1
# print("Leaving Python Program")

# # Stage 2
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40]
# #Printing List
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 1  # can also be written as i+=1
# print("Leaving Python Program")

# # Stage 3 -Append
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40]
# print("List values before Appending",a)
# a.append(50)
# a.append(60)
# print("List values after Appending",a)
# print("Leaving Python Program")

# # Stage 4 -Extend
# a = [10,20,30,40]
# print("List values before Extending",a)
# a.extend([50,60])
# print("List values after Extending via List literal",a)
# print("Leaving Python Program")

# # Stage 5
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40]
# print("List values before Extending",a)
# a.extend([50,60])
# print("List values after Extending via List literal",a)
# b = [70,80]
# print("Values in list b")
# a.extend(b)
# print("List values after Extending via list b",a)
# print("List b is not affected by this extention",b)
# print("Leaving Python Program")

# # Stage 6 -Insert
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40]
# print("List values before insertion",a)
# a.insert(1,333)
# print("List values after insertion at index 1",a)
# print("Leaving Python Program")

# # Stage 7 -Remove
# print("Entering Python Program")
# a = [10,20,30,40]
# print("List values before insertion",a)
# a.insert(1,333)
# print("List values after insertion at index 1",a)
# a.remove(333)
# print("List value after value 333 is removed",a)
# print("Leaving Python Program")

# # Stage 8 -Remove by index
# print("Entering Python Program")
# a = [10,20,30,40]
# print("List values before insertion",a)
# a.insert(1,333)
# print("List values after insertion at index 1",a)
# a.pop(1)
# print("List value after value at index 1 is popped",a)
# print("Leaving Python Program")

# # Stage 9 -Popping rightmost value 
# print("Entering Python Program")
# a = [10,20,30,40]
# print("List values before insertion",a)
# a.insert(1,333)
# print("List values after insertion at index 1",a)
# a.pop(1)
# print("List value after value at index 1 is popped",a)
# r = a.pop()
# print("The popped value is ",r)
# print("List after popping rightmost value is ",a)
# print("Leaving Python Program")

# # Stage 10 -Reverse
# print("Entering Python Program")
# a = [10,20,30,40]
# print("List values before reversing",a)
# a.reverse()
# print("List values after reversing",a)
# print("Leaving Python Program")

# # Stage 11 -Sort
# print("Entering Python Program")
# #Creating a List
# a = [50,60,777,3,532,521,20,1000,4]
# print("List before sorting",a)
# #Sorting the List
# a.sort()
# print("List after sorting",a)
# c = [1.0,4.33,0.2,0.446,600.33,43.21]
# print("Float List before sorting",c)
# # Sorting the List
# c.sort()
# print("Float List after sorting",c)
# b = ["z","u","q","w","v","j","t"]
# print("String List before sorting",b)
# # Sorting the List
# b.sort()
# print("String List after sorting",b)
# print("Leaving Python Program")

# # Stage 12 -Slicing
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# print("List before slicing",a)
# # Slicing the List
# b = a[0:5]
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")


# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# print("List before slicing",a)
# # Slicing the List
# b = a[3:]           #ie from 3:len(a)
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")


# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# print("List before slicing",a)
# # Slicing the List
# b = a[:7]           #ie from 0:7
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")


# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# b = a[1:8:3]    #start:end:step
# print(b)
# print("List before slicing",a)
# # Slicing the List
# b = a[:]            #ie from 0:len(a)
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")

# # Stage 13 -Negative index
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# #Printing List
# for i in [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
#     print(a[i])
# print("Leaving Python Program")

# # Stage 14 -Negative Slicing
# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# print("List before slicing",a)
# # Slicing the List
# b = a[:-6]
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")

# print("Entering Python Program")
# #Creating a List
# a = [10,20,30,40,50,60,70,80,90,100]
# print("List before slicing",a)
# # Slicing the List
# b = a[-8:]
# print("Sliced List",b)
# print("List after slicing",a)
# print("Leaving Python Program")

# a = [10,20,30]
# b = [1,2,3]
# f = []
# f.extend(a)
# f.extend(b)
# print(f)
# c = a + b
# print(c)
# d = a * 3
# print(d)
# e = c * 2 + d * 4
# print(e)


# str = "hello world"
# s = str[2:9]
# print(s)
# s1 = str[9:4:-1]
# print(s1)
# s2 = str*3
# print(s2)
# s3 = str + s
# print(s3)


