vehicle = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
hours = float(input('Please enter the number of parking hours: '))
if vehicle == 1 or vehicle == 2:
    if hours > 0:
        if vehicle == 1: # Motorcycle
            if hours > 0 and hours < 1:
                print('Parking fee: 0.00 THB')
            elif hours >= 1:
                a = 10+(hours-1)*5
                print('Parking fee: %.2f'%a, 'THB')
        if vehicle == 2: # Personal Car
            if hours > 0 and hours < 1:
                print('Parking fee: 0.00 THB')
            elif hours >= 1:
                b = 30+(hours-1)*15
                print('Parking fee: %.2f'%b, 'THB')
    else:
        print('Please enter a valid number of parking hours')
else:
    print('Invalid vehicle type')