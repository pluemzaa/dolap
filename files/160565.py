mhc1 = 0
mhc2 = 0
to1 = 0
to2 = 0

while True:
    park = int(input('Please enter vehicle type (1: Motorcycle, 2: Personal Car): '))
    mh = float(input('Please enter the number of parking hours: '))
    if park == 1:


        if mh < 1 and mh >= 0:
            cas1 = 0
        elif mh >= 1:
            cas1 = 10 + (mh - 1) * 5
        elif mh < 0:
            print("Please enter a valid number of parking hours")
            pass
        print(f"Parking fee: {cas1:.2f} THB")

        if mh >= 0:
            mhc1 = mhc1 + mh
            to1 = to1 + cas1


    elif park == 2:
        if mh < 1 and mh >= 0:
            cas = 0

        elif mh >= 1:
            cas = 30 + (mh - 1) * 15

        elif mh < 0:
            print("Please enter a valid number of parking hours")
            pass
        print(f"Parking fee: {cas:.2f} THB")

        if mh >= 0:
            mhc2 = mhc2 + mh
            to2 = to2 + cas

    else:
        print('Invalid vehicle type')
        pass

    co = input('Do you want to continue? (y/n):')
    print('------------------------------')
    if co == 'y':
        continue
    elif co == 'n':
        pass
    else:
        break
    if mhc1>0 and mhc2>0:
        print('VT Hours Cost')
        print(f'1 {mhc1:.2f} {to1:.2f}')
        print(f'2 {mhc2:.2f} {to2:.2f}')
        total = to1 + to2
        print(f'Total {total:.2f} THB')
    elif mhc1>0 and mhc2 == 0:
        print('VT Hours Cost')
        print(f'1 {mhc1:.2f} {to1:.2f}')
        print(f'Total {to1:.2f} THB')
    elif mhc2>0 and mhc1 == 0:
        print('VT Hours Cost')
        print(f'1 {mhc2:.2f} {to2:.2f}')
        print(f'Total {to2:.2f} THB')
    break