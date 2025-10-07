price = input("Enter product price:")
price = float(price)
point = input("Enter your point:" )
point = int(point)
Discount = point/500
Total = price-discount
print(f"Enter product price: {price:.2f}")
print("Enter your point:",point)
print(f"Discount: {Discount:.2f}")
print(f"Total: {Total:.2f} Baht")