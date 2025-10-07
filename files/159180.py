v = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
h = float(input('Please enter the number of parking hours:'))

if v == 1:
   if 0 < h < 1:
       fee = 0
       print(f'Parking fee: {fee:.2f} THB')
   elif h == 1:
       fee = 10
       print(f'Parking fee: {fee:.2f} THB')
   elif h > 1:
       fee = 10 + 5*(h-1)
       print(f'Parking fee: {fee:.2f} THB')
   else:
       print('Please enter a valid number of parking hours')
       
elif v == 2:
   if 0 < h < 1:
       fee = 0
       print(f'Parking fee: {fee:.2f} THB')
   elif h == 1:
       fee = 30
       print(f'Parking fee: {fee:.2f} THB')
   elif h > 1:
       fee = 30 + 15*(h-1)
       print(f'Parking fee: {fee:.2f} THB')
   else:
       print('Please enter a valid number of parking hours')
else:
    print('Invalid vehicle type')