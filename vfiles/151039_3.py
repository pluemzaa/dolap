price = input("Enter product price:")
point = input("Enter your point:")
price = float(price)
point = float(point)
dis = point/500
disf = float(dis)
total = price-disf
print(f"Discount: {disf:.2f}")
print(f"Total: {total:.2f}")