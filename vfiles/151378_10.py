price =input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point= int(point)
discount = point/500
total= price-discount
print("Discount: %.2f" % discount)
print("Total: %.2f Bath" % total)