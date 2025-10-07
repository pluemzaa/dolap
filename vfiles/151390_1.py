price = input("enter product price")
price = float(price)
point = input("Enter your point")
point = int(point)
Discount = 1/500 * point
total = price-Discount
print("Discount: %.2f" % Discount)
print("total: %.2f baht" % total)