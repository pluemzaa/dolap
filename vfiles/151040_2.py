price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = float(point)
discount = 1/500*point
total = price-discount
print("Discount: "discount)
print(f"Total: {price:.2f} Baht")