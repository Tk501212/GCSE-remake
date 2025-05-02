import random

number = random.randint(1,100) 
correct = False 

while correct == False:
    guess = input("Guess: ")
    guess = int(guess)

    if guess == number:
        print("Correct")
        correct = True
    elif guess < number:
        print("incorrect")
        print("too low")
    else:
        print("incorrect")
        print("too high")









