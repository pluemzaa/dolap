price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = int(point)
Discount = 0
if point >= 500:
  discount = 1
  total_price = price - discount
print(f"discount : {discount:.2f} Bath")
print(f"total : {total_price:.2f} Bath")