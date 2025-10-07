price = input("Enter price:")
price = float(price)
point = 1/500 * price
print(point)
print("your point: %.2f" % point)
print(f"price {price:.2f} bath = {point:.2f} point")