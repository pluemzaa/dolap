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

choice = int(input("\nEnter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

if choice == 1:
    if qty > coffee_qty:
        print("\nSorry, Coffee is out of stock")
    else:
        total = qty * coffee_price
        print(f"\nYou purchased {qty} Coffee for ${total:.2f}")
        print("Enjoy your drink!")
elif choice == 2:
    if qty > tea_qty:
        print("\nSorry, Tea is out of stock")
    else:
        total = qty * tea_price
        print(f"\nYou purchased {qty} Tea for ${total:.2f}")
        print("Enjoy your drink!")
elif choice == 3:
    if qty > juice_qty:
        print("\nSorry, Juice is out of stock")
    else:
        total = qty * juice_price
        print(f"\nYou purchased {qty} Juice for ${total:.2f}")
        print("Enjoy your drink!")
else:
    print("\nInvalid choice. Please select a beverage from the list.")