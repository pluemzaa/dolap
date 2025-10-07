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
quantity = int(input("Enter the quantity you want to purchase: "))

if choice == 1:
    name = "Coffee"
    price = coffee_price
    stock = coffee_qty
elif choice == 2:
    name = "Tea"
    price = tea_price
    stock = tea_qty
elif choice == 3:
    name = "Juice"
    price = juice_price
    stock = juice_qty
else:
    print("Invalid selection")
    raise SystemExit

if stock <= 0 or quantity > stock:
    print(f"Sorry, {name} is out of stock")
else:
    total = price * quantity
    print(f"You purchased {quantity} {name} for ${total}")
    print("Enjoy your drink!")