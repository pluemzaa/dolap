ty = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
ti = float(input('Please enter the number of parking hours: '))
result = 0
h1 = 0
if ti > 0:
    if ty == 1:
        if ti < 1:
            print('Parking fee: 0.00 THB')
        else:
            h1 = 1 * 10
            result = (ti - 1) * 5
            result = result + h1
            print(f'Parking fee: {result:.2f} THB')
    elif ty == 2:
        if ti < 1:
            print('Parking fee: 0.00 THB')
        else:
            h1 = 1 * 30
            result = (ti - 1) * 15
            result = result + h1
            print(f'Parking fee: {result:.2f} THB')
    else:
        print('Invalid vehicle type')
else:
    print('Please enter a valid number of parking hours')