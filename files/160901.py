parking_records = []

while True:
    try:
        vehicle_type = int(input("Please enter vehicle type (1: Motorcycle, 2: Personal Car):"))
        hours = float(input("Please enter the number of parking hours:"))

        if vehicle_type not in [1, 2]:
            print("Invalid vehicle type")
        elif hours <= 0:
            print("Please enter a valid number of parking hours:")
        else:
            if hours < 1:
                cost = 0.00
            else:
                if vehicle_type == 1:
                    cost = 10 + (hours - 1) * 5
                else:
                    cost = 30 + (hours - 1) * 15

            print(f"Parking fee: {cost:.2f} THB")
            parking_records.append((vehicle_type, hours, cost))
    except ValueError:
        print("Invalid input. Please enter numbers only")

    cont = input("Do you want to continue? (y/n): ").strip().lower()
    print("------------------------------")
    if cont != 'y':
        break

if parking_records:
    print("VT Hours Cost")
    total = 0
    for vt, h, c in parking_records:
        print(f"{vt} {h:.2f} {c:.2f}")
        total += c
    print(f"Total {total:.2f} THB")