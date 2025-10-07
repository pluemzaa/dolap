price = float(input("Enter product price: "))
point =int(input("Enter your point: "))
Discount = 1/500 * point
print(f"Discount: {Discount:.2f}")
print (f"Total: {price-Discount:.2f} Bath")