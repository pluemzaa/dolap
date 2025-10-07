prict = input("Enter product price:")
point = input("Enter your point:")
prict = float(prict)
point = float(point)
Discount = point/500
print(f"Discount: {Discount:.2f}")
Total = prict-Discount
Total = float(Total)
print(f"Total: {Total:.2f} Baht")