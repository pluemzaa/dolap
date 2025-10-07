price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)

discount = point/500
print("discount: %.2f" % discount)

Total = price-discount
print("Total: %.2f" % Total)