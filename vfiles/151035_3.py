price = float(input("Enter product price: ")) 
point = float(input("Enter your point: "))
cal = 1/500 * point
discount = price - cal

print(f"Discount: {cal:.2f}")
print(f"Total: {discount:.2f} Bath")