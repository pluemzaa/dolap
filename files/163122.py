beverages = []
    {"name": "Coffee", "price": 2.5, "quantity": 10},
    {"name": "Tea",    "price": 1.5, "quantity": 0},
    {"name": "Juice",  "price": 3.0, "quantity": 2},

print("Beverage List:")
for i, b in enumerate(beverages, start=1):
    print(f"{i}. {b['name']} - ${b['price']} - Quantity: {b['quantity']}")
choice = int(input("Enter the number of the beverage you want to purchase: "))
qty = int(input("Enter the quantity you want to purchase: "))

if 1 <= choice <= len(beverages):
    beverage = beverages[choice - 1]

    if beverage["quantity"] < qty or beverage["quantity"] == 0:
        print(f"Sorry, {beverage['name']} is out of stock")
    else:
        total_price = beverage["price"] * qty
        print(f"You purchased {qty} {beverage['name']} for ${total_price:.1f}")
        print("Enjoy your drink!")
else:
    print("Invalid selection")