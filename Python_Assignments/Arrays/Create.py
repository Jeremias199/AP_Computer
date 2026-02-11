Car_Brands = ["Toyta", "Ford", "Chevrolet", "Tesla", "Honda"]


def Get_Brand(Cars):
    for i in range(len(Car_Brands)):
        if Cars == Car_Brands[i]:
            return "Correct"
    return "Wrong"


Guess = input("Name of the most popular car brands in the U.S\n")
print(Get_Brand(Guess))