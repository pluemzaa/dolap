# 200 bath = 1point
# price : 500
# point : 1/200 * 500 ==> output : yourpoint : 2.50 points

p = input("Enter price:")
price = float(p)
point = 1/200*price
print("Total price : %.2f / your point : %.2f points"% (price,point))

print(f"Total price : {price:.2f} / your point : {point:.2f}")