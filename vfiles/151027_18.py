#500 point = 1 bath
# price : 5
# point : 500/1 * 5 ==> output : yourpoint : 2500 points
p = input("Enter price:")
price = float(p)
point = 500/1*price
print("Total price : %.2f / your point : %.2f points"% (price,point))