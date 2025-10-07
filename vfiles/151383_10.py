price = input("Enter product price:")
point = input("Enter your ponit:")
price = float(price)
point = int(point)
Discount = 1/500 * point
total = price - discount
print("Discount: %.2f" % Discount)
print("total: %.2f Baht" % total)