price = input("Enter product price ")
points = input("Enter your point:")
discount = min(points,500)
total = price-discount
price = float(price)
point = 1/200*price
print("Total price : %.2f/ your point : %.2f points"% (price,point))