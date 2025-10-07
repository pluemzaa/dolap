price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point )
discount=(point/ 500)
val = price - discount

print(f"Discount:{discount:.2f}")
print(f"Total:{val:.2f} Baht")