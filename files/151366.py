price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
Discount = int(point)/500
print(f"Discount: {Discount:.2f}")
print(f"Total: {price-Discount:.2f} Baht")