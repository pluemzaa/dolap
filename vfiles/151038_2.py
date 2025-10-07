price = input("Enter product price:")
price = float(price)
point = input("Enter your point:")
point = float(point)
disc = 1/500*point
total = price-disc
print ("Discount: %.2f"%disc)
print ("Total: %.2f Bath"%total)