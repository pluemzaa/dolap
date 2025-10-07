n = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
i = float(input('Please enter the number of parking hours: '))
result = 0
prx = 0
if i > 0:
    if n == 1:
        if i < 1:
            print("Parking fee: 0.00 THB")
        else:
            prx = 1 * 10
            result = (i - 1) * 5
            result = result + prx
            print(f'Parking fee: {result:.2f} THB')
    elif n == 2:
        if i < 1:
            print('Parking fee: 0.00 THB')
        else:
            prx = 1 * 30
            result = (i - 1) * 15
            result = result + prx
            print(f'Parking fee: {result:.2f} THB')
    else:
        print('Invalid vehicle type')
else:
    print('Please enter a valid number of parking hours')