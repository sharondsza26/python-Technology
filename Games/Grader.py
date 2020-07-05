print("Welcome to Grader")

print("Please Enter your marks")

marks = int(input())

if marks >= 0 and marks <= 100:
   if marks >= 80:
       print("You passed with Distinction")
   elif marks >= 60:
       print("You passed with First Class")
   elif marks >= 35:
       print("You passed")
   else:
       print("You Failed")
else:
   print("Wrong Input")
