# กำหนดข้อมูลสินค้า
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

# รับข้อมูลจากผู้ใช้
beverage = int(input("Enter the number of the beverage you want to purchase: "))
quantity = int(input("Enter the quantity you want to purchase: "))

# ตรวจสอบและประมวลผลคำสั่งซื้อ
if beverage == 1:
    if quantity > coffee_qty or coffee_qty == 0:
        print("Sorry, Coffee is out of stock")
    else:
        total_price = quantity * coffee_price
        print(f"You purchased {quantity} Coffee for ${total_price:.1f}")
        print("Enjoy your drink!")
elif beverage == 2:
    print("Sorry, Tea is out of stock")
elif beverage == 3:
    if quantity > juice_qty or juice_qty == 0:
        print("Sorry, Juice is out of stock")
    else:
        total_price = quantity * juice_price
        print(f"You purchased {quantity} Juice for ${total_price:.1f}")
        print("Enjoy your drink!")
else:
    print("Invalid beverage selection.")