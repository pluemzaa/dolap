records = []
while True:
    vt_input = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")
    try:
        vt = int(vt_input)
    except ValueError:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == 'y':
            continue
        else:
            break
    if vt not in [1, 2]:
        print("Invalid vehicle type")
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == 'y':
            continue
        else:
            break

    hours_input = input("Please enter the number of parking hours: ")
    try:
        hours = float(hours_input)
    except ValueError:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == 'y':
            continue
        else:
            break

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont == 'y':
            continue
        else:
            break

    if hours < 1:
        cost = 0.0
    else:
        if vt == 1:
            cost = 10 + 5 * (hours - 1)
        elif vt == 2:
            cost = 30 + 15 * (hours - 1)
        else:
            cost = 0.0 
    print(f"Parking fee: {cost:.2f} THB")
    records.append((vt, hours, cost))  

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont == 'y':
        continue
    else:
        break


print()
if records:
    print("VT Hours Cost")
    total = 0.0
    for rec in records:
        print(f"{rec[0]} {rec[1]:.2f} {rec[2]:.2f}")
        total += rec[2]
    print(f"Total {total:.2f} THB")