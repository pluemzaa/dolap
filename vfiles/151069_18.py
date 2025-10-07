price = input('Enter poduct price:')
point = input('Enter your point:')
price = float(price)
point = int(point)
Discout = 1/500*point
total = price-Discout
print('Discout: %.2f' % Discout)
print('total: %.2f Baht' %total)