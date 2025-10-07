price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
discount = point/500
total = price-discount
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f}")