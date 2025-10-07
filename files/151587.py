price = input('Enter product price: ')
point = input('Enter your point: ')
price = float(price)
point = int(point)
Discount = 1/500 * point
Discount = float(Discount)
Total = price-Discount
print(f'Discount: %.2f \nTotal: %.2f baht'%(Discount,Total))