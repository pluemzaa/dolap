m = input('Membership (y/n) : ')
t = float(input('Total amount : '))
r = 0
d = 0
if m == 'y':
    if 500 <= t <= 999:
        d = t * 0.1
        r = t - d
        print(f'Discount : {d:.2f}')
        print(f'Final Amount to Pay : {r:.2f}')
    elif t >= 1000:
        d = t * 0.2
        r = t - d
        print(f'Discount : {d:.2f}')
        print(f'Final Amount to Pay : {r:.2f}')
    else:
        print('Discount : 0.00')
        print(f'Final Amount to Pay : {t:.2f}')
elif t >= 1000:
    d = t * 0.05
    r = t - d
    print(f'Discount : {d:.2f}')
    print(f'Final Amount to Pay : {r:.2f}')
else:
    print('Discount : 0.00')
    print(f'Final Amount to Pay : {t:.2f}')