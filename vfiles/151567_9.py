price = input("Enter product price:")
price = float(price)
point = input("Enter product point:")
point = float(point)
Discount = point/500
Total = price - Discount
print("Your point: %.2f point" % point)
print("Total:%.2f} baht"%Total)
#print("Total price %.2f,Your point : %.2f point" % (price,point))