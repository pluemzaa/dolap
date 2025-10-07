li = [['Coffee', 2.5, 10], ['Tea', 1.5, 0], ['Juice', 3.0, 2]]

print('Beverage List:')
for i in range(3):
    print(f'{i+1}. {li[i][0]} - ${li[i][1]} - Quantity: {li[i][2]}')

b = int(input('Enter the number of the beverage you want to purchase: '))
q = int(input('Enter the quantity you want to purchase: '))

if q > li[b-1][2]:
    print(f'Sorry, {li[b-1][0]} is out of stock')
else:
    print(f'You purchased {q} {li[b-1][0]} for ${q * li[b-1][1]}')
    print('Enjoy your drink!')