price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point)
Discount = 1/500*(point)
Total = price - Discount
print(f"Total: {Total:.2f}")