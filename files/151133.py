price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
print(f"Discount: {point/500:.2f}")
print(f"Total: {price - (point/500):.2f} Baht")