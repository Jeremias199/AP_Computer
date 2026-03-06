from functools import total_ordering
from math import degrees

Ask_Amt = int(input("How man songs are in your play list? "))

Energy_List = []

for i in range(Ask_Amt):
    Energy_List.append(int(input("What is the energy rating in the song? (1-10)")))

def analyze_playlist(energy_list):
    Total = 0
    for j in range(len(Energy_List)):
        Total += Energy_List[j]
    Average = Total / Ask_Amt;

    if Average >= 7:
        return "THIS IS A HIGH ENERGY PLAYLIST! Your average energy is: " + str(Average)
    elif Average >= 4:
        return "Chill playlist. Your average energy is: "+ str(Average)
    else:
        return "You need a better playlist gng.  Your average energy is: "+ str(Average)

print(analyze_playlist(Energy_List))