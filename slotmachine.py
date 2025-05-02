




import random

def generateLetters():
    letters = []

    print("(C)onstanant or (V)owel")
    Choice = input("C or V: ").upper()
    print(pickLetter(Choice))
    return letters

def pickLetter(Choice):
    vowels = "AEIOU"
    constanants = "BCDFGHJKLMNPQRSTVWXYZ"
    if Choice == "V":  
        random.Choice(vowels)
    else:
        random.Choice(constanants)
