price = input("Enter price:")
price = float(price)
point = input("Enter point: ")
point = int(point)
discount = point/500
Total = price-discount
print(f"Total: {Total:.2f} baht")