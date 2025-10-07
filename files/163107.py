# กำหนดราคาและจำนวนสินค้า
coffee_price = 2.5
coffee_qty = 10

tea_price = 1.5
tea_qty = 0

juice_price = 3.0
juice_qty = 2

# แสดงเมนูสินค้า
print("Beverage List:")
print(f"1. Coffee - ${coffee_price} - Quantity: {coffee_qty}")
print(f"2. Tea - ${tea_price} - Quantity: {tea_qty}")
print(f"3. Juice - ${juice_price} - Quantity: {juice_qty}")

# รับค่าจากผู้ใช้
choice = int(input("\nEnter the number of the beverage you want to purchase: "))
quantity = int(input("Enter the quantity you want to purchase: "))

# ตรวจสอบการสั่งซื้อ
if choice == 1:
    if quantity > coffee_qty:
        print("Sorry, Coffee is out of stock")
    else:
        total = quantity * coffee_price
        print(f"You purchased {quantity} Coffee for ${total}")
        print("Enjoy your drink!")
elif choice == 2:
    if quantity > tea_qty:
        print("Sorry, Tea is out of stock")
    else:
        total = quantity * tea_price
        print(f"You purchased {quantity} Tea for ${total}")
        print("Enjoy your drink!")
elif choice == 3:
    if quantity > juice_qty:
        print("Sorry, Juice is out of stock")
    else:
        total = quantity * juice_price
        print(f"You purchased {quantity} Juice for ${total}")
        print("Enjoy your drink!")
else:
    print("Invalid selection. Please choose 1, 2, or 3.")