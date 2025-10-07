# Enter price : 500 ===> 1 bath -> 500 point
# Your point : 2.5 points 1/500 * 100000
price = input ("Enter price")
price = float (price)
point = 1/500 * price
print(point)
print("Your point: %.2f point" % point)
#print("Total price %.2f , Your point: %.2f point" % 
print(f"Total price {price:.2f} , Your point: %.2f point")