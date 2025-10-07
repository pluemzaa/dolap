coffee_price = 2.5
coffee_qty = 10
tea_price = 1.5
tea_qty = 0
juice_price = 3.0
juice_qty = 2

print("Beverage List:")
print("1. Coffee - $", coffee_price, "- Quantity:", coffee_qty)
print("2. Tea - $", tea_price, "- Quantity:", tea_qty)
print("3. Juice - $", juice_price, "- Quantity:", juice_qty)

cs = int(input("Enter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

if cs == 1:
    if qty > coffee_qty:
        print("Sorry, Coffee is out of stock")
    else:
        total = coffee_price * qty
        print("You purchased", qty, "Coffee for $", total)
        print("Enjoy your drink!")
elif cs == 2:
    if qty > tea_qty:
        print("Sorry, Tea is out of stock")
    else:
        total = tea_price * qty
        print("You purchased", qty, "Tea for $", total)
        print("Enjoy your drink!")
elif cs == 3:
    if qty > juice_qty:
        print("Sorry, Juice is out of stock")
    else:
        total = juice_price * qty
        print("You purchased", qty, "Juice for $", total)
        print("Enjoy your drink!")
else:
    print("Invalid cs")