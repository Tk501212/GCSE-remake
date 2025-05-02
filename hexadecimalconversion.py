import random

GameOver = False
Score = 0

while GameOver == False:
    denaryNumber = random.randint(1,255)
    binaryNumber = bin(denaryNumber)
    binaryNumber = binaryNumber[2:]
    binaryNumber = binaryNumber.zfill(8)
    hexNumber = hex(denaryNumber).upper()
    hexNumber = hexNumber[2:]
    hexNumber = hexNumber.zfill(2)

    print("Convert the hexadecimal number of" , hexNumber , "into its binary equivalant." )
    print("give your answer in 8-bit")

    answer = input("answer: ")

    if answer == binaryNumber:
        print("Well done!")
        Score = Score + 1

    else:
        print("wrong!" , "you scored:", Score)
        GameOver = True 
























