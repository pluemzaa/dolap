price = float(input("Enter product price: "))
collectpoint = float(input("Enter your point: "))

discount = collectpoint / 500
totalprice = price - discount
print(f"Discount: {discount:.2f}")
print(f"Total: {totalprice:.2f} Baht ")