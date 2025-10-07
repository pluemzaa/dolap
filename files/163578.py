# Fixed prices and quantities
coffee_price, coffee_qty = 2.5, 10
tea_price, tea_qty = 1.5, 0
juice_price, juice_qty = 3.0, 2


print("Beverage List:")
print(f"1. Coffee - ${coffee_price} - Quantity: {coffee_qty}")
print(f"2. Tea - ${tea_price} - Quantity: {tea_qty}")
print(f"3. Juice - ${juice_price} - Quantity: {juice_qty}")


choice = input("Enter the number of the beverage you want to purchase: ").strip()
qty_str = input("Enter the quantity you want to purchase: ").strip()

# Validate numeric inputs
if not (choice.isdigit() and qty_str.isdigit()):
    
    exit()

choice = int(choice)
qty = int(qty_str)

# Map choice to item data
items = {
    1: ("Coffee", coffee_price, coffee_qty),
    2: ("Tea", tea_price, tea_qty),
    3: ("Juice", juice_price, juice_qty),
}

if choice not in items or qty <= 0:
    
    exit()

name, price, stock = items[choice]

# Out-of-stock: กรณีไม่มีของเลย หรือของไม่พอ
if stock <= 0 or qty > stock:
    print(f"Sorry, {name} is out of stock")
else:
    total = price * qty
    # ตัวอย่างในโจทย์พิมพ์ $7.5 (ไม่บังคับสองตำแหน่ง)
    print(f"You purchased {qty} {name} for ${total}")
    print("Enjoy your drink!")