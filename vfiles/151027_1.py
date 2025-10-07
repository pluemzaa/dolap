# 1 bath = 500point
# price : 1
# point : 1/500 * 500 ==> output : yourpoint : 2.50 points

p = input("Enter price:")
price = float(price)
point = 1/200*price
print("Total price : %.2f / your point : %.2f points"% (price,point))

print(f"Total price : {price:.2f} / your point : {point:.2f}"% (price,point))