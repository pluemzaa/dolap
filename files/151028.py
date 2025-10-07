price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
Discount = point/500
Total = price - Discount
print(f"Discount: {Discount:.2f}")
print(f"Total: {Total:.2f} Baht" )