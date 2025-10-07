price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discout = float(1/500*point)
total = price-discout
print(f"Discount: {discout:.2f}")
print(f"Total: {total:.2f} Baht")