price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = int(point)
Discount = point/500
total = price - discount

print("Discount: %.2f" % Discount)
print("Total: %.2f Bath" %total)