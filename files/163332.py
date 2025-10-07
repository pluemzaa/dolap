coffee_price = 2.5
coffee_qty = 10

tea_price = 1.5
tea_qty = 0

juice_price = 3.0
juice_qty = 2


print("Beverage List:")
print(f"1. Coffee - ${coffee_price:.1f} - Quantity: {coffee_qty}")
print(f"2. Tea - ${tea_price:.1f} - Quantity: {tea_qty}")
print(f"3. Juice - ${juice_price:.1f} - Quantity: {juice_qty}")


choice = int(input("\nEnter the number of the beverage you want to purchase: "))
quantity = int(input("Enter the quantity you want to purchase: "))


if choice == 1:
    if quantity <= coffee_qty:
        total_cost = quantity * coffee_price
        print(f"\nYou purchased {quantity} Coffee for ${total_cost:.1f}")
        print("Enjoy your drink!")
    else:
        print(f"\nSorry, Coffee is out of stock")
elif choice == 2:
    if quantity <= tea_qty:
        total_cost = quantity * tea_price
        print(f"\nYou purchased {quantity} Tea for ${total_cost:.1f}")
        print("Enjoy your drink!")
    else:
        print(f"\nSorry, Tea is out of stock")
elif choice == 3:
    if quantity <= juice_qty:
        total_cost = quantity * juice_price
        print(f"\nYou purchased {quantity} Juice for ${total_cost:.1f}")
        print("Enjoy your drink!")
    else:
        print(f"\nSorry, Juice is out of stock")
else:
    print("\nInvalid choice.")