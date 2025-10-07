price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point)
disc = 1/500*point
disc = float(disc)
total = price-disc
total = float(total)
print (f"Discount: {disc:.2f}")
print (f"Total: {total:.2f} Baht")