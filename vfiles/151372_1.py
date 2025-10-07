# 200 bath = 1 point
# price : 500
# point : 1/200 * 500 ==> output : your point : 2.50 points

price = input("Enter price:")
price = float(price)
point = 1/500*price
print(f"Total price : %.2f / Your point : %.2f points"% (point,point))