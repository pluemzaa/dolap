price = input("Enter product price: ")
point = input("Enter your point: ")
price = float(price)
point = int(point)
discout = point/500
total = price - discout

print(f"Discount: {discout:.2f}") 
print(f"Total: {total:.2f} Baht")