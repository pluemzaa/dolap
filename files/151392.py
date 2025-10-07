price = input("Enter product price:")
point = input("Enter your point:")
point = float(point)
price = float(price)
Discount = 1/500 * point
Discount = float(Discount)
Total   = price - Discount
Total   = float(Total)
print("Discount: %.2f" % Discount)
print("Total: %.2f Baht" % Total)