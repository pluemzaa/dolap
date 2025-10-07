price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = float(point)
Discount = 1/500*point
Total = price-Discount
print(f"Discount: {Discount:.2f}")
print(f"Total: {Total:.2f} Baht")