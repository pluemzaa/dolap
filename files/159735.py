Veh = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
hrs = float(input('Please enter the number of parking hours: '))
result = 0
t1 = 0
if hrs > 0:
    if Veh == 1:
        if hrs < 1:
            print('Parking fee: 0.00 THB')
        else:
            t1 = 1 * 10
            result = (hrs - 1) * 5
            result = result + t1
            print(f'Parking fee: {result:.2f} THB')
    elif Veh == 2:
        if hrs < 1:
            print('Parking fee: 0.00 THB')
        else:
            t1 = 1 * 30
            result = (hrs- 1) * 15
            result = result + t1
            print(f'Parking fee: {result:.2f} THB')
    else:
        print('Invalid vehicle type')
else:
    print('Please enter a valid number of parking hours')