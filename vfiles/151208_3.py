price = input('Enter product price:')
price = float(price)
point = input('Enter your point:')
point = int(point)
Discount = point/500
Total = (price-Discount)
print(f'Discount: {Discount:.2f}')
print(f'Total: {Total:.2f}')