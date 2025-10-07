cp = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
cs = float(input('Please enter the number of parking hours: '))
result = 0
h1 = 0
if cs > 0:
    if cp == 1:
        if cs < 1:
            print('Parking fee: 0.00 THB')
        else:
            h1 = 1 * 10
            result = (cs - 1) * 5
            result = result + h1
            print(f'Parking fee: {result:.2f} THB')
    elif cp == 2:
        if cs < 1:
            print('Parking fee: 0.00 THB')
        else:
            h1 = 1 * 30
            result = (cs - 1) * 15
            result = result + h1
            print(f'Parking fee: {result:.2f} THB')
    else:
        print('Invalid vehicle type')
else:
    print('Please enter a valid number of parking hours')