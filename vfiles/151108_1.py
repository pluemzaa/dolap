price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point)
Discount = 1/500 * point
Discount = float(Discount)
total_price = price - Discount 
print(f"Discount :{Discount:.2f}")
print(f"Discount :{total_price:.2f}")