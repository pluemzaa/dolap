price = float(input("Enter product price: ")) 
point = float(input("Enter your point: "))
cal = 1/500 * price
discount = price - cal

print(f"Discount: {cal}")
print(f"Total: {discount} Bath")