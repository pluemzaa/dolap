price = input('Enter product price:' )
price = float(price)
point = input("Enter your point:" )
point = int(point)
discount = point/500
total = price-discount
print(f"Enter product price: {price:.2f} ")
print("Enter your point:",point)
print(f'Discount: {discount:.2f}')
print(f"Total: {total:.2f} Baht")