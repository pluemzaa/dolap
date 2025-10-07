price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = float(point)
discount =   point/500.00
val = price - discount

print("Discount:",discount)
print(f"Total: {val:.2f} Baht")