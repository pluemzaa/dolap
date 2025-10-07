price = float(input("Eter product price: "))
point = int(input("Enter your point: "))
discount = (point /500) * 1
total = price - discount
print(f"discount: {discount:.2f} Baht")
print(f"Total: {total:.2f} Baht")