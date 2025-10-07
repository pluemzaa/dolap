price = inout("Enter product price")
price = float(price)
point = 1/500 * price
print(point)
print("Enter Your point: %.2f point" % point)
print(f"Total price {price : .2f} , Your point: {point: .2f} point")