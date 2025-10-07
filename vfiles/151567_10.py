price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)

Discount = point/500
Total = price - Discount

print("Discount: %.2f point" % point)
print("Total:%.2f} baht"%Total)