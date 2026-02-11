import random

choose = input("Favorite Team(1), or Guess Number(2)\n"
               "")

if choose == 1:
    Fav_Team = input("What's the name of your favorite team?")

    for i in range(20):
        print("Go", Fav_Team)
elif choose == 2:
    print("It works")
    for i in range(3):
        guess_num = input("Guess a number: ")
        Real_Num = random.randomint(1,20)
        if guess_num == Real_Num:
            print("You got it!")
            break
        else:
            print("Guess again")
