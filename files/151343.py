product_price = float(input("Enter product price: "))
points = int(input("Enter your point: "))

Discount = points/500
print("Discount: %.2f" % Discount)
Total = product_price-Discount
print("Total: %.2f" % Total, "Baht")