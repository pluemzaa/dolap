result = 0
sessions = []
while True:
    menu = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
    ti = float(input('Please enter the number of parking hours: '))
    valid = True
    if menu == 1:
        if ti <= 0:
            print('Please enter a valid number of parking hours')
            valid = False
        elif ti < 1:
            result = 0.00
            print('Parking fee: 00.00 THB')
            sessions += [(menu, ti, result)]
        else:
            result = 1 * 10 + (ti - 1) * 5
            print(f'Parking fee: {result:.2f} THB')
            sessions += [(menu, ti, result)]
    elif menu == 2:
        if ti <= 0:
            print('Please enter a valid number of parking hours')
            valid = False
        elif ti < 1:
            result = 0.00
            print('Parking fee: 00.00 THB')
            sessions += [(menu, ti, result)]
        else:
            result = 1 * 30 + (ti - 1) * 15
            print(f'Parking fee: {result:.2f} THB')
            sessions += [(menu, ti, result)]
    else:
        print('Invalid vehicle type')
        valid = False

    con = input('Do you want to continue? (y/n): ')
    print('------------------------------')
    if con == 'n':
        break
    if not valid:
        continue

print('VT Hours Cost')
total = 0
for vt, hours, cost in sessions:
    print(f'{vt} {hours:.2f} {cost:.2f}')
    total += cost
print(f'Total {total:.2f} THB')