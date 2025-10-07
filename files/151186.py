price = input("Enter product price: ")
point = input("Enter your point: ")
point = int(point)
price = float(price)
discount = int(point)/500
total = price - discount

print (f"Discount: {discount:.2f}")
print (f"Total: {total:.2f} Baht")