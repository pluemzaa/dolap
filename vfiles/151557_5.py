price = input("Enter product price:") 
price = float(price)
point = 12.15513794/1 * price
discount = point/500
print("Enter your point: %.2f" % point)
print(f"Discount: {discount:.2f}\nTotal: {price-discount:.2f} Baht")