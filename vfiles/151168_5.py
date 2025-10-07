price = ("Enter product price:")
point = int(input("Enter your point: "))

Discount1 = float(point / 500)
R_price = price - Discount1

print("Discount: %.2f" %Discount1)
print("Total: %.2f bath" %R_price)