# ให้นักศึกษาสร้างโปรแกรมสำหรับกำหนดการทำงานของตู้กดเครื่องดื่มกระต่ายบิน

# 1. โปรแกรมจะต้องแสดงเมนูสินค้า ดังนี้
print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")

# data_stock = {
#     "Coffee":10,
#     "Tea":0,
#     "Juice":2          
#               }
data_stock = (10, 0, 2)
data_price = (2.5, 1.5, 3.0)
data_labels = ("Coffee", "Tea", "Juice")

# Enter the number of the beverage you want to purchase: 2
# Enter the quantity you want to purchase: 3
product = int(input("Enter the number of the beverage you want to purchase: "))
quantity = int(input("Enter the quantity you want to purchase: "))

if data_stock[product-1]<quantity:
    print(f"Sorry, {data_labels[product-1]} is out of stock")
else:
    print(f"You purchased {quantity} {data_labels[product-1]} for ${quantity*data_price[product-1]:.1f}")
    print("Enjoy your drink!")