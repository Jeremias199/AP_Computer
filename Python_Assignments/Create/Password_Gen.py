import random
from typing import List

Samples_UI = int(input("How many random samples do you need? "))
High_Bound = int(input("Highest number in your random number generator: "))
Low_Bound = int(input("Lowest number in your random number generator: "))


def generator(amt_looped, high, low,):
    list_stuff = []
    rand_list = []
    if amt_looped >= 10000:
        print("TOO MANY SAMPLES")
    elif amt_looped < 10000:
        for i in range(amt_looped):
            list_stuff.append(i+1)
            Random = random.randint(low, high)
            rand_list.append(Random)
        print(list_stuff , "\n" , rand_list)

generator(Samples_UI, High_Bound, Low_Bound)