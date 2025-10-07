m = input('Membership (y/n) : ')
to = float(input('Total amount : '))
if m == 'y':
    if to >= 1000:
        d = (to / 100) * 20
        print(f'Discount : {d:.2f}')
        f = to - d
        print(f'Final Amount to Pay : {f:.2f}')
    elif to >= 500 and to <= 999:
        d = (to / 100) * 10
        print(f'Discount : {d:.2f}')
        f = to - d
        print(f'Final Amount to Pay : {f:.2f}')
    else:
        d = 0.00
        print(f'Discount : {d:.2f}')
        f = to -d
        print(f'Final Amount to Pay : {to:.2f}')

elif m == 'n':
    if to >= 1000:
        d = (to / 100) * 5
        print(f'Discount : {d:.2f}')
        f = to - d
        print(f'Final Amount to Pay : {f:.2f}')
    
    elif to <= 1000 and to != 0:
        d = 0.00
        print(f'Discount : {d:.2f}')
        f = to -d
        print(f'Final Amount to Pay : {f:.2f}')

    else:
        d = 0.00
        print(f'Discount : {d:.2f}')
        f = to -d
        print(f'Final Amount to Pay : {to:.2f}')

else:
    pass