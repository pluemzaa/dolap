coffee_price = 2.5
coffee_qty = 10
tea_price = 1.5
tea_qty = 0
juice_price = 3.0
juice_qty = 2

print("Beverage List:")
print("1. Coffee - $2.5 - Quantity:", coffee_qty)
print("2. Tea - $1.5 - Quantity:", tea_qty)
print("3. Juice - $3.0 - Quantity:", juice_qty)

choice = int(input("Enter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

# ตรวจสอบและประมวลผล
if choice == 1:
    if coffee_qty < qty:
        print("Sorry, Coffee is out of stock")
    else:
        total = coffee_price * qty
        print(f"You purchased {qty} Coffee for ${total}")
        print("Enjoy your drink!")
elif choice == 2:
    if tea_qty < qty:
        print("Sorry, Tea is out of stock")
    else:
        total = tea_price * qty
        print(f"You purchased {qty} Tea for ${total}")
        print("Enjoy your drink!")
elif choice == 3:
    if juice_qty < qty:
        print("Sorry, Juice is out of stock")
    else:
        total = juice_price * qty
        print(f"You purchased {qty} Juice for ${total}")
        print("Enjoy your drink!")
else:
    print("Invalid choice")