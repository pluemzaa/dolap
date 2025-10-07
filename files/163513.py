mem=str(input('Membership (y/n) : '))
to=float(input('Total amount : '))

if mem == 'y':
    if to >= 1000:
        dis1=float((to*20)/100)
        print(f'Discount : {dis1:.2f}')
        print(f'Final Amount to Pay : {to-dis1:.2f}')
    elif to >=500 and to <= 999:
        dis2=float((10*to)/100)
        print(f'Discount : {dis2:.2f}')
        print(f'Final Amount to Pay : {to-dis2:.2f}')
    else:
        print('Discount : 0.00')
        print(f'Final Amount to Pay : {to:.2f}')
elif to >= 1000:
        dis3=float((to*5)/100)
        print(f'Discount : {dis3:.2f}')
        print(f'Final Amount to Pay : {to-dis3:.2f}')
else:
        print('Discount : 0.00')
        print(f'Final Amount to Pay : {to:.2f}')