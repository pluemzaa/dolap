price = input("Enter product price: ")

price = float(price)
point = input("Enter your point: ")
point = int(price)

discount = 1/500*point
print(f"Discount: {discount:2f}")
total = price-discount
print(f"Total: {total:2f} Baht")