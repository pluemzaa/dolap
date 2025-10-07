price = input("Enter product price: ")
price = float(price)
point = input("Enter your point: ")
point = int(point)
discout = point/500
total = price-discout
print( "Discount: ", discout)
print(f"Total: {total:.2f} Baht")