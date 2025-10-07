price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
discount = 1/500 * point
print("Discount: %.2f" % discount)
total = price - discount
print("Total: %.2f Bath" % total)