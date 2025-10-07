coffee_price = 2.5
coffee_qty = 10
tea_price = 1.5
tea_qty = 0
juice_price = 3.0
juice_qty = 2

print("Beverage List:")
print(f"1. Coffee - ${coffee_price} - Quantity: {coffee_qty}")
print(f"2. Tea - ${tea_price} - Quantity: {tea_qty}")
print(f"3. Juice - ${juice_price} - Quantity: {juice_qty}")

choice = int(input("Enter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

if choice == 1:
    name, price, available = "Coffee", coffee_price, coffee_qty
elif choice == 2:
    name, price, available = "Tea", tea_price, tea_qty
elif choice == 3:
    name, price, available = "Juice", juice_price, juice_qty
else:
    print("Invalid selection")
    name = None

if name is not None:
    if qty <= available and available > 0:
        total = price * qty
        print(f"You purchased {qty} {name} for ${total}")
        print("Enjoy your drink!")
    else:
        print(f"Sorry, {name} is out of stock")