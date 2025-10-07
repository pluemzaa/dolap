price = input("Enter price")
price = float(price)
point = 500/1 * price
print(point)
print("Enter product price: %.2f point" % point)
print("Total price %.2f Your point: %.2f point" % (price,point))
print(f"Total price {price: %.2f}, Your point:{point : %.2f} point")