price = input("Enter price:")
point = input("Enter point:")
discount = input ("Enter discout:")
price = float(price)
point = 1/500 * price
print(point)
print("your point: %.2f" % point)
print("price %.2f bath = %.2f point" % (price,point,discount))