price = input("Enter product price: ")
point = input("Enter your point: ")
Discount = float(point/500)
Total = float(price)-Discount
print(f"Discount:{Discount:.2f}")
print(f"Total: {Total:.2f}")