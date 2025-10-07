# 500 point = 1 bath
# Price :1 <== input
# point : 1/500 * 500 ==> output : your point : 1 points

price = input("Enter price:")
point = 1/500*float(price)
point = 1/500*price
print("Total price : %.2f / your point : %.2f points"% (price,point))