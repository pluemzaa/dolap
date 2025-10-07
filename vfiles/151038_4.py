price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
disc = 1/500*point
total = price-disc
print (f"Discount: {disc:.2f}")
print (f"Total: {total:.2f} Bath")