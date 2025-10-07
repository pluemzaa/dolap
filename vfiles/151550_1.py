price = input("Enter product price:")
price = float(price)
point = 1/200 * price
print(point)
print("Your point: %.2f point" % point)
#print("Total price %.2f , Your point: %.2f point" % (point,point))
print(f"Total price {price:.2f} , Your point: {point:.2f} point")