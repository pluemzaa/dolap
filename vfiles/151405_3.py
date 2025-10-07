price=input('Enter product price: ')
price=float(price)
point=input('Enter your point: ')
point=int(point)
discout=1/500*point
total= price-discout
print('Discount: ',discout)
print('total:',total,'Baht')