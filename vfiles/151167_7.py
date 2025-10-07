price = input(float("Enter product price: "))
point = input(int("Enter your point: "))
discount = point/500
print(f"Discount: {discount:.2f}")
total = price - discount
print(f"Total: {total:.2f} Baht")