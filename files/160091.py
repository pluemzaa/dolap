type=int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
hour=float(input('Please enter the number of parking hours: '))

if type not in [1, 2]:
    print('Invalid vehicle type')
elif hour <= 0:
    print('Please enter a valid number of parking hours')
elif type == 1:
    if hour < 1:
        print('Parking fee: 0.00 THB')
    else:
        fee = (5 * hour) + 5
        print(f'Parking fee: {fee:.2f} THB')
elif type == 2:
    if hour < 1:
        print('Parking fee: 0.00 THB')
    else:
        fee = (15 * hour) + 15
        print(f'Parking fee: {fee:.2f} THB')