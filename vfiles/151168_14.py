price = input("Enter product price: ")
price = float(price)
point = float(input("Enter your point: "))

Discount1 = (point / 500)
R_price = price - Discount1

print(f"Discount: {Discount1:.2f}")
print(f"Total: {R_price:.2f} Bath")