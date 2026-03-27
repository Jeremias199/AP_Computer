import random
from multiprocessing.connection import answer_challenge

Vocab_Words = []
Vocab_Definition = []

Vocab_Amt = int(input("How many vocabulary words do you have? \n"))

for i in range(Vocab_Amt):
    Vocab_Words.append(input("Vocabulary Words: "))
    Vocab_Definition.append(input("Vocabulary Definition: "))


def card(test):
    Choice = int(input("Do you want to look ar your vocabulary words (press 1), or Do you want to test your knowledge? (press 2)?"))

    if(Choice == 1):
        for j in range(test):
            print("Word: ", Vocab_Words[j], "\nDefinition: ", Vocab_Definition[j])
    elif(Choice == 2):
        Rand_Word = random.randint(0,test)

        for k in range(Rand_Word + 1):
            print("Word: ", Vocab_Words[k],)
            answer = input( "\nType the Definition: ")

            if answer == Vocab_Definition[k]:
                print("Correct!!!")
            else:
                print("WRONG")

card(Vocab_Amt)