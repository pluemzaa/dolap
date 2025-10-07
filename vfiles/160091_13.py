type=int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
hour=float(input('Please enter the number of parking hours: '))
motopri=float
pripri=15
pripriroral=(pripri*hour)+15
ptipti=float
motopri=5
motototal=(motopri*hour)+5
if type ==1 :
    if hour>= 1 : 
        print(f'Parking fee: {motototal:.2f} THB')
    elif hour <1 and hour>0 :
        print('Parking fee: 0.00 THB')
if type==2:
    if  hour>= 1 : 
        print(f'Parking fee: {motototal:.2f} THB')
    elif hour <1 and hour>0 :
        print('Parking fee: 0.00 THB')
if type > 2 :
    print('Invalid vehicle type')
else:
    print('Please enter a valid number of parking hours')