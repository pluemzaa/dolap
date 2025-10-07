price = input("Enter poduct price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
discout = 1/500*point
total = price-discout
print(f"total: {total:.2f} Bath" )