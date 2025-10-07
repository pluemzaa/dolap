# 1 bath = 500 point
# price : 1
# point : 1 * 500 ==> output : yourpoint : 500 points

p = input("Enter price :")
price = float(price)
point = 1/500*price
print(f"Total price : {price:.2f} / your point : {point:.2f}"% (price,point))