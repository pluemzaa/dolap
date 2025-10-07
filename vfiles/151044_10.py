price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)
discout = float(1/500*point)
total = price-discout
print(f"Discount: {discout}")
print(f"Total: {total} Baht")