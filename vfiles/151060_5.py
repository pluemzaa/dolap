price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
point1 = point/500
discount = price/point1
total = price-discount
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")