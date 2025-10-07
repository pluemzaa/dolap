price = input("Enter product price: ")
point = input("Enter your point: ")

point = float(point)
price = float(price)

point_2 = point/500

total = price - point_2
print("Discount: %.2f" % point_2 )
print("Total: %.2f" %total)