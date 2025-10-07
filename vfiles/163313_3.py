print('Beverage List:')
print('1. Coffee - $2.5 - Quantity: 10')
print('2. Tea - $1.5 - Quantity: 0')
print('3. Juice - $3.0 - Quantity: 2')

coffee_price = 2.5
coffee_qty = 10
tea_price = 1.5
tea_qty = 0
juice_price = 3
juice_qty = 2

num = int(input('Enter the number of the beverage you want to purchase: '))
quan = int(input('Enter the quantity you want to purchase: '))

if num == 1:
    if quan > coffee_qty:
        print('Sorry, Coffee is out of stock')
    else:
        total = quan*2.5
        print(f'You purchased {quan} Coffee for ${total}')
        print('Enjoy your drink!')
        
elif num == 2:
    if quan >= tea_qty:
        print('Sorry, Tea is out of stock')
    else:
        total = quan*1.5
        print(f'You purchased {quan} Tea for ${total}')
        print('Enjoy your drink!')

elif num == 3:
    if quan > juice_qty:
        print('Sorry, Juice is out of stock')
    else:
        total = quan*3
        print(f'You purchased {quan} Juice for ${total}')
        print('Enjoy your drink!')