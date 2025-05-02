import random 

options = ("ROCK" , "PAPER" , "SCISSORS")
playerScore = 0
computerScore = 0

while playerScore < 3 and computerScore < 3:
    playerChoice = input ("(R)OCK (P)APER (S)CISSORS: ")
    computerChoice = random.choice(options) 


    print("you chose" , playerChoice)
    print("the computer chose" , computerChoice )


    if playerChoice == computerChoice:
        print("DRAW")
    else: 
            if playerChoice == "ROCK" and computerChoice == "SCISSORS":
                print("player wins!")
                playerScore = playerScore + 1 
            elif playerChoice == "ROCK" and computerChoice == "PAPER":
                print("computer wins!")
                computerScore = computerScore + 1
            elif playerChoice == "SCISSORS" and computerChoice == "PAPER":
                print("player wins!")
                playerScore = playerScore + 1
            elif playerChoice == "SCISSORS" and computerChoice == "ROCK":
                print("computer wins!")  
                computerScore = computerScore + 1
            elif playerChoice == "PAPER" and computerChoice == "ROCK":
                print("player wins!")
                playerScore = playerScore + 1
            elif playerChoice == "PAPER" and computerChoice == "SCISSORS":
                print("computer wins!")
                computerScore = computerScore + 1
if computerScore == 3:
    print("your trash kid")
else:
    print("GG")
