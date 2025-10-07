p = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Dis = 1/500 * point
print(f"Discount: {Dis:.2f}")
total = p-Dis
print(f"Total: {total:.2f} Bath")