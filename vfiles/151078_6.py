product = input("Enter product price: ")
price = float(product)
point = int(input("Enter your point: "))
#point = int(point)
discout = point/500
total = price-discout
print("Discount:", discout)
print(f"Total: {total:.2f} Baht")