product = input("Enter product price:")
product = float(product)
point = int(input("Enter your point:"))
discout = point/500
price = product-discout
print(f"Discount: {discout:.2f} \nTotal: {price:.2f} Baht")