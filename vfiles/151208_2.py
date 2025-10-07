price = input('Enter product price:')
price = float(price)
point = input('Enter your point:')
point = int(point)
dis = point/500
Total = (price-dis)
print(f'Discount: {dis:.2f}')
print(f'Total: {Total:.2f}')