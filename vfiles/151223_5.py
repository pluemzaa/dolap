price = input("Enter price:")
price = float(price)
point = input("Enter point:")
point = int(point)
discount = point/500
Total = (price-discount)
print(f"Discount: {discount:.2f}")
print(f"Total: {Total:.2f} baht")