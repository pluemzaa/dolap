parking_records = []
total_fee = 0

while True:
    vt = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    if vt not in ['1', '2']:
        print("Invalid vehicle type")
        break

    try:
        hours = float(input("Please enter the number of parking hours: "))
    except:
        print("Please enter a valid number of parking hours")
        break

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")
        print("------------------------------ ")
        if cont.lower() == 'y':
            continue
        else:
            break

    if hours < 1:
        fee = 0.00
    else:
        if vt == '1':
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:05.2f} THB")
    parking_records.append([vt, hours, fee])
    total_fee += fee

    cont = input("Do you want to continue? (y/n): ")
    print("------------------------------ ")
    if cont.lower() != 'y':
        break

if parking_records:
    print("VT Hours Cost")
    for rec in parking_records:
        print(f"{rec[0]} {rec[1]:.2f} {rec[2]:05.2f}")
    print(f"Total {total_fee:.2f} THB")