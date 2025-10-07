# Price :1 <== input
# point : 1/500 * 500 ==> output : your point : 1 points

price = float(input("Enter price:"))
point = 500/1*float(price)
print(price)
print(point)
print("Total price : %.2f / your point : %.2f points"%(point,price))