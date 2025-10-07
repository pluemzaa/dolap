print("Beverage List:")
print("1. Coffee - $2.5 - Quantity: 10")
print("2. Tea - $1.5 - Quantity: 0")
print("3. Juice - $3.0 - Quantity: 2")
a = input("Enter the number of the beverage you want to purchase: ")
b = int(input("Enter the quantity you want to purchase: "))
c = 0
if b >= 0:
    if a == "1":
        if b <= 10:
            c = b*2.5
            print(f"You purchased {b} Coffee for ${c}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Coffee is out of stock")
    elif a == "2":
        if b <= 0:
            c = b*1.5
            print(f"You purchased {b} Tea for ${c}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Tea is out of stock")
    elif a == "3":
        if b <= 2:
            c = b*3.0
            print(f"You purchased {b} Juice for ${c}")
            print("Enjoy your drink!")
        else:
            print("Sorry, Juice is out of stock")
else:
    pass