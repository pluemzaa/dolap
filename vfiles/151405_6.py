price=float(input('Enter product price: '))
point=float(input('Enter your point: '))
discout=1/500*point
total= point-discout
print(f'Discount: {discout:.2f}')
print(f'Total: {total:.2f} Baht')