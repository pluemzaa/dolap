price = input("Enter poduct price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
Discout = 1/500*point
total = price-Discout
print(f"total: {total:.2f} Bath" )