# Enter price: 1 ===> 500baht - > 1 point
# your point : 2.50 points  1/200 * 500
price = input("Enter price:")
price = float(price)
point =1/200 * price
print(point)
print("your point: %.2f point" % point)
#print("Total price %.2f , Your point: {point")
print(f"Total price {price:.2f} , Your point: {point}")