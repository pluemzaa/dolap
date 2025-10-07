price = float(input("Enter product price:"))
point = float(input("Enter your point:"))
Discount = 1/500*point
print(f"Discount: {Discount:.2f}")
a = price-Discount

print("Your point : %.2f point" % point)
print(f"Total: {price:.2f} Baht" )