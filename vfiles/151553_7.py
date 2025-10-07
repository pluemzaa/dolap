price = float(input("Enter product price: "))
point = (input("Enter your point: "))
Discount = 1/500*point
print(f"Discount: {Discount:.2f}")
a = price-Discount

print(f"Total: {price:.2f} Baht" )