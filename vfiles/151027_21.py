#500 point = 1 bath <==input
# price : 5 
# point : 500/1 * 5 ==> output : yourpoint : 2500 points
p = input("Enter price:")
p = input("Enter point:")
price = float(p)
point = 500/1*price
print("Total price : %.2f / your point : %.2f points"% (price,point))