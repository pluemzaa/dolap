price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = float(point)
Discount = point*1/500
Total = price-Discount
print(f"Discount: {Discount:.2f}")
print(f"Total: {Total:.2f} Bath")