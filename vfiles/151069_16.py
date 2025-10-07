price = input('Enter poduct price:')
price = float(price)
point = input("Enter your point:")
point = int(point)
Discout = 1/500*point
total = price-Discout
print('Discout: %.2f' % Discout)
print('total: %.2f Baht' %total)