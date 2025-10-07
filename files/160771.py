mhours = 0
chours = 0
mprice = 0
cprice = 0
ccount = 0
mcount = 0
while True:
    vehicle = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hours = float(input("Please enter the number of parking hours: "))
    if vehicle == 1 or vehicle == 2:
        if hours > 0:
            if vehicle == 1: # Motorcycle
                if hours > 0 and hours < 1:
                    a = 0
                elif hours >= 1 and hours < 2:
                    a = 10
                elif hours >= 2:
                    a = 10+((hours-1)*5)
                print('Parking fee: %.2f'%a, 'THB')
                mhours += hours
                mprice += a
                mcount += 1
            if vehicle == 2: # Personal Car
                if hours > 0 and hours < 1:
                    b = 0
                elif hours >= 1 and hours < 2:
                    b = 30
                elif hours >= 2:
                    b = 30+((hours-1)*15)
                print('Parking fee: %.2f'%b, 'THB')
                chours += hours
                cprice += b
                ccount += 1
        else:
            print('Please enter a valid number of parking hours')
    else:
        print('Invalid vehicle type')
    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == 'n':
         break
if mcount >= 1 or ccount >= 1:
    print("VT Hours Cost")
    if mcount >= 1:
        print(f"1 {mhours:.2f} {mprice:.2f}")
    if ccount >= 1:
        print(f"2 {chours:.2f} {cprice:.2f}")
    total = mprice + cprice
    print(f"Total {total:.2f} THB")