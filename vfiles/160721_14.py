records = []
while True:

    try:
        vt_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
        vt = int(vt_input)
        if vt not in [1, 2]:
            print("Invalid vehicle type")
            break
    except:
        print("Invalid vehicle type")
        break

    try:
        hours_input = input("Please enter the number of parking hours: ")
        hours = float(hours_input)
        if hours <= 0:
            print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")

        if cont.lower() != 'y':
            break
        else:
            continue
    except:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ")

        if cont.lower() != 'y':
            break
        else:
            continue

    if hours < 1:
        fee = 0.00
    elif vt == 1:
        fee = 10 + (hours - 1) * 5
    elif vt == 2:
        fee = 30 + (hours - 1) * 15
    if hours < 1:
        fee = 0.00
    elif vt == 1:
        fee = 10 + (hours - 1) * 5
    elif vt == 2:
        fee = 30 + (hours - 1) * 15

    print(f"Parking fee: {fee:.2f} THB")
    records.append((vt, hours, fee))

    cont = input("Do you want to continue? (y/n): ")

    if cont.lower() != 'y':
        break