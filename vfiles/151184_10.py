price = float(input("Enter product price: "))
point =int(input("Enter your point: "))
discount = 1/500 * point
print(f"Discount: {discount:.2f}")
print (f"Total: {price-discount:.2f} Bath")