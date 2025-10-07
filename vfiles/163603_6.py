print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")

x = int(input("Enter the number of the beverage you want to purchase: "))
y = int(input("Enter the quantity you want to purchase: "))

Coffee_price = 2.5
Tea_price = 1.5
Juice_price = 3.0

Coffee_qty = 10
Tea_qty = 0
Juice_qty = 2

if x == 1:
    if y > Coffee_qty:
        print("Sorry, Coffee is out of stock")
    else:
        print(f"You purchased {y} Coffee for NaN")
        print("Enjoy your drink!")

elif x == 2:
    if y > Tea_qty:
        print("Sorry, Tea is out of stock")
    else:
        print(f"You purchased {y} Tea for NaN")
        print("Enjoy your drink!")

elif x == 3:
    if y > Juice_qty:
        print("Sorry, Juice is out of stock")
    else:
        print(f"You purchased {y} Juice for NaN")
        print("Enjoy your drink!")

else:
    print("Invalid choice!")