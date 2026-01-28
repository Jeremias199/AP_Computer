Converted_Celsius = 0
Converted_Fahrenheit = 0
print("Type 1: Fahrenheit to Celsius \nType 2: Celsius to Fahrenheit")

Choice_Num = input("Convert: ")

if Choice_Num == "1":
    Fahrenheit = input("F: ")
    Conv_C = (Fahrenheit_Temp - 32) * 0.5555556
    print(Conv_C, "F")
elif Choice_Num == "2":
    Celsius = input("C: ")
    Conv_F = (Celsius * 0.5555556) + 32
    print(Conv_F, "C")
