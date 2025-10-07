price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = 1/500 * price
Discount = float(input("Discount: "))
Total = price-Discount
print(f"Total: {Total:.2f} Baht ")