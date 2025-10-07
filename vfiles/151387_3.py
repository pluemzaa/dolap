a = input("Enter product price:")
b = input("Enter your point:")
a = float(a)
b = int(b)
point = b/500
Total = a-point

print("Discount: %.2f" % point)
print("Total: %.2f Baht" % Total)