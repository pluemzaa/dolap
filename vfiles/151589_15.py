price = float(input("Enter product price:"))
point = int(input("Enter your point:"))
Discount = point/500
total = price-Discount
print(f"Discount:{Discount %.2f}")
print(f"total:{total: %.2f} Baht")