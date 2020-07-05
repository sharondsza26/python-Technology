# Number Guess 
import random
print("Welcome, I am TakeChance game...Let's play")
number = random.randint(1,10)
print("I have already guessed a number between 1 and 10")
print("You get 3 chances to get it right and win a prize")
count = 0
while(count < 3):
    count = count + 1
    guess = int(input("Please enter your Guess\n"))
    if(guess == number):
        print("You are lucky... you win the prize")
        break
else:
    print("You exhuasted your turns. Better luck next time")
print("See ya in the next game")