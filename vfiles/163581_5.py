print('Beverage List:\n1. Coffee - $2.5 - Quantity: 10\n2. Tea - $1.5 - Quantity: 0\n3. Juice - $3.0 - Quantity: 2')
n1 = int(input('Enter the number of the beverage you want to purchase: '))
n2 = int(input('Enter the quantity you want to purchase: '))
coffee_price=2.5
coffee_qty=10
coffee_price=2.5
if n1 == 1:
    if n2 <= 10:
        r = 2.5 * n2
        print(f'You purchased {n2} Coffee for ${r}')
        print('Enjoy your drink!')
    else:
        print('Sorry, Coffee is out of stock')
elif n1 == 2:
    
    if n2 > 0:
        r = 1.5 * n2
        print(f'You purchased {n2} Tea for ${r}')
        print('Enjoy your drink!')
    else:
        print('Sorry, Tea is out of stock')
elif n1 == 3:
    if 0 < n2 <= 2:
        r = 3.0 * n2
        print(f'You purchased {n2} Juice for ${r}')
        print('Enjoy your drink!')
    else:
        print('Sorry, Juice is out of stock')