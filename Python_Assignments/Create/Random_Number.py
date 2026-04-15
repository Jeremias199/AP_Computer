import random

Samples_UI = int(input("How many random samples do you need? "))
Repeating_Num = input("Would you like repeating numbers? (y/n)").lower()
Bounds = input("Random number bounds (low and high) separate with space or comma: ")
bounds_list = Bounds.replace(',', ' ').split()
Low = int(bounds_list[0])
High = int(bounds_list[1])


def generator(amt_looped, high, low, repeating):
    if amt_looped >= 10000:
        print("TOO MANY SAMPLES")
    elif amt_looped < 10000:
        #for i in range(amt_looped):
        rand_list = []
        list_stuff = []
        if repeating == "n" and amt_looped > (high-low+1):
            print("IMPOSSIBLE GENERATION")
            return

        if repeating == "n" and amt_looped <= high:
            rand_list = random.sample(range(low,high +1),amt_looped)
        elif repeating == "y":
            for i in range(amt_looped):
                rand_list.append(random.randint(low,high+1))

        list_stuff = list(range(1,amt_looped + 1))
        print(f"\nSample Number: {list_stuff} \nRandom Number: {rand_list}")

generator(Samples_UI,High, Low, Repeating_Num)