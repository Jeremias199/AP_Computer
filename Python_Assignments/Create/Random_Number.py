import random

Samples_UI = int(input("Random Samples: "))
Repeating_Num = input("Would you like repeating numbers?\n(y/n):").lower()
Bounds = input("Type the lowest and highest number to generate (make sure to separate with \",\" OR \" \"): ")

bounds_list = Bounds.replace(',', ' ').split()
Low = int(bounds_list[0])
High = int(bounds_list[1])


def generator(amt_looped, high, low, repeating):
    if amt_looped >= 10000:
        print("TOO MANY SAMPLES")
    elif amt_looped < 10000:
        rand_list = []
        list_stuff = []

        #It'll be impossible to generate a random number if the sample size is greater than the highest number
        if repeating == "n" and amt_looped > (high-low+1):
            print("IMPOSSIBLE GENERATION")
            return
        elif repeating == "n" and amt_looped <= high:
            rand_list = random.sample(range(low,high +1),amt_looped)
        elif repeating == "y":
            for i in range(amt_looped):
                rand_list.append(random.randint(low,high+1))

        list_stuff = list(range(1,amt_looped + 1))
        print(f"\nSample Number: {list_stuff} \nRandom Number: {rand_list}")

generator(Samples_UI,High, Low, Repeating_Num)