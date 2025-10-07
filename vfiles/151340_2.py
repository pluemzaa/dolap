price = float(input('Enter product price: '))
point = float(input('Enter your point: '))
discount = 1/500 * point
total = price - discount
print(f'Discount: {discount:.2f}')
print(f'Total: {total:.2f} Baht')