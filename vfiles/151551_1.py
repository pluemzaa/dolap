# Enter price : 500 ===> 200 bath -> 1 point
# Your point : 2.5 points 1/200 * 500
price = input ("Enter price")
price = float (price)
point = 1/200 * price
print(point)
print("Your point: %.2f point" % point)
print("Total price %.2f , Your point: %.2f point" % (price,point))
print(f"Total price {price:.2f} , Your point: %.2f point")