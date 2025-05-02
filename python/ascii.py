numberOfChars = input("number of characters: ")
numberOfChars = int(numberOfChars)

numOfBits = numberOfChars * 8

print(numOfBits)

import random
sentenceFile = open("asciicode.txt", "r")
fileContent = sentenceFile.read()
listOfsentences = fileContent.split("\n")

ascii = random.choice(listOfsentences)
print(ascii)












