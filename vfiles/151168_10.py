# Enter product price: 1250.50
# Enter your point: 15200
# Discount: 30.40
# Total: 1220.10 Baht

price = float(input("Enter product price:"))
point = int(input("Enter your point: "))

Discount1 = (point / 500)
R_price = price - Discount1

print(f"Discount{Discount1:.2f}")
print(f"Total{R_price:.2f} Bath")