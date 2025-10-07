price = input("Enter produnct price:")
price = input("Enter your point:")
price = float(price)
point = 1/500 * price
print(point)
print("Enter product price: %.2f point" % point)
print("Total price %.2f Your point: %.2f point" % (price,point))
print(f"Total price {price: %.2f}, Your point:{point : %.2f} point")