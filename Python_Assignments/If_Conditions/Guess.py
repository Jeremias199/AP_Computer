import random

Computer_Num = random.Random(10) ; Player_Guess = int(input("Guess and number from 1-10"))

if Player_Guess == Computer_Num:
    print("You guessed right")
else:
        print("WRONG!")