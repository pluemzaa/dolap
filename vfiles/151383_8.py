price = input("Enter product price:")
point = input("Enter your ponit:")
price = float(price)
point = int(point)
discount = 1/500 * point
print("Discount: %.2f" % discount)
total = price - discount
print("Total: %.2f Baht" % total)