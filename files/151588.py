price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = (point /500) * 1.0
total = price - discount
print(f"discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")