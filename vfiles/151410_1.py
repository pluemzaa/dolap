price = input("Enter product price")
price = float(price)
point = input("Enter your point")
point = float(point)
point = 1/500 * point
print("Discount %2f" % point)
pi = price - point
print(f"total:{pi:.2f} baht")