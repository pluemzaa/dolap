price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = int(point)

discount = (point/500) *1
total = price-discount

print(f"discount: {discount:.2f}")
print(f"total: {total:.2f} Baht")