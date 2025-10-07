#Enter price:500===>200 bath->1 point
#your point:2.5 point 1/200*500
price=500
point=1/200* price
print(point)
print("Your point:%.2f point"%point)
#print("Total price %.2f,Your point:%.2f point" % (price,point))
print(f"Total price {price:.2f},Your point: {point:.2f} point")