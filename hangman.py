###HANGMAN !
import random
#choose a word - picked at random by a computer 
words = ["fish","badger","cheese","apple"]
lives = 10
win = False
word = random.choice(words)
wordlength = len(word)
dashes = "-" * wordlength
print(word)

#repeat over and over until they either win OR lose
while lives > 0 and win == False:
     #showdashes
    print(dashes)

    #enter a letter 
    guess = input("Enter Letter: ")

#is the letter in the word
    if guess in word:
        print("correct")
        newDashes = "" 
        #go through each letter in the word
        for i in range(wordlength):
              #if it is the guessed letter
            if word[i] == guess:
                #update the dashes to have that letter
                newDashes = newDashes + guess 
            else:
                #if not keep the old symbol for the dashes
                newDashes = newDashes + dashes[i]
            dashes = newDashes 
            if dashes == word:
                win + True 
        #if it isn't - 
    else:
        #remove a life
        lives = lives - 1
        print("incorrect")
        print("you have" , lives , "lives remaining")
        #maybe show guessed letters too








        #if it is in the word 
        

