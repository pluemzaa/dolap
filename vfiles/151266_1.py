price = input("Enter price: ")
price = float(price) 
point = input("Enter price: ")
point = int(price) 
discount = 1/500 * point

print(f"discount: {discount:.2f}")
print(f"Total: {price-discount:.2f} baht")