price = float(input("Enter product price: "))
point = int(input("Enter your point: "))

discount = point / 500
total = price - discount

print("discount %.2f baht = %.2f points" % (discount, point))
print(f"Total: {total:.2f} Baht")