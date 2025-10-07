price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = float(point)
discount = 1/500*point
total = price-discount
price(f"Discount: {discount:.2f}")
price(f"Total: {total:.2f} Baht")