result = 0
m1 = 0  
m2 = 0  
t1 = 0  
t2 = 0  

while True:
    menu = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
    ti = float(input('Please enter the number of parking hours: '))

    if menu == 1:
        if ti <= 0:
            print('Please enter a valid number of parking hours')
        elif ti < 1:
            fee = 0.00
            print('Parking fee: 00.00 THB')
            m1 += fee
            t1 += ti
            result += fee
        else:
            fee = 10 + (ti - 1) * 5
            print(f'Parking fee: {fee:.2f} THB')
            m1 += fee
            t1 += ti
            result += fee
    elif menu == 2:
        if ti <= 0:
            print('Please enter a valid number of parking hours')
        elif ti < 1:
            fee = 0.00
            print('Parking fee: 00.00 THB')
            m2 += fee
            t2 += ti
            result += fee
        else:
            fee = 30 + (ti - 1) * 15
            print(f'Parking fee: {fee:.2f} THB')
            m2 += fee
            t2 += ti
            result += fee
    else:
        print('Invalid vehicle type')

    con = input('Do you want to continue? (y/n): ')
    print('------------------------------')
    if con == 'n':
        break

print('VT Hours Cost')
sums1 = [(1, t1, m1),(2, t2, m2)]
for vt, Hours, cost in sums1:
    if Hours > 0:
        print(f'{vt} {Hours:.2f} {cost:.2f}')
print(f'Total {result:.2f} THB')