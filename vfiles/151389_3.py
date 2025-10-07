price = input("Enter product price:")
price = float(price)
point = int(input("Enter your point"))
discount = 1 / 500 * point
total = price - discount
print("Discount : %.2f Discount" % discount)
print("Total : %.2f baht" % total)