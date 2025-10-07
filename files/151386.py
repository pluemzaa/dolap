price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = int(point)
Discount = 1/500 * point
print(f"Discount : {Discount:.2f} ")
total = price - Discount
print(f"total: {total:.2f} Baht")