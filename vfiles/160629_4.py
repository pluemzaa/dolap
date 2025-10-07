price1 = 0
price2 = 0

hour_moter = 0
hour_car = 0
while True:
    a = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    b = float(input("Please enter the number of parking hours: "))
    c = ((b-1)*5 +10)
    d = ((b-1)*15 +30)

    if a == 1:
        if b >= 1:
            hour_moter += b
            if b >= 1 and b < 2:
                print("Parking fee: 10.00 THB")
                price1 += 10
            else:
                m = "Parking fee: %.2f" %(c)
                print((m),"THB")
                price1 += c
        elif b < 0:
                print("Please enter a valid number of parking hours")
        else:
            print("Parking fee: 0.00 THB")
    elif a == 2:
        if b >= 1:
            hour_car += b
            if b >= 1 and b < 2:
                print("Parking fee: 30.00 THB")
                price2 += 30
            else:
                car = ("Parking fee: %.2f" %(d))
                print((car),"THB")
                price2 += d
        elif b < 0:
                print("Please enter a valid number of parking hours")
        else:
            print("Parking fee: 0.00 THB")
    else:
        print("Invalid vehicle type")

    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == 'n':
         break

total = price1 + price2
print("VT Hours Cost")

if hour_moter > 0:
     print(f'1 {hour_moter:.2f} {price1:.2f}')

if hour_car > 0:
     print(f'1 {hour_car:.2f} {price2:.2f}')
     
print(f"Total {total:.2f} THB")