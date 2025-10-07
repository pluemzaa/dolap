price = input("Enter product price:")
price = float(price)
point = input("Enter your point: ")
point = int(point)
dis = point/500
total = price-dis
print("Discount: %.2f" % dis)
print("Total: %.2f Baht"% total)