car = 30
mor = 10

carhour = 0
morhour = 0

m = 0
c = 0

totalcar = 0
totalmor = 0

while True:
    v = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): "))
    hour = float(input("Please enter the number of parking hours: "))
    if v < 1 or v > 2:
        print("Invalid vehicle type")
    elif hour <= 0:
        print("Please enter a valid number of parking hours")
    else:
        if v == 1:
            if hour < 1:
                price = mor * 0
            elif hour >= 1 and hour < 2:
                price = mor
            else:
                price = mor + ((hour - 1) * 5)
            print(f"Parking fee: {price:.2f} THB")
            totalmor += price
            morhour += hour
            m += 1
        elif v == 2:
            if hour < 1:
                price = car * 0
            elif hour >= 1 and hour < 2:
                price = car
            else:
                price = car + ((hour - 1) * 15)
            print(f"Parking fee: {price:.2f} THB")
            totalcar += price
            carhour += hour
            c += 1
    con = input("Do you want to continue? (y/n): ")
    print("------------------------------")
    if con == "n":
        break

if c > 0 or m > 0:
    print("VT Hours Cost")
    if m >= 1:
        print(f"1 {morhour:.2f} {totalmor:.2f}")
    if c >= 1:
        print(f"2 {carhour:.2f} {totalcar:.2f}")
    total = totalcar + totalmor
    print(f"Total {total:.2f} THB")