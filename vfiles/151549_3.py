price = float(input("Enter product price: "))
point = float(input("Enter your point: "))

point_price = point / 500
tolot =  price - point_price
print("Discount: %.2f" % point_price)
print("Total:%.2f" % tolot)