import random, time 
#typing tester

#open up the file
sentenceFile = open("sentences.txt", "r")
#read the context
fileContent = sentenceFile.read()
listOfsentences = fileContent.split("\n")
#pick a random sentence
sentence = random.choice(listOfsentences)
print(sentence)
startTime = time.time()
#display the sentence to the user
#user needs to type in the sentence
userAnswer = input(">>")
endTime = time.time()
overallTime = endTime - startTime
overallTime = round(overallTime,2)
print(overallTime, "seconds")

sentenceLength = len(sentence)
correct = 0

for i in range(sentenceLength):
    if sentence[i] == userAnswer[i]:
        correct = correct + 1

accuracy = correct / sentenceLength * 100
print(accuracy, "%")
#check for accuracy










