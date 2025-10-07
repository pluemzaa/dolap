price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
point = 1/500 * point
print("Discount: %.2f" % point)
print(f"Total: {price:.2f} baht = {point:.2f} Baht")