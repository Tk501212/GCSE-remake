

import random 

GameOver = False
Score = 0

while GameOver == False:
    number = random.randint(0,255)
    binary = bin(number)
    binary = binary[2:]
    binary = binary.zfill(8)

    # print("Convert " + binary + " into denary.")
    # random.randint(0,65536)

    print("convert" , binary, "into denary")#
    answer = input("Answer: ")
    answer = int(answer)

    if answer == number:
        print("correct")
        Score = Score + 1
    else:
        print("incorrect" , "you scored:", Score)
        GameOver = True
    





