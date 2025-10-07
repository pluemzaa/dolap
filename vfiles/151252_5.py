price = input("enter product price:")
price = float(price)
point = input("enter your point:")
point = float(point)

DC = (point/500)
Realprice = price - DC

print(f"Discount: {DC:.2f}")
print(f"Total: {Realprice:.2f}Baht")