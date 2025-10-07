price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = point / 500

print("Discount: %.2f" %discount)
print("Total: %.2f Baht" %(price - discount))