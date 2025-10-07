price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point)
Discount = 1/500 * point
print("Discount: %.2f" %Discount )
Total = price - Discount
print(f"Total: {Total:.2f} Baht")