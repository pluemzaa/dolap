price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)
discount = point/500
total = price - discount
print(f"Discount: {discount:.2f})
print(f"Total: {total:.2f} Bath")