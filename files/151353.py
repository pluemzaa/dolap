price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = int(point)
Discount = point * 1/500
Discount = float(Discount)
total = (price - Discount)

print("Discount: %.2f" % Discount)
print("Total: %.2f Baht" % total)