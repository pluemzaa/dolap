price = input("Enter product price: ")
price = float(price)
point = input("Enter Your point: ")
point = float(point)

Discount = point/500
Total = price - Discount

print("Discount:%.2f" % Discount)
print("Total:%.2fBaht" %Total)