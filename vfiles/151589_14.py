price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discount = 1/500 * point
total = price-Discount
print(f"Discount:{Discount %.2f}")
print(f"total:{total: %.2f} Baht")