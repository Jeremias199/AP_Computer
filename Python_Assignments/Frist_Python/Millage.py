from multiprocessing.managers import SharedMemoryManager

print("Hello!")

Ask_Miles = int(input("How many miles did you travel from here? "))
Ask_Gallons = int(input("How many gallons did you have before you got here? "))

time = Ask_Miles / Ask_Gallons
print("Your MPG is " , time)

