# Finding number frequency
list = [10,20,30,40,30,30,40,10,2,2]
num = int(input("Enter number  "))
i,count = 10,0
while i: count = count + 1 if list[(i:=i-1)] == num else count         # if-else as Ternary
print("The frequency of number is ",count)