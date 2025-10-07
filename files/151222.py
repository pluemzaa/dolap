price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
discount = 1/500 * point

print(f"Discount: {discount:.2f}")
print(f"Total: {price-discount:.2f} Baht")