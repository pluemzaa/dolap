price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = float(point)
discount = 1/500 * point
discount = float(discount)
print("Discount: %.2f" % discount)
print(f"Total: {(price)-(discount):.2f} Baht")