price = input("Enter product price: ")
point = input("Enter product point: ")
price = float(price)
point = int(point)
discout = float(1/500*point)
total = price-discout
print(f"Discount: {discout}")
print(f"Total: {total}")