cp = 2.5
cq = 10
tp = 1.5
tq = 0
jp = 3.0
jq = 2
print('Beverage List:')
print('1. Coffee - $2.5 - Quantity: 10')
print('2. Tea - $1.5 - Quantity: 0')
print('3. Juice - $3.0 - Quantity: 2')
p = int(input('Enter the number of the beverage you want to purchase: '))
q = int(input('Enter the quantity you want to purchase: '))
if p == 1:
    if q <= 10 and q >=1 :
        pq = 2.5 * q
        print('You purchased',q,'Coffee for $',pq,)
        print('Enjoy your drink!')
    else:
        print('Sorry, Coffee is out of stock')
if p == 2:
    if q >= 0 :
        print('Sorry, Tea is out of stock')
if p == 3:
    if q <= 2 and q >=1 :
        pq = 3.0 * q
        print('You purchased',q,'Coffee for $',pq,)
        print('Enjoy your drink!')
    else:
        print('Sorry, Juice is out of stock')