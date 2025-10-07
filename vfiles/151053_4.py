price = input("Enter prodct price:")
point = input("Enter your point:")
price = float(price)
point = int(point)
discount = point/500
print("Discount: %.2f" % discount)
print(f "Total price: {price:.2f - discount:.2f} bath")