price = float(input("Enter product price: "))
point = int(input("Enter your point: "))
discount = 1/500*point
print(f"Discount: {discount:.2f}")
total = price - discount
print(f"Total: {total:.2f} Haht")