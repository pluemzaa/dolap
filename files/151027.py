pr = float(input("Enter product price: "))
pi = float(input("Enter your point: "))
discount = pi / 500
total = pr - discount
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")