pri = input("Enter product price:")
poi = input("Enter your point:")

pri = float(pri)
poi = int(poi)

discount = (poi/500) * 1.0

total = pri - discount
print(f"Discount: {discount:.2f}")
print(f"Total: {total:.2f} Baht")