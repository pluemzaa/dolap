data = []

while True:
    vehicle_type = input("Please enter vehicle type (1: Motorcycle, 2: Personal Car): ")

    if vehicle_type != "1" and vehicle_type != "2":
        print("Invalid vehicle type")
        break

    hours_input = input("Please enter the number of parking hours: ")
    
    is_valid = True
    dot = False
    for ch in hours_input:
        if ch == '.':
            if dot:
                is_valid = False
                break
            dot = True
        elif not ch.isdigit():
            is_valid = False
            break

    if not is_valid:
        print("Please enter a valid number of parking hours")
        break

    hours = float(hours_input)
    if hours <= 0:
        print("Please enter a valid number of parking hours")
        break

    vt = int(vehicle_type)

    if hours < 1:
        fee = 0.00
    else:
        if vt == 1:
            fee = 10 + (hours - 1) * 5
        else:
            fee = 30 + (hours - 1) * 15

    print("Parking fee: %.2f THB" % fee)
    data.append((vt, float("%.2f" % hours), float("%.2f" % fee)))

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

if len(data) > 0:
    total = 0
    print("VT Hours Cost")
    for vt, hrs, cost in data:
        print("%d %.2f %.2f" % (vt, hrs, cost))
        total += cost
    print("Total %.2f THB" % total)