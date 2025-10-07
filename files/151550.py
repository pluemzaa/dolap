price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = float(point)
discount = point/500
total = price-discount
print(f"discount: {discount:.2f}")
print(f"total: {total:.2f} Baht")