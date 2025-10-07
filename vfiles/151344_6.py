price = input("Enter product price")
price = float(price)
point = input("Enter your point")
point = int(point)
Discount = 1/500 * point
Discount = float(Discount)
Total = (price - Discount)
print("Your Discount : %.2f" % Discount)
print("Your Total : %.2f Bath " % Total)