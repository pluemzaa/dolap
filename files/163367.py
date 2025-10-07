beverages = {
    1: {"name": "Coffee", "price": 2.5, "quantity": 10},
    2: {"name": "Tea", "price": 1.5, "quantity": 0},
    3: {"name": "Juice", "price": 3.0, "quantity": 2}
}

print("Beverage List:")
for num, item in beverages.items():
    print(f"{num}. {item['name']} - ${item['price']} - Quantity: {item['quantity']}")
try:
    choice = int(input("\nEnter the number of the beverage you want to purchase: "))
    if choice not in beverages:
        print("Invalid beverage number.")
    else:
        selected = beverages[choice]
        qty = int(input("Enter the quantity you want to purchase: "))
        
       
        if selected['quantity'] < qty or qty <= 0:
            print(f"\nSorry, {selected['name']} is out of stock")
        else:
            total_price = qty * selected['price']
            print(f"\nYou purchased {qty} {selected['name']} for ${total_price:.2f}")
            print("Enjoy your drink!")
except ValueError:
    print("\nInvalid input. Please enter numeric values only.")