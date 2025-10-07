price = input("Enter price:")
price = float (price)
point = 1/500 * price
print("Your point: %.2f point" % point)
print("Total point: %.2f , your point: %.2f point" % (price,point))
print(f"Total price {price:.2f}, Your point:  {point:.2f} point")