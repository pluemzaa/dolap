#print('Hello Python!')
price = float(input("Enter product point:"))
point = int(input("Enter your point:"))
discount = point / 500
total = price - discount
print(f"discount: {discount:.2f}")
print(f"total: {total:.2f} Bath")