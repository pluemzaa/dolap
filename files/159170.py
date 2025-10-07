v = input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): ')
t = float(input('Please enter the number of parking hours: '))
if v == '1':
    if t <1 and t >0:
        print('Praking fee: 0.00 THB')
    elif t <=0:
        print('Please enter a valid number of parking hours')
    elif t == 1:
        print('Parking fee: 10.00 THB')
    elif t>1:
        fee = 10+(t-1)*5
        print(f'Parking fee: {fee:.2f} THB')
elif v =='2':
    if t<1 and t>0:
        print('Parking fee: 0.00 THB')
    elif t<=0:
        print('Please enter a valid number of parikng hours')
    elif t == 1:
        print('Parking fee: 30.00 THB')
    elif t>1:
        fee = 30+(t-1)*15
        print(f'Parking fee: {fee:.2f} THB')
else:
    print('Invalid vehicle type')