member = input('Membership (y/n) : ')
total = int(input('Total amount : '))

if member == 'y':
    if total >= 1000:
        dis = (total*20)/100
    elif 500 <= total <= 999:
        dis = (total*10)/100
    else:
        dis = 0
        
elif member == 'n':
    if total >= 1000:
        dis = (total*5)/100
    else:
        dis = 0

final = total - dis

print(f'Discount : {dis:.2f}')
print(f'Final Amount to Pay : {final:.2f}')