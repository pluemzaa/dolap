price = input("Enter product_price :")
point = input("Enter point :")
price = float(price)
point = float(point)
point = 1/500* point
total = price-point
total =float(total)
print("Discount :%.2f" % point)
print("Total :%.2f baht" % total)