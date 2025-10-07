price = float(input("Enter product price: "))
point = int(input("Enter product point: "))
discout = 1/500*point
total = price-discout
print(f"Discount: {discout}")
print(f"Total: {total}")