price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)

point_2 = point/500
Total= price-point_2

print("Discount:%.2f"% point_2)
print("Total:%.2fBaht" %Total )