price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)
discount = point/500
print("Discount: %.2f" % discount)
print("Total: %.2f Baht" %(price - discount))