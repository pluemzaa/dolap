price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = float(point/500)

print(f"Discount: {discount:.2f}")
print(f"Total: {price-discount:.2f} Baht")