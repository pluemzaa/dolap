price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
dis = point/500
dis = float(dis)
total = price - dis

print(f"Discount: {dis:.2f}")
print(f"total: {total:.2f} Baht")