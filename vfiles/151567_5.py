price = input("Enter product price:")
price = float(price)
point = input("Enter product point:")
point = float(point)
point_2 = point/500
total = price - point_2
print("Your point: %.2f point" % point)
print("total:%.2f} baht"%total)
#print("total price %.2f,Your point : %.2f point" % (price,point))