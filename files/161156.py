records = []
total_cost = 0.0

while True:
    print("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ", end="")
    try:
        vehicle_type = int(input())
    except ValueError:
        print("Invalid vehicle type")
        break

    if vehicle_type not in [1, 2]:
        print("Invalid vehicle type")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        if cont != 'y':
            print("------------------------------")
            break
        print("------------------------------")
        continue

    print("Please enter the number of parking hours: ", end="")
    try:
        hours = float(input())
    except ValueError:
        print("Please enter a valid number of parking hours")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        if cont != 'y':
            print("------------------------------")
            break
        print("------------------------------")
        continue

    if hours <= 0:
        print("Please enter a valid number of parking hours")
        print("Do you want to continue? (y/n): ", end="")
        cont = input().strip().lower()
        if cont != 'y':
            print("------------------------------")
            break
        print("------------------------------")
        continue

    if hours < 1:
        cost = 0.00
    else:
        if vehicle_type == 1:
            cost = 10 + (hours - 1) * 5
        elif vehicle_type == 2:
            cost = 30 + (hours - 1) * 15

    print(f"Parking fee: {cost:.2f} THB")
    records.append((vehicle_type, hours, cost))
    total_cost += cost

    print("Do you want to continue? (y/n): ", end="")
    cont = input().strip().lower()
    if cont != 'y':
        print("------------------------------")
        break
    print("------------------------------")

if records:
    print("VT Hours Cost")
    for rec in records:
        vt, hr, cs = rec
        print(f"{vt} {hr:.2f} {cs:.2f}")
    print(f"Total {total_cost:.2f} THB")