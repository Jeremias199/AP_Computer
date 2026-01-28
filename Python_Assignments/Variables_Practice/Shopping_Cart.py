Item_1 = "Coffee"
Item_2 = "Uranium 235 Pound Cake"
Item_3 = "Eggs"
Item_4 = "Milk"

Item_1_Price = 10
Item_2_Price = 3
Item_3_Price = 12
Item_4_Price = 5

Tax_Rate = 0.1
Subtotal = Item_1_Price + Item_2_Price + Item_3_Price + Item_4_Price
Total = Subtotal * Tax_Rate

print("*******************")
print("*******************")
print("*******Items*******")
print(Item_1,"\n", Item_2, "\n", Item_3, "\n", Item_4)
print("*******************")
print("*******************")
print("Subtotal: ", Subtotal)
print("Total: ", Total)
print("*******************")
