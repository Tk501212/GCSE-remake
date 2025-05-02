import random 

gameover = False 
lives = 3
score = 0

while gameover == False and lives > 0:
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    answer = num1 + num2
    print(num1, "+" , num2, "= ?")
    guess = input(" just gimme your moneyy: ")
    guess = int(guess)
    if guess == answer:
        print("noice")
        score = score + 1
    else:
        print("nuh uh uh!!!")
        gameover = True

print("Game over, you scored:", score)




















