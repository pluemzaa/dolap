price = input("Enter product price: ")
point = int(input("Enter your point: "))
price = float(price)
discount = 1/500 * point
result = price - discount
print("Discount: %.2f" % discount)
print("Total: %.2f Baht" % result )