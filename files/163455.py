print("""Beverage List:
1. Coffee - $2.5 - Quantity: 10
2. Tea - $1.5 - Quantity: 0
3. Juice - $3.0 - Quantity: 2""")
s = int(input('Enter the number of the beverage you want to purchase: '))
q = int(input('Enter the quantity you want to purchase:'))

cf = 2.5
te = 1.5
ju = 3.0

if (s==1) and (0<q<=10):
    print(f'You purchased {q} Coffee for ${(q*cf):.1f}\nEnjoy your drink!')
elif (s==1) and (q>10):
    print('Sorry, Coffee is out of stock')
elif (s==2) and (q>0):
    print('Sorry, Tea is out of stock')
elif (s==3) and (q<2):
    print(f'You purchased {q} Juice for ${(q*ju):.1f}\nEnjoy your drink!')
elif (s==3) and (q>2):
    print('Sorry, Juice is out of stock')