# a = [10, 20, 30, 40]
# print(a)
# b = []
# for i in a:
#     c = i * 2
#     b.append(c)
#     # b.append(i*2)
# print(b)

# Comprehension
a = [10,20,30,40,50,60]
b = [ v*2 for v in a]
print(a)
print(b)

# Using if
a = [10,20,30,40,50,60]
b = [ v*2 for v in a if v > 20 ]
print(a)
print(b)

# Nesting comprehension
a = [10,20,30,40,50,60]
b = [ k + 3 for k in [ v*2 for v in a if v > 20 ]]
print(a)
print(b)
