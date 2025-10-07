price = input('Enter product price:' )
price = float(price)
point = input("Enter your point:" )
point = int(point)
discount = point/500
total = price-discount
print(f"Enter product price: {price:.2f} ")
print("Enter your point:",point)
print(f'discount: {discount:.2f}')
print(f"total: {total:.2f} Baht")